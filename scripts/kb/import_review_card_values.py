"""Promote only direct JVM literals; keep dynamic/conditional effects unknown.

This is a static base/upgrade projection, not a combat simulator. Every
promoted value points to a class hash and bytecode offset in saved evidence.
"""
import hashlib,json,re,sqlite3
from collections import Counter
from bootstrap_sample import ROOT,DB_PATH,add_claim,add_resolution,utc_now


def direct_literal(previous,current):
    if previous is None or previous[1] not in ('int','ldc') or not isinstance(previous[2],int):return None
    # iconst=1 byte, bipush=2, sipush=3, ldc=2/3. Exact byte adjacency
    # excludes values subsequently altered by arithmetic/stack operations.
    expected=1 if -1<=previous[2]<=5 else 2 if -128<=previous[2]<=127 else 3
    if previous[1]=='ldc':return None # avoid uncertain ldc_w width
    return previous[2] if current[0]-previous[0]==expected else None


def literals(evidence):
    constructor=evidence['methods'].get('<init>()V',[])
    result={};locations={}
    keys={'baseDamage':'damage','baseBlock':'block','baseMagicNumber':'magic_number'}
    for i,ins in enumerate(constructor):
        if ins[1]=='0xb5':
            name=ins[2].split(':')[-2]
            if name in keys:
                value=direct_literal(constructor[i-1] if i else None,ins)
                if value is not None:result[keys[name]]=value;locations[keys[name]]=ins[0]
    upgrade=dict(result);dynamic=[]
    method=evidence['methods'].get('upgrade()V',[])
    for field,call in [('damage','upgradeDamage'),('block','upgradeBlock'),('magic_number','upgradeMagicNumber')]:
        calls=[(i,x) for i,x in enumerate(method) if x[1]=='0xb6' and ':'+call+':' in x[2]]
        if calls:
            value=direct_literal(method[calls[0][0]-1] if calls[0][0] else None,calls[0][1]) if len(calls)==1 else None
            if value is not None and field in result:upgrade[field]=result[field]+value
            else:upgrade.pop(field,None);dynamic.append(field)
    target=next((x[2].split(':')[-2] for x in constructor if x[1]=='0xb2' and 'AbstractCard$CardTarget:' in x[2]),None)
    return result,upgrade,locations,dynamic,target


def render(template,values,language='zh-CN'):
    if not template:return None
    for token,key in [('!D!','damage'),('!B!','block'),('!M!','magic_number')]:
        if token in template:
            if key not in values:return None
            template=template.replace(token,str(values[key]))
    if re.search(r'![A-Za-z]+!',template):return None
    template=re.sub(r'\bNL\b',' ',template)
    template=re.sub(r'#[rgbypw]','',template)
    template=re.sub(r'\*(?=[\u4e00-\u9fffA-Za-z])','',template)
    unit='点能量' if language=='zh-CN' else ' Energy'
    # An icon after a variable or in an equality denotes the energy unit,
    # not an extra literal 1. Recycle and Doppelganger use these templates.
    template=re.sub(r'(X(?:\s*\+\s*\d+)?)\s*\[[RGBPEW]\]',lambda m:m[1]+unit,template)
    template=re.sub(r'相等的\s*\[[RGBPEW]\]','相等的能量',template)
    template=re.sub(r'\[[RGBPEW]\](?=\s+equal to)','Energy',template)
    if language=='zh-CN':
        template=re.sub(r'([一二两三四五六七八九十])点\s*(?=\[[RGBPEW]\])',lambda m:str({'一':1,'二':2,'两':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9,'十':10}[m[1]]),template)
    template=re.sub(r'(\d+)\s*\[[RGBPEW]\]',lambda m:m[1]+unit,template)
    template=re.sub(r'(?:\[[RGBPEW]\]\s*)+',lambda m:str(len(re.findall(r'\[',m[0])))+unit,template)
    template=' '.join(template.split())
    return re.sub(r'(?<=[\u4e00-\u9fff0-9。，])\s+(?=[\u4e00-\u9fff0-9。，])','',template)


