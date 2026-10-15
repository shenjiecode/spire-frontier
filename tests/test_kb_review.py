import json,sqlite3,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts/kb'))
from import_review_card_values import direct_literal,literals,render
from review_xiao import parse_page
from review_semantics import notation,pair_key,decision_for

class ReviewTests(unittest.TestCase):
    def test_only_adjacent_literals(self):
        self.assertEqual(direct_literal([4,'int',8],[6,'0xb5','field']),8)
        self.assertIsNone(direct_literal([4,'int',8],[7,'0xb5','field']))
        self.assertIsNone(direct_literal([4,'ldc',8],[6,'0xb5','field']))

    def test_upgrade_arithmetic_remains_unknown(self):
        evidence={'methods':{'<init>()V':[[0,'int',6],[2,'0xb5','Card:baseDamage:I']],
                             'upgrade()V':[[0,'int',3],[1,'0xb6','Card:upgradeDamage:(I)V']]}}
        base,up,*_=literals(evidence)
        self.assertEqual(base['damage'],6);self.assertEqual(up['damage'],9)
        evidence['methods']['upgrade()V'][1][0]=5
        self.assertNotIn('damage',literals(evidence)[1])

    def test_localization_icons_and_unknowns(self):
        self.assertEqual(render('Gain [W].',{},'en'),'Gain 1 Energy.')
        self.assertEqual(render('Gain 2 [R].',{},'en'),'Gain 2 Energy.')
        self.assertEqual(render('获得 [R] [R] 。',{}),'获得2点能量。')
        self.assertEqual(render('获得一点 [R] 。',{}),'获得1点能量。')
        self.assertIsNone(render('Gain !B! Block.',{}))
        self.assertEqual(render('获得X [G] 。',{}),'获得X点能量。')
        self.assertEqual(render('获得与其耗能相等的 [B] 。',{}),'获得与其耗能相等的能量。')
        self.assertEqual(render('Gain [B] equal to its cost.',{},'en'),'Gain Energy equal to its cost.')
        self.assertEqual(render('gain X+1 [G].',{},'en'),'gain X+1 Energy.')

    def test_quantity_notation_preserves_rules(self):
        self.assertEqual(notation('造成7点伤害。生成1个闪电充能球。'),notation('造成7点伤害。生成一个闪电充能球。'))
        self.assertEqual(notation('抽十二张牌'),notation('抽12张牌'))
        self.assertEqual(notation('造成二十五点伤害'),notation('造成25点伤害'))
        self.assertNotEqual(notation('获得两点能量'),notation('获得3点能量'))
        self.assertNotEqual(notation('可以打出'),notation('不可以打出'))
        self.assertNotEqual(notation('本回合'),notation('本场战斗'))
        self.assertNotEqual(notation('伤害+1'),notation('伤害-1'))
        self.assertEqual(notation('两者择一'), '两者择一')

    def test_semantic_decision_invalidates_when_either_value_changes(self):
        key=pair_key('e','a','f','current','source')
        decisions={key:{'status':'equivalent_wording'}}
        self.assertIsNotNone(decision_for(decisions,'e','a','f','current','source'))
        self.assertIsNone(decision_for(decisions,'e','a','f','changed','source'))
        self.assertIsNone(decision_for(decisions,'e','a','f','current','changed'))

    def test_card_boundaries_and_noncard(self):
        raw='<div class="article-content"><h1>彩虹</h1><img/><p>基础效果</p><h1>彩虹+</h1><img/><p>升级效果</p><h1>测试画风</h1><p>不提取</p></div>'.encode()
        self.assertEqual(parse_page(raw,'彩虹')['card_descriptions'],[{'variant':'base','text':'基础效果'},{'variant':'upgrade','text':'升级效果'}])
        self.assertEqual(parse_page(raw)['card_descriptions'],[])

    def test_database_corrected_projections(self):
        c=sqlite3.connect(ROOT/'data/spire.sqlite')
        self.assertFalse(c.execute('PRAGMA foreign_key_check').fetchall())
        self.assertEqual(c.execute("SELECT count(*) FROM monster_moves WHERE monster_entity_id='sts1.monster.slime_boss'").fetchone()[0],4)
        self.assertEqual(c.execute("SELECT count(*) FROM monster_moves WHERE monster_entity_id='sts1.monster.bronze_automaton' AND name='Stasis'").fetchone()[0],0)
        for monster,name in [('hexaghost','Divider'),('darkling','Nip'),('transient','Attack')]:
            self.assertIsNone(c.execute('SELECT damage FROM monster_moves WHERE monster_entity_id=? AND name=?',('sts1.monster.'+monster,name)).fetchone()[0])
        for eid,variant,expected in [('sts1.card.watcher.evaluate','base',6),('sts1.card.colorless.burn','upgrade',4)]:
            row=c.execute('SELECT parsed_json FROM card_variants cv JOIN entity_variants v ON v.id=cv.variant_id WHERE v.entity_id=? AND v.variant_kind=?',(eid,variant)).fetchone()
            if eid.endswith('evaluate'):self.assertEqual(json.loads(row[0])['game_values']['values']['block'],expected)
            else:self.assertEqual(json.loads(row[0])['game_values']['values']['magic_number'],expected)
        c.close()

if __name__=='__main__':unittest.main()
