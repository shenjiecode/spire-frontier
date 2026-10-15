"""Apply bounded, traceable corrections found by the full Xiaoheihe review."""
import hashlib
import json
import re
import sqlite3
from collections import Counter

from bootstrap_sample import ROOT, DB_PATH, add_claim, add_name, add_resolution
from review_xiao import clean, norm, fields
from supplement_editorial_zh import STATUS_FIXES, _status_claim, _game_source_page, _source_page


def main():
    c=sqlite3.connect(DB_PATH);c.row_factory=sqlite3.Row
    c.execute('PRAGMA foreign_keys=ON')
    c.executescript((ROOT/'schemas/003_xiao_review.sql').read_text(encoding='utf-8'))
    stats=Counter()
    def log(e,path,old,new,pid,reason):
        if old==new:return
        key=hashlib.sha256(json.dumps([e,path,old,new],ensure_ascii=False).encode()).hexdigest()[:24]
        c.execute('INSERT OR IGNORE INTO xiao_corrections VALUES(?,?,?,?,?,?,?)',
                  ('xcorr.'+key,e,path,json.dumps(old,ensure_ascii=False),json.dumps(new,ensure_ascii=False),pid,reason))
        stats[path]+=1
    with c:
        # Negative Dexterity is a state of Dexterity, not the delayed DexLoss
        # debuff. The prior mapping mixed those two Chinese article titles.
        aid='15454365';old='sts1.status.dexterity_down';new='sts1.status.dexterity_negative'
        page=c.execute('SELECT * FROM xiao_page_review WHERE article_id=?',(aid,)).fetchone()
        if page and page['content_json']:
            content=json.loads(page['content_json']);pid=page['source_page_id']
            assert 'Block from cards is reduced' in content['text']
            rows=c.execute('''SELECT cl.* FROM claims cl JOIN source_pages p ON p.id=cl.source_page_id
                WHERE cl.subject_entity_id=? AND p.source_id='xiaoheihe' AND p.article_id=?''',(old,aid)).fetchall()
            for r in rows:
                if r['field_path'] in ('source.article_text','source.title_text','status.description'):
                    c.execute("UPDATE claims SET notes=COALESCE(notes,'') || '; superseded: negative Dexterity article belongs to dexterity_negative' WHERE id=? AND COALESCE(notes,'') NOT LIKE '%superseded: negative Dexterity%'",(r['id'],))
            add_claim(c,new,'source.article_text',content['text'],pid,language='zh-CN',notes='Reviewed negative Dexterity article; not delayed DexLoss.')
            f=fields(content)
            for lang,label in [('en','效果英文描述'),('zh-CN','效果中文描述')]:
                if f.get(label):add_claim(c,new,'status.description',f[label],pid,language=lang,extraction_method='structured_html',locator='table/'+label)
            c.execute("DELETE FROM names WHERE entity_id=? AND language='zh-CN' AND name IN ('敏捷(负)','敏捷（负）')",(old,))
            add_name(c,new,'zh-CN','敏捷（负）',source_page_id=pid,name_kind='alias',status='single_source')
            c.execute("UPDATE names SET is_preferred=CASE WHEN name='敏捷下降' THEN 1 ELSE 0 END WHERE entity_id=? AND language='zh-CN'",(old,))
            for r in c.execute('''SELECT m.* FROM inventory_mappings m JOIN inventory_items i ON i.id=m.zh_inventory_id WHERE i.article_id=?''',(aid,)).fetchall():
                evidence=json.loads(r['evidence_json'] or '{}');evidence['entity_id']=new
                evidence['review_note']='Negative Dexterity, not the end-of-turn DexLoss status; reviewed against article effect.'
                c.execute('UPDATE inventory_mappings SET evidence_json=?,rationale=? WHERE id=?',(json.dumps(evidence,ensure_ascii=False),evidence['review_note'],r['id']))
            log(new,'identity.xiao_article',old,new,pid,'Chinese and English effect explicitly reduces card Block rather than losing Dexterity at end of turn.')

        # Fix repeatability of the existing explicit status-variant decisions.
        for eid,fix in STATUS_FIXES.items():
            pid=_game_source_page(c,eid) or _source_page(c,eid,'source.wikitext') or _source_page(c,eid,'status.description')
            for lang,key in [('en','description_en'),('zh-CN','description_zh')]:
                _status_claim(c,eid,fix[key],lang,pid)

        rows=c.execute('''SELECT x.*,p.source_page_id FROM xiao_field_checks x JOIN xiao_page_review p USING(article_id)
            JOIN entities e ON e.id=x.entity_id WHERE e.lifecycle='active' ''').fetchall()
        for row in rows:
            eid=row['entity_id'];path=row['field_path'];pid=row['source_page_id']
            old=json.loads(row['current_json']);source=json.loads(row['source_json'])
            if not isinstance(source,str) or not source:continue
            if path.startswith('variants.') and path.endswith('.description_zh') and isinstance(old,str):
                # Only remove provable parser duplication, not real repeated effects.
                explicit_boundary_fix=eid in ('sts1.card.colorless.live_forever','sts1.card.watcher.study') and norm(old)!=norm(source)
                if norm(old)!=norm(source)*2 and not explicit_boundary_fix:continue
                variant=path.split('.')[1]
                v=c.execute('SELECT id FROM entity_variants WHERE entity_id=? AND variant_kind=?',(eid,variant)).fetchone()
                if not v:continue
                c.execute('UPDATE card_variants SET description_zh=? WHERE variant_id=?',(source,v[0]))
                claim=add_claim(c,eid,'card.description',source,pid,variant_id=v[0],language='zh-CN',extraction_method='structured_html',notes='Full review: removed duplicated DOM extraction.')
                add_resolution(c,eid,'card.description.zh',claim,source,variant_id=v[0],status='adopted',rationale='Exact single source caption replaces duplicated extraction.')
                log(eid,path,old,source,pid,'Source caption appeared twice in the prior projection.')
            elif path in ('relic.description_zh','potion.description_zh'):
                kind=path.split('.')[0];table='relics' if kind=='relic' else 'potions'
                current=c.execute(f'SELECT effect_json FROM {table} WHERE entity_id=?',(eid,)).fetchone()
                effect=json.loads(current[0] or '{}')
                # Preserve clean, more detailed game descriptions. Replace
                # display templates/UI fragments and article-table pollution.
                contaminated=bool(re.search(r'#[rgbypw]|\[[ERGBP]\]|稀有度|选择\d张牌|这件遗物|已经耗尽|潘多拉的魔盒已经',old or ''))
                if not contaminated:continue
                chosen=source;reason='Adopt explicit Xiaoheihe effect cell instead of unresolved localization fragments or whole-table text.'
                if eid=='sts1.relic.toolbox':
                    chosen='每场战斗开始时，从3张随机无色牌中选择1张加入手牌。'
                    reason='Xiaoheihe has outdated random-card effect; current English description explicitly says choose 1 of 3. Chinese editorial rendering, not Xiaoheihe transcription.'
                elif eid=='sts1.relic.art_of_war':
                    chosen='如果你在回合中不打出任何攻击牌，在下一回合得到1点额外能量。'
                    reason='Correct duplicated quantity wording in Xiaoheihe using game and English effect.'
                elif eid=='sts1.relic.brimstone':chosen=source.replace('>','')
                elif eid=='sts1.relic.mutagenic_strength':
                    chosen='每场战斗开始时获得3点力量，在你的第一个回合结束时失去3点力量。'
                    reason='Fill numeric template from source while preserving the game first-turn condition omitted in Xiaoheihe.'
                if effect.get('description_zh')==chosen:continue
                claim=add_claim(c,eid,kind+'.effect',chosen,pid,language='zh-CN',extraction_method='manual',locator='table/effect',notes=reason)
                add_resolution(c,eid,kind+'.description.zh',claim,chosen,status='adopted',rationale=reason)
                effect['description_zh']=chosen
                effect['description_zh_origin']='reviewed_editorial' if chosen!=source else 'xiaoheihe_effect_cell'
                effect['description_zh_source_page_id']=pid
                c.execute(f'UPDATE {table} SET effect_json=? WHERE entity_id=?',(json.dumps(effect,ensure_ascii=False,sort_keys=True),eid))
                log(eid,path,old,chosen,pid,reason)

        # English list extraction also appended flavor text without a space.
        for r in c.execute('SELECT * FROM relics').fetchall():
            effect=json.loads(r['effect_json'] or '{}');old=effect.get('description_en','');flavor=effect.get('flavor_en',effect.get('flavor',''))
            if flavor and old.endswith(flavor):
                new=old[:-len(flavor)].strip()
                if not new:continue
                effect['description_en']=new
                pid=c.execute("SELECT source_page_id FROM claims WHERE subject_entity_id=? AND language='en' AND field_path='relic.effect' LIMIT 1",(r['entity_id'],)).fetchone()
                log(r['entity_id'],'relic.description_en',old,new,pid[0] if pid else None,'Separate exact trailing flavor text from the rule description.')
                c.execute('UPDATE relics SET effect_json=? WHERE entity_id=?',(json.dumps(effect,ensure_ascii=False,sort_keys=True),r['entity_id']))

        explicit_effects={
            'sts1.relic.regal_pillow':('在休息时额外回复15点生命。','Xiaoheihe relic page says 25, but its Rest Site page and English Wiki both say 15.'),
            'sts1.relic.the_boot':('每当你造成小于等于4点未被格挡的攻击伤害时，将伤害提升为5。','English rule explicitly uses 4 or less; preserve exact threshold rather than Xiaoheihe 5.'),
            'sts1.relic.warped_tongs':('在你的每个回合开始时，随机升级一张你的手牌（只影响本场战斗）。','Preserve the combat-only duration explicitly present in game and English source.'),
            'sts1.relic.cultist_headpiece':('你觉得自己有开腔的欲望。','Separate effect from triggered dialogue fragments.'),
            'sts1.potion.duplication_potion':('本回合你的下一张牌将被打出两次。','Separate base description from Sacred Bark enhancement; original fragments remain in claims.'),
            'sts1.potion.smoke_bomb':('从一场非Boss战斗中逃离，不获得任何奖励。','Separate effect from the surrounded failure message; restriction is retained separately.'),
        }
        for eid,(chosen,reason) in explicit_effects.items():
            table='potions' if '.potion.' in eid else 'relics';kind='potion' if table=='potions' else 'relic'
            row=c.execute(f'SELECT effect_json FROM {table} WHERE entity_id=?',(eid,)).fetchone()
            if not row:continue
            effect=json.loads(row[0] or '{}');old=effect.get('description_zh')
            p=c.execute('SELECT p.source_page_id FROM xiao_entity_pages x JOIN xiao_page_review p USING(article_id) WHERE x.entity_id=?',(eid,)).fetchone();pid=p[0] if p else None
            if eid=='sts1.relic.regal_pillow':
                pid=c.execute("SELECT source_page_id FROM xiao_page_review WHERE article_id='15463366'").fetchone()[0]
            elif eid in ('sts1.relic.the_boot','sts1.relic.warped_tongs'):
                independent=c.execute("SELECT cl.source_page_id FROM claims cl JOIN source_pages p ON p.id=cl.source_page_id WHERE cl.subject_entity_id=? AND p.source_id='wiki_gg' AND cl.language='en' LIMIT 1",(eid,)).fetchone()
                if independent:pid=independent[0]
            if eid=='sts1.potion.smoke_bomb':effect['restrictions_zh']=['Boss战不可使用','被夹击时不可逃脱']
            effect['description_zh']=chosen;effect['description_zh_origin']='reviewed_editorial';effect['description_zh_source_page_id']=pid
            c.execute(f'UPDATE {table} SET effect_json=? WHERE entity_id=?',(json.dumps(effect,ensure_ascii=False,sort_keys=True),eid))
            if eid=='sts1.potion.duplication_potion':
                enhancement=c.execute('SELECT enhancement_json FROM potions WHERE entity_id=?',(eid,)).fetchone()[0]
                enhanced=json.loads(enhancement or '{}');enhanced['sacred_bark_description_zh']='本回合你的下两张牌将被打出两次。'
                c.execute('UPDATE potions SET enhancement_json=? WHERE entity_id=?',(json.dumps(enhanced,ensure_ascii=False),eid))
            if pid:
                claim=add_claim(c,eid,kind+'.effect',chosen,pid,language='zh-CN',notes=reason)
                add_resolution(c,eid,kind+'.description.zh',claim,chosen,status='adopted',rationale=reason)
            log(eid,kind+'.description_zh',old,chosen,pid,reason)

        # Plated Armor is lost from unblocked ATTACK damage, not all HP loss.
        plate=c.execute("SELECT p.* FROM xiao_entity_pages x JOIN xiao_page_review p USING(article_id) WHERE x.entity_id='sts1.status.plated_armor'").fetchone()
        if plate:
            f=fields(json.loads(plate['content_json']))
            for lang,label in [('en','效果英文描述'),('zh-CN','效果中文描述')]:
                if f.get(label):_status_claim(c,'sts1.status.plated_armor',f[label],lang,plate['source_page_id'])

        # Previously omitted modifier records: only exact bilingual game
        # identity matches get a game ID. Source-only entries stay provisional.
        local=ROOT/'data/raw/game_local/cfad868ac8d65a88'
        en=json.loads((local/'eng/run_mods.json').read_text(encoding='utf-8-sig'))
        zh=json.loads((local/'zhs/run_mods.json').read_text(encoding='utf-8-sig'))
        game_pages={}
        for lang in ('eng','zhs'):
            p=local/lang/'run_mods.json';digest=hashlib.sha256(p.read_bytes()).hexdigest();pid='game.run_mods.'+lang+'.'+digest[:16]
            c.execute('''INSERT OR IGNORE INTO source_pages(id,source_id,url,title,fetched_at,http_status,content_type,snapshot_path,sha256,parser_version,is_index_page,notes)
                VALUES(?,'game_local',?,?,'2026-09-18T00:00:00Z',200,'application/json',?,?,'xiao-review/1',0,?)''',
                (pid,'game-local://cfad868ac8d65a88/localization/'+lang+'/run_mods.json','Game run modifiers '+lang,p.relative_to(ROOT).as_posix(),digest,'Extracted from installed JAR recorded in jar-metadata.json.'))
            game_pages[lang]=pid
        for page in c.execute('''SELECT DISTINCT p.* FROM xiao_page_review p JOIN xiao_directory d USING(article_id)
            WHERE d.scope='daily_modifier' AND p.content_json IS NOT NULL''').fetchall():
            content=json.loads(page['content_json']);f=fields(content)
            if not f.get('名称') or not f.get('效果'):continue # related pages, not modifiers
            eid='sts1.mechanic.modifier.'+page['article_id']
            matches=[key for key,item in en.items() if '[DEPRECATED]' not in item['NAME'] and
                (norm(item['NAME'])==norm(f.get('英文名称')) or norm(zh.get(key,{}).get('NAME'))==norm(f['名称']))]
            key=matches[0] if len(matches)==1 else None
            exists=c.execute('SELECT 1 FROM entities WHERE id=?',(eid,)).fetchone()
            c.execute('''INSERT OR IGNORE INTO entities(id,kind,subtype,game_id,lifecycle,mapping_status,notes)
                VALUES(?,'mechanic','run_modifier',?,'active',?,?)''',(eid,key,'confirmed' if key else 'provisional','Xiaoheihe run modifier; identity checked against installed run_mods localization where available.'))
            add_name(c,eid,'zh-CN',zh[key]['NAME'] if key else f['名称'],source_page_id=game_pages['zhs'] if key else page['source_page_id'],preferred=True,status='single_source')
            if key or not re.search('[\u4e00-\u9fff]',f.get('英文名称','')):
                add_name(c,eid,'en',en[key]['NAME'] if key else f['英文名称'],source_page_id=game_pages['eng'] if key else page['source_page_id'],preferred=True,status='single_source')
            data=dict(definition_zh=zh[key]['DESCRIPTION'] if key else f['效果'],definition_en=en[key]['DESCRIPTION'] if key else None,
                      source_description_zh=f['效果'],source_notes_zh=f.get('备注'),origin='game_localization' if key else 'xiaoheihe',source_page_id=page['source_page_id'])
            c.execute('INSERT OR REPLACE INTO mechanics(entity_id,definition_json) VALUES(?,?)',(eid,json.dumps(data,ensure_ascii=False)))
            add_claim(c,eid,'source.article_text',content['text'],page['source_page_id'],language='zh-CN',extraction_method='visible_text')
            if key:
                for lang in ('eng','zhs'):
                    add_claim(c,eid,'game.run_modifier',dict(game_id=key,**(en if lang=='eng' else zh)[key]),game_pages[lang],language='en' if lang=='eng' else 'zh-CN',extraction_method='manual',status='verified_game')
            if not exists:log(eid,'new.run_modifier',None,data,page['source_page_id'],'Previously omitted daily/custom modifier section.')
    report=dict(changes_this_run=dict(stats),total_logged=c.execute('SELECT count(*) FROM xiao_corrections').fetchone()[0])
    (ROOT/'reports/xiaoheihe-corrections.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2));c.close()


if __name__=='__main__':main()
