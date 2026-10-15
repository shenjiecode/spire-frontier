"""Compare every entity/directory article with current Xiaoheihe evidence.

Exact text/number matches are distinguished from semantic review. Source
tables and sections stay queryable even when a safe field mapping is absent.
Never promotes a candidate based only on a matching translated name.
"""
from __future__ import annotations
import hashlib
import json
import re
import sqlite3
import unicodedata
from collections import Counter, defaultdict

from lxml import html, etree
from bootstrap_sample import ROOT, DB_PATH, add_claim
from discover_inventory import XIAO_CORE_BLOCKS, XIAO_INTRO_TAGS
from build_records import HEADINGS
from refresh_xiao_review import OUT
from review_semantics import notation,load_decisions,decision_for


def clean(text):
    text = re.sub(r'[\u200b-\u200f\ufeff]', '', str(text or ''))
    return ' '.join(text.replace('请输入图片描述', '').replace('输入图片描述', '').split())


def norm(text):
    text = unicodedata.normalize('NFKC', clean(text)).casefold()
    text = re.sub(r'#[rgbypw]', '', text).replace('nl', '')
    return re.sub(r'[\s。，、；：！？,.!?:;“”"（）()\[\]【】]', '', text)


def numbers(text):
    return re.findall(r'(?<![\w])\d+(?:\.\d+)?|\d+(?:\.\d+)?', clean(text))


def span_text(root, start=None, stop=None):
    active = start is None
    chunks = []
    for action, node in etree.iterwalk(root, events=('start','end')):
        if action == 'start':
            if node is stop:
                break
            if node is start:
                active = True
            if active and node.text:
                chunks.append(node.text)
        elif active:
            if node.tag in ('br','p','div','li','tr','h1','h2','h3','h4','h5','h6'):
                chunks.append('\n')
            if node.tail:
                chunks.append(node.tail)
    return '\n'.join(x for line in ''.join(chunks).splitlines() if (x := clean(line)))


def parse_page(raw,card_name=None):
    root = html.fromstring(raw.decode('utf-8')).xpath('//*[contains(concat(" ",normalize-space(@class)," ")," article-content ")]')[0]
    for bad in root.xpath('.//script|.//style'):
        bad.drop_tree()
    tables=[]
    for ti,t in enumerate(root.xpath('.//table'),1):
        rows=[]
        for tr in t.xpath('.//tr'):
            rows.append([clean(td.text_content()) for td in tr.xpath('./th|./td')])
        tables.append(dict(locator=f'table[{ti}]',rows=rows))
    heads=[h for h in root.xpath('.//h1|.//h2|.//h3|.//h4|.//h5|.//h6')
           if clean(h.text_content()) and not h.xpath('ancestor::table') and 'img-desc' not in h.get('class','')]
    sections=[]
    for i,h in enumerate(heads):
        stop=next((n for n in heads[i+1:] if int(n.tag[1])<=int(h.tag[1])),None)
        text=span_text(root,h,stop)
        title=clean(h.text_content())
        if text.startswith(title): text=text[len(title):].strip()
        role='advice' if title.strip('：: ') in HEADINGS else 'rule_notes' if title in ('注意','备注') else 'other'
        sections.append(dict(heading=title,text=text,role=role,locator=f'heading[{i+1}]'))
    captions=[]
    h1=[h for h in heads if h.tag=='h1']
    beta=next((h for h in heads if '测试画风' in clean(h.text_content())),None)
    before=[]
    for node in root.iter():
        if node is beta:break
        before.append(node)
    for node in before:
        if 'img-desc' in node.get('class','') and clean(node.text_content()):
            captions.append(clean(node.text_content()))
    card=[]
    for i,h in enumerate(h1):
        title=clean(h.text_content())
        if '测试画风' in title:break
        if title in HEADINGS:break
        stop=h1[i+1] if i+1<len(h1) else beta
        text=span_text(root,h,stop)
        if text.startswith(title):text=text[len(title):].strip()
        # A useful image caption belongs to the main card; later embedded
        # cards (e.g. Insight on Study) are examples, not extra card effects.
        descendants=[];started=False
        for node in root.iter():
            if node is stop:break
            if node is h:started=True
            elif started:descendants.append(node)
        useful=[clean(n.text_content()) for n in descendants if 'img-desc' in n.get('class','') and clean(n.text_content())]
        if useful:text=useful[0]
        text=re.split(r'此卡为',text,1)[0].strip()
        if text:card.append(dict(variant='upgrade' if '+' in title else 'base',text=clean(text)))
    if not card:
        card=[dict(variant='base' if i==0 else 'upgrade',text=v) for i,v in enumerate(captions[:2])]
    if card_name:
        images=[n for n in before if n.tag=='img' and (not n.get('data-width') or int(n.get('data-width','0'))>=150)]
        if images:
            card=[]
            for i,node in enumerate(images[:2]):
                stop=images[i+1] if i+1<len(images) else beta
                text=span_text(root,node,stop)
                lines=[line for line in text.splitlines() if norm(line) not in (norm(card_name),norm(card_name+'+'))]
                text=clean(' '.join(lines))
                text=re.split(r'此卡为',text,1)[0].strip()
                text=re.sub(re.escape(card_name)+r'\+?$', '', text).strip()
                if text:card.append(dict(variant='base' if i==0 else 'upgrade',text=text))
    else:
        card=[]
    return dict(text=span_text(root),tables=tables,sections=sections,card_descriptions=card)