def main():
    root=ROOT/'data/raw/game_local/cfad868ac8d65a88'
    p=root/'review-class-evidence.json';evidence=json.loads(p.read_text(encoding='utf-8'))
    zh=json.loads((root/'zhs/cards.json').read_text(encoding='utf-8-sig'))
    en=json.loads((root/'eng/cards.json').read_text(encoding='utf-8-sig'))
    by_id={}
    for name,item in evidence.items():
        if '/cards/' not in name or '/deprecated/' in name:continue
        game_id=item['constant_fields'].get('ID')
        if game_id:by_id.setdefault(game_id,[]).append((name,item))
    c=sqlite3.connect(DB_PATH);c.row_factory=sqlite3.Row;c.execute('PRAGMA foreign_keys=ON')
    digest=hashlib.sha256(p.read_bytes()).hexdigest();pid='game.review.classes.'+digest[:16]
    stats=Counter();unknown=[]
    with c:
        c.execute('''INSERT OR IGNORE INTO source_pages(id,source_id,url,title,fetched_at,http_status,content_type,snapshot_path,sha256,parser_version,is_index_page,notes)
         VALUES(?,'game_local',?,'Installed game constructor/upgrade bytecode',?,200,'application/json',?,?,'card-values/1',0,?)''',
         (pid,'game-local://cfad868ac8d65a88/review-class-evidence/'+digest,utc_now(),p.relative_to(ROOT).as_posix(),digest,'Static instruction evidence extracted from JAR recorded in jar-metadata.json; no runtime simulation.'))
        for entity in c.execute("SELECT * FROM entities WHERE kind='card' AND lifecycle='active'").fetchall():
            candidates=by_id.get(entity['game_id'],[])
            if len(candidates)!=1:
                unknown.append(dict(entity_id=entity['id'],reason='no unique game class'));continue
            name,item=candidates[0];base,upgraded,locations,dynamic,target=literals(item)
            if target:
                old=c.execute('SELECT target FROM cards WHERE entity_id=?',(entity['id'],)).fetchone()[0]
                if old!=target:
                    c.execute('UPDATE cards SET target=? WHERE entity_id=?',(target,entity['id']));stats['targets_updated']+=1
                add_claim(c,entity['id'],'card.target',target,pid,locator=name+'/<init>/CardTarget',status='verified_game')
            for v in c.execute('''SELECT v.*,cv.description_zh,cv.parsed_json FROM entity_variants v JOIN card_variants cv ON cv.variant_id=v.id WHERE v.entity_id=?''',(entity['id'],)).fetchall():
                if v['variant_kind'] not in ('base','upgrade'):continue
                vals=base if v['variant_kind']=='base' else upgraded
                data=json.loads(v['parsed_json'] or '{}')
                data['game_values']=dict(values=vals,source_page_id=pid,class_name=name,class_sha256=item['sha256'],
                    constructor_offsets=locations,dynamic_upgrade_fields=dynamic if v['variant_kind']=='upgrade' else [],scope='unmodified static base values; conditions/multipliers are in descriptions')
                c.execute('UPDATE card_variants SET parsed_json=? WHERE variant_id=?',(json.dumps(data,ensure_ascii=False,sort_keys=True),v['id']))
                add_claim(c,entity['id'],'card.game_values',data['game_values'],pid,variant_id=v['id'],status='verified_game',locator=name+'/'+v['variant_kind'])
                stats['variants_with_literal_values']+=bool(vals)
                localized=zh.get(entity['game_id'],{})
                method=item['methods'].get('upgrade()V',[])
                upgraded_description=any('UPGRADE_DESCRIPTION:' in str(x[2]) for x in method)
                template=localized.get('UPGRADE_DESCRIPTION') if v['variant_kind']=='upgrade' and upgraded_description else localized.get('DESCRIPTION')
                # A custom upgrade builds a description at runtime; leave it
                # for manual review instead of silently using the base text.
                if v['variant_kind']=='upgrade' and not upgraded_description and any(':rawDescription:' in str(x[2]) and x[1]=='0xb5' for x in method):
                    unknown.append(dict(entity_id=entity['id'],variant=v['variant_kind'],reason='custom upgrade description'));continue
                new=render(template,vals)
                if new is None:
                    unknown.append(dict(entity_id=entity['id'],variant=v['variant_kind'],reason='dynamic or unsupported placeholder'));continue
                stats['variants_renderable']+=1
                if new!=v['description_zh']:
                    c.execute('UPDATE card_variants SET description_zh=? WHERE variant_id=?',(new,v['id']))
                    key='xcorr.'+hashlib.sha256(json.dumps([v['id'],v['description_zh'],new],ensure_ascii=False).encode()).hexdigest()[:24]
                    c.execute('INSERT OR IGNORE INTO xiao_corrections VALUES(?,?,?,?,?,?,?)',(key,entity['id'],'variants.'+v['variant_kind']+'.description_zh',json.dumps(v['description_zh'],ensure_ascii=False),json.dumps(new,ensure_ascii=False),pid,'Render official localized template with directly observed JVM literals; see class and localization evidence.'))
                    stats['descriptions_rendered']+=1
                claim=add_claim(c,entity['id'],'card.description',new,pid,variant_id=v['id'],language='zh-CN',status='verified_game',locator=name+'/'+v['variant_kind'],notes='Derived from local cards.json template and direct bytecode literals; not a Wiki transcription.')
                add_resolution(c,entity['id'],'card.description.zh',claim,new,variant_id=v['id'],status='adopted',rationale='Official localization rendered with inspected static game values.')
                en_local=en.get(entity['game_id'],{})
                en_template=en_local.get('UPGRADE_DESCRIPTION') if v['variant_kind']=='upgrade' and upgraded_description else en_local.get('DESCRIPTION')
                new_en=render(en_template,vals,'en')
                if new_en:
                    old_en=c.execute('SELECT description_en FROM card_variants WHERE variant_id=?',(v['id'],)).fetchone()[0]
                    if old_en!=new_en:
                        c.execute('UPDATE card_variants SET description_en=? WHERE variant_id=?',(new_en,v['id']))
                        key='xcorr.'+hashlib.sha256(json.dumps([v['id'],old_en,new_en],ensure_ascii=False).encode()).hexdigest()[:24]
                        c.execute('INSERT OR IGNORE INTO xiao_corrections VALUES(?,?,?,?,?,?,?)',(key,entity['id'],'variants.'+v['variant_kind']+'.description_en',json.dumps(old_en),json.dumps(new_en),pid,'Render official English template with direct JVM literals.'))
                        stats['english_descriptions_rendered']+=1
                    claim=add_claim(c,entity['id'],'card.description',new_en,pid,variant_id=v['id'],language='en',status='verified_game',locator=name+'/'+v['variant_kind'],notes='Derived from local English template and direct bytecode literals.')
                    add_resolution(c,entity['id'],'card.description.en',claim,new_en,variant_id=v['id'],status='adopted',rationale='Official localization rendered with inspected static game values.')
    report=dict(counts=dict(stats),unresolved=unknown)
    (ROOT/'reports/game-card-values-review.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2));c.close()


if __name__=='__main__':main()
