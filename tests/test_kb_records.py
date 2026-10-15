"""Focused tests for advice boundaries, manual edits and Mod identity lookup."""
import sqlite3
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts/kb'))
from build_records import sections, update_understanding
from query import find_entities


class RecordsTests(unittest.TestCase):
    def test_advice_boundaries(self):
        raw = '''<div class="article-content"><h2>小技巧</h2>
          <div><p>先打<a>能力牌</a>。</p><h3>准备</h3><p>积累资源。</p></div>
          <h2> </h2><p>准备完成。</p><h2>轶事</h2><p>不要提取。</p></div>'''
        found = sections(raw.encode())
        self.assertEqual(len(found), 1)
        self.assertIn('先打能力牌。', found[0]['excerpt'])
        self.assertIn('准备完成。', found[0]['excerpt'])
        self.assertNotIn('不要提取', found[0]['excerpt'])

    def test_no_flavor_or_empty_advice(self):
        self.assertEqual(sections('<div class="article-content"><h2>说明</h2><p>响声回荡。</p><h2>策略</h2></div>'.encode()), [])

    def test_manual_and_empty_and_idempotent(self):
        db = sqlite3.connect(':memory:')
        db.row_factory = sqlite3.Row
        db.executescript('''CREATE TABLE entities(id TEXT PRIMARY KEY);
          CREATE TABLE source_pages(id TEXT PRIMARY KEY);
          CREATE TABLE names(entity_id TEXT, language TEXT, name TEXT, is_preferred INTEGER);''')
        # The view may reference absent entity columns until queried.
        db.executescript((ROOT / 'schemas/002_understanding.sql').read_text(encoding='utf-8'))
        db.executemany('INSERT INTO entity_understanding VALUES(?,?,?,?)', [
            ('manual', '我的理解', 'manual', 'reviewed'),
            ('empty', None, 'empty', 'unreviewed'),
            ('source', None, 'empty', 'unreviewed')])
        for subject in ('manual', 'source'):
            db.execute('INSERT INTO understanding_sources VALUES(?,?,?,?,?,?,?)',
                       (subject, subject, 'page', '技巧', 'heading[1]', '来源建议', 'test'))
        update_understanding(db)
        first = [tuple(r) for r in db.execute('SELECT * FROM entity_understanding ORDER BY entity_id')]
        update_understanding(db)
        self.assertEqual(first, [tuple(r) for r in db.execute('SELECT * FROM entity_understanding ORDER BY entity_id')])
        rows = {r['entity_id']: r for r in db.execute('SELECT * FROM entity_understanding')}
        self.assertEqual(rows['manual']['understanding'], '我的理解')
        self.assertIsNone(rows['empty']['understanding'])
        self.assertEqual(rows['source']['verification_status'], 'source_opinion')
        db.close()

    def test_game_id_and_character_filter(self):
        db = sqlite3.connect(':memory:')
        db.row_factory = sqlite3.Row
        db.executescript('''CREATE TABLE entities(id TEXT,game_id TEXT,kind TEXT,lifecycle TEXT);
          CREATE TABLE cards(entity_id TEXT,character_entity_id TEXT);
          CREATE TABLE names(entity_id TEXT,language TEXT,normalized TEXT);
          CREATE VIRTUAL TABLE names_fts USING fts5(entity_id UNINDEXED,name);
          INSERT INTO entities VALUES('card','Shared','card','active'),('power','Shared','status','active');
          INSERT INTO cards VALUES('card','ironclad');
          INSERT INTO names VALUES('ironclad','en','ironclad');''')
        self.assertEqual(len(find_entities(db, 'Shared')), 2)
        self.assertEqual(find_entities(db, 'Shared', 'card', 'ironclad')[0]['id'], 'card')
        self.assertEqual(find_entities(db, 'Shared', 'card', 'silent'), [])
        db.close()


if __name__ == '__main__':
    unittest.main()
