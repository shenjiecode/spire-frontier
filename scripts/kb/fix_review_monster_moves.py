"""Remove group-page move contamination, retaining every old row in audit log."""
import hashlib,json,sqlite3
from bootstrap_sample import ROOT,DB_PATH

def main():
    c=sqlite3.connect(DB_PATH);c.row_factory=sqlite3.Row
    c.execute('PRAGMA foreign_keys=ON')
    def log(row,new,reason):
        old=dict(row);eid=old['monster_entity_id']
        pid=c.execute("SELECT source_page_id FROM claims WHERE subject_entity_id=? AND field_path='source.wikitext' LIMIT 1",(eid,)).fetchone()
        key=hashlib.sha256(json.dumps([old,new],sort_keys=True).encode()).hexdigest()[:24]
        c.execute('INSERT OR IGNORE INTO xiao_corrections VALUES(?,?,?,?,?,?,?)',('xcorr.'+key,eid,'monster_moves.'+old['id'],json.dumps(old,ensure_ascii=False),json.dumps(new,ensure_ascii=False),pid[0] if pid else None,reason))
    def remove(row,reason):
        log(row,None,reason);c.execute('DELETE FROM monster_moves WHERE id=?',(row['id'],))
    with c:
        for parent,child,names in [
            ('bronze_automaton','bronzeorb',['Stasis','Support Beam','Beam']),
            ('reptomancer','dagger',['Wound','Explode']),
            ('the_collector','torchhead',['Tackle'])]:
            for name in names:
                childrow=c.execute('SELECT * FROM monster_moves WHERE monster_entity_id=? AND name=?',('sts1.game.candidate.monster.'+child,name)).fetchone()
                assert childrow is not None,(child,name)
                for row in c.execute('SELECT * FROM monster_moves WHERE monster_entity_id=? AND name=?',('sts1.monster.'+parent,name)).fetchall():
                    assert row['damage']==childrow['damage']
                    remove(row,'Shared article included summoned creature moves; move retained on '+childrow['monster_entity_id'])
        for monster,damage,block in [('looter',16,'(11;17)'),('mugger',12,'6 Block')]:
            for row in c.execute('SELECT * FROM monster_moves WHERE monster_entity_id=?',('sts1.monster.'+monster,)).fetchall():
                if (row['name']=='Lunge' and row['damage']==damage) or (row['name']=='Smoke Bomb' and block in row['effect_json']):
                    remove(row,'Looter/Mugger shared source table: remove the other member\'s move.')
        for en,zh in [('Goop Spray','黏液喷射'),('Preparing','准备'),('Slam','史莱姆撞击'),('Split','分裂')]:
            rows=c.execute("SELECT * FROM monster_moves WHERE monster_entity_id='sts1.monster.slime_boss' AND name IN (?,?)",(en,zh)).fetchall()
            if len(rows)!=2:continue
            a=next(r for r in rows if r['name']==en);b=next(r for r in rows if r['name']==zh)
            effect=json.loads(a['effect_json'] or '{}');effect.update(json.loads(b['effect_json'] or '{}'));effect['name_zh']=zh
            new=dict(a);new.update(effect_json=json.dumps(effect,ensure_ascii=False),hits=a['hits'] or b['hits'],order_rules=a['order_rules'] or b['order_rules'])
            log(a,new,'Merge bilingual duplicate move while preserving structured effects and order rules.')
            c.execute('UPDATE monster_moves SET effect_json=?,hits=?,order_rules=? WHERE id=?',(new['effect_json'],new['hits'],new['order_rules'],a['id']))
            remove(b,'Bilingual duplicate merged into '+a['id'])
        for monster,name in [('hexaghost','Divider'),('darkling','Nip'),('transient','Attack')]:
            row=c.execute('SELECT * FROM monster_moves WHERE monster_entity_id=? AND name=?',('sts1.monster.'+monster,name)).fetchone()
            if row and row['damage'] is not None:
                new=dict(row);new['damage']=None
                log(row,new,'Damage is a formula or range in effect_json, not a fixed scalar.')
                c.execute('UPDATE monster_moves SET damage=NULL WHERE id=?',(row['id'],))
    c.close()

if __name__=='__main__':main()