def scope(category,subcategory):
    if category in XIAO_CORE_BLOCKS or (category=='游戏入门介绍' and subcategory in XIAO_INTRO_TAGS):return 'foundation'
    if category=='每日挑战随机特殊效果':return 'daily_modifier'
    if category in ('职业打法','遗物选择'):return 'wiki_strategy'
    return 'site_or_intro'


def fields(content):
    result={}
    for table in content['tables']:
        for cells in table['rows']:
            if len(cells)==2:result.setdefault(cells[0],cells[1])
            elif len(cells)==1 and re.match(r'^(稀有度|角色)[:：]',cells[0]):
                k,v=re.split('[:：]',cells[0],1);result[k]=v
    return result


def main():
    c=sqlite3.connect(DB_PATH);c.row_factory=sqlite3.Row
    c.execute('PRAGMA foreign_keys=ON')
    c.executescript((ROOT/'schemas/003_xiao_review.sql').read_text(encoding='utf-8'))
    directory=json.loads((OUT/'directory.json').read_text(encoding='utf-8'))
    manifest=json.loads((OUT/'manifest.json').read_text(encoding='utf-8'))
    checks=[]
    decisions=load_decisions()
    def check(e,aid,path,current,source,note='',status=None):
        if status is None:
            if source is None:status='not_in_source_text'
            elif current is None or current=='':status='missing_in_database'
            elif norm(current)==norm(source):status='match'
            elif isinstance(current,str) and isinstance(source,str) and notation(current)==notation(source):
                status='equivalent_notation';note='中文数量词与阿拉伯数字、空白或标点写法等价；不属于规则冲突。'
            elif isinstance(source,(int,float,list,dict)):status='different'
            elif numbers(current)!=numbers(source):status='numeric_or_text_difference'
            else:status='text_difference'
        decision=decision_for(decisions,e,aid,path,current,source)
        if decision:
            status=decision['status'];note=decision['reason']
        key='|'.join((e,aid or '',path))
        checks.append(dict(id='xcheck.'+hashlib.sha256(key.encode()).hexdigest()[:24],entity_id=e,
                           article_id=aid,field_path=path,current_json=json.dumps(current,ensure_ascii=False),
                           source_json=json.dumps(source,ensure_ascii=False),status=status,note=note))
    with c:
        c.execute('DELETE FROM xiao_directory')
        for chunk in directory['result']['chunk']:
            for block in chunk.get('block',[]):
                for tag in block.get('tag_list',[]):
                    for entry in tag.get('block_entries') or []:
                        if not entry.get('article_id'):continue
                        category=clean(block.get('block_title'));subcategory=clean(tag.get('tag_name'))
                        c.execute('INSERT OR IGNORE INTO xiao_directory VALUES(?,?,?,?,?)',
                                  (str(entry['article_id']),clean(entry.get('entry_name') or entry.get('article_name')),
                                   category,subcategory,scope(category,subcategory)))
        c.execute('DELETE FROM xiao_field_checks');c.execute('DELETE FROM xiao_entity_pages')
        for aid in [r[0] for r in c.execute('SELECT DISTINCT article_id FROM xiao_directory ORDER BY article_id')]:
            m=manifest.get(aid,{})
            fallback=False
            if m.get('error'):
                previous=c.execute("SELECT * FROM source_pages WHERE source_id='xiaoheihe' AND article_id=? AND parser_version!='xiao-review/1' ORDER BY fetched_at DESC LIMIT 1",(aid,)).fetchone()
                if previous and previous['snapshot_path'] and (ROOT/previous['snapshot_path']).exists():
                    m=dict(url=previous['url'],path=previous['snapshot_path'],sha256=hashlib.sha256((ROOT/previous['snapshot_path']).read_bytes()).hexdigest(),fetched_at=previous['fetched_at'])
                    fallback=True
            if not m.get('path'):
                c.execute('INSERT OR REPLACE INTO xiao_page_review VALUES(?,NULL,NULL,?,?)',(aid,'fetch_failed' if m.get('error') else 'pending_fetch',m.get('error','missing')));continue
            raw=(ROOT/m['path']).read_bytes()
            if hashlib.sha256(raw).hexdigest()!=m['sha256']:raise ValueError(f'Snapshot hash mismatch {aid}')
            card_title=c.execute("SELECT name FROM xiao_directory WHERE article_id=? AND category IN ('铁甲战士','静默猎手','故障机器人','观者','无色牌','诅咒牌') LIMIT 1",(aid,)).fetchone()
            content=parse_page(raw,card_title[0] if card_title else None)
            pid=f"xiao.review.{aid}.{m['sha256'][:16]}"
            title=c.execute('SELECT name FROM xiao_directory WHERE article_id=? LIMIT 1',(aid,)).fetchone()[0]
            c.execute('''INSERT OR IGNORE INTO source_pages(id,source_id,url,title,article_id,fetched_at,http_status,content_type,snapshot_path,sha256,parser_version,is_index_page)
                         VALUES(?,'xiaoheihe',?,?,?,?,200,'text/html',?,?,'xiao-review/1',0)''',
                      (pid,m['url']+'#snapshot-'+m['sha256'][:16],title,aid,m['fetched_at'],m['path'],m['sha256']))
            c.execute('INSERT OR REPLACE INTO xiao_page_review VALUES(?,?,?,?,?)',
                      (aid,pid,json.dumps(content,ensure_ascii=False),'historical_fallback' if fallback else 'parsed','Current fetch failed; retained historical evidence.' if fallback else 'Parsed source evidence; field checks are not a blanket semantic verification.'))
            # Preserve reviewed identity mappings. Multiple members sharing a
            # monster page remain explicitly shared rather than inheriting HP.
            entities=c.execute('''SELECT DISTINCT e.* FROM entities e JOIN claims cl ON cl.subject_entity_id=e.id
                      JOIN source_pages p ON p.id=cl.source_page_id
                      WHERE p.source_id='xiaoheihe' AND (p.article_id=? OR p.url=?)
                      AND cl.field_path='source.article_text' AND COALESCE(cl.notes,'') NOT LIKE '%superseded:%' ORDER BY e.id''',(aid,m['url'])).fetchall()
            for e in entities:
                c.execute('INSERT OR REPLACE INTO xiao_entity_pages VALUES(?,?,?)',(e['id'],aid,'shared' if len(entities)>1 else 'direct'))
            active=[e for e in entities if e['lifecycle']=='active']
            f=fields(content)
            for e in entities:
                eid=e['id'];kind=e['kind']
                aliases=[r[0] for r in c.execute("SELECT name FROM names WHERE entity_id=? AND language='zh-CN'",(eid,))]
                directory_names=[r[0] for r in c.execute('SELECT DISTINCT name FROM xiao_directory WHERE article_id=?',(aid,))]
                check(eid,aid,'identity.name_zh',aliases,directory_names,status='match' if set(map(norm,aliases))&set(map(norm,directory_names)) else 'shared_page_or_name_difference')
                if kind=='card':
                    data=c.execute('SELECT * FROM cards WHERE entity_id=?',(eid,)).fetchone()
                    tags=[r[0] for r in c.execute('SELECT DISTINCT subcategory FROM xiao_directory WHERE article_id=?',(aid,))]
                    types={'攻击':'Attack','技能':'Skill','能力':'Power','状态卡':'Status'}
                    expected=next((types[t] for t in tags if t in types),None)
                    check(eid,aid,'cards.card_type',data['card_type'] if data else None,expected,'From directory filter')
                    variants=c.execute('''SELECT v.*,cv.description_zh,cv.cost_value,cv.cost_type FROM entity_variants v JOIN card_variants cv ON cv.variant_id=v.id WHERE v.entity_id=?''',(eid,)).fetchall()
                    for v in variants:
                        source=next((d['text'] for d in content['card_descriptions'] if d['variant']==v['variant_kind']),None)
                        check(eid,aid,f"variants.{v['variant_kind']}.description_zh",v['description_zh'],source)
                        check(eid,aid,f"variants.{v['variant_kind']}.cost",dict(cost_type=v['cost_type'],value=v['cost_value']),None,'Card cost is usually image-only; no image inference performed.')
                elif kind in ('relic','potion'):
                    data=c.execute(f"SELECT * FROM {'relics' if kind=='relic' else 'potions'} WHERE entity_id=?",(eid,)).fetchone()
                    if not data:continue
                    rarity={'初始':'Starter','普通':'Common','罕见':'Uncommon','稀有':'Rare','商店':'Shop','事件':'Event','特殊':'Special','BOSS':'Boss','Boss':'Boss'}.get(f.get('稀有度'))
                    check(eid,aid,f'{kind}.rarity',data['rarity'],rarity)
                    effect=json.loads(data['effect_json'] or '{}')
                    source=f.get('作用') or f.get('效果中文描述')
                    if kind=='potion' and content['tables']:
                        one=[r[0] for r in content['tables'][0]['rows'] if len(r)==1 and r[0]]
                        source=one[-1] if one and not re.match('^(稀有度|角色)',one[-1]) else None
                    check(eid,aid,f'{kind}.description_zh',effect.get('description_zh'),source)
                    if kind=='relic':check(eid,aid,'relic.flavor_zh',effect.get('flavor_zh'),f.get('说明') or f.get('中文引言'))
                    role=f.get('角色') or f.get('所属')
                    role_id={'铁甲战士':'sts1.character.ironclad','静默猎手':'sts1.character.silent','故障机器人':'sts1.character.defect','观者':'sts1.character.watcher'}.get(role)
                    if role in ('通用','所有','全角色'):role_id='all_characters'
                    check(eid,aid,f'{kind}.character',data['character_entity_id'] or 'all_characters',role_id)
                elif kind=='character':
                    data=c.execute('SELECT * FROM characters WHERE entity_id=?',(eid,)).fetchone()
                    for label,col in [('生命','initial_hp'),('金币','initial_gold')]:
                        value=int(f[label]) if f.get(label,'').isdigit() else None
                        check(eid,aid,'character.'+col,data[col],value)
                    deck=json.loads(data['starting_deck_json'] or '[]');translated={}
                    for item in deck:
                        name=c.execute("SELECT name FROM names WHERE entity_id=? AND language='zh-CN' ORDER BY is_preferred DESC LIMIT 1",(item.get('entity_id'),)).fetchone()
                        translated[name[0] if name else item['name']]=item['quantity']
                    source_deck={name:int(qty) for name,qty in re.findall(r'([\u4e00-\u9fff]+)\s*[×x]\s*(\d+)',f.get('初始牌组',''))}
                    check(eid,aid,'character.starting_deck',translated,source_deck or None)
                    relic=c.execute("SELECT name FROM names WHERE entity_id=? AND language='zh-CN' ORDER BY is_preferred DESC LIMIT 1",(data['starting_relic_entity_id'],)).fetchone()
                    check(eid,aid,'character.starting_relic',relic[0] if relic else None,f.get('初始遗物'))
                elif kind=='monster':
                    data=c.execute('SELECT * FROM monsters WHERE entity_id=?',(eid,)).fetchone()
                    # Only unambiguous single-monster infoboxes can be aligned.
                    hp=f.get('生命值') if len(active)==1 and e['subtype']!='group_page' else None
                    base=re.match(r'^(\d+)(?:\s*[-;~～–]\s*(\d+))?',hp or '')
                    expected=[int(base[1]),int(base[2] or base[1])] if base else None
                    check(eid,aid,'monster.hp_base',[data['hp_min'],data['hp_max']] if data else None,expected,
                          'Grouped pages require member-specific alignment; parentheses are ascension variants.')
                    check(eid,aid,'monster.moves_and_ascension',None,content['tables'],status='requires_semantic_review')
                elif kind=='status':
                    for lang,key in [('zh-CN','效果中文描述'),('en','效果英文描述')]:
                        claims=c.execute('''SELECT cl.value_json FROM claims cl JOIN source_pages p ON p.id=cl.source_page_id
                            WHERE cl.subject_entity_id=? AND cl.language=? AND cl.field_path='status.description'
                            AND COALESCE(cl.notes,'') NOT LIKE '%superseded:%'
                            ORDER BY CASE p.source_id WHEN 'game_local' THEN 0 WHEN 'wiki_gg' THEN 1 ELSE 2 END,cl.created_at DESC''',(eid,lang)).fetchall()
                        values=[json.loads(r[0]) for r in claims]
                        source=f.get(key)
                        check(eid,aid,'status.description.'+lang,values[0] if values else None,source)
                elif kind=='mechanic' and e['subtype']=='run_modifier':
                    data=json.loads(c.execute('SELECT definition_json FROM mechanics WHERE entity_id=?',(eid,)).fetchone()[0])
                    check(eid,aid,'modifier.description_zh',data.get('definition_zh'),f.get('效果'))
                    check(eid,aid,'modifier.name_en',c.execute("SELECT name FROM names WHERE entity_id=? AND language='en' ORDER BY is_preferred DESC LIMIT 1",(eid,)).fetchone()[0],f.get('英文名称'))
                else:
                    check(eid,aid,kind+'.source_sections',None,content['sections'],status='requires_semantic_review')
        # Member records inherit only the source-page pointer, never the
        # parent's HP or attacks. The source relationship stays explicit.
        for r in c.execute('''SELECT r.target_entity_id,x.article_id FROM relations r JOIN xiao_entity_pages x ON x.entity_id=r.source_entity_id
            WHERE r.relation_type='has_member' AND r.status='confirmed' ''').fetchall():
            c.execute("INSERT OR IGNORE INTO xiao_entity_pages VALUES(?,?,'member_of_group')",(r[0],r[1]))
            check(r[0],r[1],'monster.member_source',None,None,status='member_specific_review_required',note='Source is a grouped monster page; page coverage is not numerical verification.')
        # No silently skipped entity, including candidates and deprecated IDs.
        for e in c.execute('SELECT * FROM entities ORDER BY id'):
            if not c.execute('SELECT 1 FROM xiao_entity_pages WHERE entity_id=?',(e['id'],)).fetchone():
                check(e['id'],None,'source.coverage',e['lifecycle'],None,status='no_direct_xiao_article',note='May be a member of a grouped page, game-only entry or English-only topic; see relationships.')
        c.executemany('INSERT INTO xiao_field_checks VALUES(:id,:entity_id,:article_id,:field_path,:current_json,:source_json,:status,:note)',checks)
    report=dict(directory_articles=c.execute('SELECT count(*) FROM xiao_page_review').fetchone()[0],
                directory_memberships=c.execute('SELECT count(*) FROM xiao_directory').fetchone()[0],
                article_status=dict(c.execute('SELECT status,count(*) FROM xiao_page_review GROUP BY status').fetchall()),
                field_status=dict(Counter(r['status'] for r in checks)),
                scope=[dict(r) for r in c.execute('SELECT scope,count(DISTINCT article_id) articles FROM xiao_directory GROUP BY scope')],
                by_kind=[dict(r) for r in c.execute('''SELECT e.kind,e.lifecycle,count(*) total,
                 sum(EXISTS(SELECT 1 FROM xiao_entity_pages x WHERE x.entity_id=e.id)) with_page FROM entities e GROUP BY e.kind,e.lifecycle''')])
    (ROOT/'reports/xiaoheihe-full-review.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    with (ROOT/'reports/xiaoheihe-field-checks.jsonl').open('w',encoding='utf-8') as file:
        for check_row in checks:
            row=dict(check_row)
            row['current']=json.loads(row.pop('current_json'));row['source']=json.loads(row.pop('source_json'))
            file.write(json.dumps(row,ensure_ascii=False)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    c.close()


if __name__=='__main__':main()
