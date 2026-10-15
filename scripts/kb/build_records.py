"""Build database-first records and source-attributed Xiaoheihe understanding.

Uses saved article snapshots only. No images or independent guide documents.
Only explicitly named advice sections are copied; flavor text and rule
descriptions do not become advice merely because they are called '说明'.
"""
from __future__ import annotations

import hashlib
import json
import re
import sqlite3
from collections import Counter

from lxml import html

from bootstrap_sample import ROOT, DB_PATH, export_data

HEADINGS = {
    '策略', '小技巧', '技巧', '应对', '玩家对策', '应对方法',
    '协同效应', '卡牌基础策略', '使用技巧', '使用方法', '用法',
    '卡牌分析', '卡牌评价', '评价', '搭配',
}
TABLES = dict(character='characters', card='cards', relic='relics',
              potion='potions', monster='monsters', encounter='encounters',
              event='events', status='statuses', keyword='keywords', mechanic='mechanics')
CHILDREN = {
    'monster': ('monster_moves', 'monster_entity_id'),
    'event': ('event_options', 'event_entity_id'),
    'encounter': ('encounter_members', 'encounter_entity_id'),
}


def sections(raw: bytes) -> list[dict]:
    tree = html.fromstring(raw.decode('utf-8'))
    roots = tree.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," article-content ")]')
    if not roots:
        return []
    root = roots[0]
    headings = root.xpath('.//h1|.//h2|.//h3|.//h4|.//h5|.//h6')
    result = []
    for ordinal, heading in enumerate(headings):
        title = ' '.join(heading.text_content().split()).strip('：: ')
        if title not in HEADINGS:
            continue
        # Walk text events to preserve nested paragraphs without duplicating
        # descendants. Blank formatting headings do not terminate a section.
        active = False
        chunks = []
        for action, node in html.etree.iterwalk(root, events=('start', 'end')):
            if action == 'start':
                if node is heading:
                    active = True
                elif active and isinstance(node.tag, str) and re.fullmatch(r'h[1-6]', node.tag):
                    text = ' '.join(node.text_content().split())
                    if text and int(node.tag[1]) <= int(heading.tag[1]):
                        break
                if active and node.text:
                    chunks.append(node.text)
            elif active:
                if node.tag in ('p', 'div', 'li', 'br', 'h1', 'h2', 'h3', 'h4'):
                    chunks.append('\n')
                if node.tail:
                    chunks.append(node.tail)
        text = ''.join(chunks).replace('请输入图片描述', '').replace('输入图片描述', '')
        lines = [' '.join(line.split()) for line in text.splitlines()]
        lines = [line for line in lines if line]
        if lines and lines[0].strip('：: ') == title:
            lines.pop(0)
        excerpt = '\n'.join(lines).strip()
        if excerpt:
            result.append(dict(heading=title, locator=f'article-content/heading[{ordinal+1}]', excerpt=excerpt))
    return result


def decode(row) -> dict:
    result = dict(row)
    for key, value in list(result.items()):
        if key.endswith('_json'):
            result[key[:-5]] = json.loads(value) if value is not None else None
            del result[key]
    return result


def record(conn, row) -> dict:
    result = dict(row)
    entity_id = row['id']
    result['names'] = [dict(n) for n in conn.execute(
        'SELECT language,name,name_kind FROM names WHERE entity_id=? ORDER BY language,name,name_kind', (entity_id,))]
    table = TABLES.get(row['kind'])
    data = conn.execute(f'SELECT * FROM {table} WHERE entity_id=?', (entity_id,)).fetchone() if table else None
    result['data'] = decode(data) if data else None
    if row['kind']=='status' and result['data'] is not None:
        for language,suffix in [('zh-CN','zh'),('en','en')]:
            claim=conn.execute("""SELECT value_json,source_page_id,verification_status FROM claims
                WHERE subject_entity_id=? AND field_path='status.description' AND language=?
                AND COALESCE(notes,'') NOT LIKE '%superseded:%' ORDER BY created_at DESC,id DESC LIMIT 1""",(entity_id,language)).fetchone()
            if claim:
                result['data']['description_'+suffix]=json.loads(claim['value_json'])
                result['data']['description_'+suffix+'_source_page_id']=claim['source_page_id']
    if row['kind'] == 'card':
        result['variants'] = [decode(v) for v in conn.execute('''
            SELECT v.id,v.variant_kind,v.level,v.condition_json,c.cost_type,c.cost_value,
                   c.description_zh,c.description_en,c.parsed_json
            FROM entity_variants v JOIN card_variants c ON c.variant_id=v.id
            WHERE v.entity_id=? ORDER BY v.id''', (entity_id,))]
    if row['kind'] in CHILDREN:
        child, foreign = CHILDREN[row['kind']]
        result[child] = [decode(r) for r in conn.execute(f'SELECT * FROM {child} WHERE {foreign}=? ORDER BY 1', (entity_id,))]
    result['understanding_sources'] = [dict(r) for r in conn.execute('''
        SELECT u.heading,u.excerpt,u.locator,u.source_page_id,p.url,p.sha256,p.fetched_at
        FROM understanding_sources u JOIN source_pages p ON p.id=u.source_page_id
        WHERE u.entity_id=? ORDER BY p.id,u.locator''', (entity_id,))]
    # Category paths come from the article's own directory rows, not name
    # similarity. Grouped pages remain groups rather than assigning advice
    # arbitrarily to every monster child.
    result['categories'] = [dict(r) for r in conn.execute('''
        SELECT DISTINCT i.category,i.subcategory,i.character,i.url
        FROM inventory_items i JOIN source_pages p ON p.url=i.url
        JOIN claims c ON c.source_page_id=p.id
        WHERE c.subject_entity_id=? AND c.field_path='source.article_text'
          AND p.source_id='xiaoheihe' ORDER BY i.category,i.subcategory,i.url''', (entity_id,))]
    if conn.execute("SELECT 1 FROM sqlite_master WHERE name='xiao_entity_pages'").fetchone():
        result['categories']=[dict(r) for r in conn.execute('''SELECT DISTINCT d.category,d.subcategory,d.article_id
            FROM xiao_directory d JOIN xiao_entity_pages x USING(article_id) WHERE x.entity_id=?
            ORDER BY d.category,d.subcategory,d.article_id''',(entity_id,))]
        result['xiaoheihe']=[dict(r) for r in conn.execute('''SELECT x.article_id,x.relationship,p.status,p.source_page_id,s.url,s.fetched_at
            FROM xiao_entity_pages x JOIN xiao_page_review p USING(article_id) JOIN source_pages s ON s.id=p.source_page_id
            WHERE x.entity_id=? ORDER BY x.article_id''',(entity_id,))]
        result['review_checks']=[dict(r) for r in conn.execute('''SELECT field_path,status,note FROM xiao_field_checks
            WHERE entity_id=? ORDER BY article_id,field_path''',(entity_id,))]
    return result


def update_understanding(conn):
    """Refresh source-derived prose while preserving manually authored rows."""
    for row in conn.execute("SELECT * FROM entity_understanding WHERE origin IN ('empty','xiaoheihe')").fetchall():
        excerpts = conn.execute('SELECT heading,excerpt FROM understanding_sources WHERE entity_id=? ORDER BY source_page_id,locator', (row['entity_id'],)).fetchall()
        text = '\n\n'.join(dict.fromkeys(f"{r['heading']}\n{r['excerpt']}" for r in excerpts)) or None
        conn.execute('UPDATE entity_understanding SET understanding=?,origin=?,verification_status=? WHERE entity_id=?',
                     (text,'xiaoheihe' if text else 'empty','source_opinion' if text else 'unreviewed',row['entity_id']))


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA foreign_keys=ON')
    conn.executescript((ROOT/'schemas/002_understanding.sql').read_text(encoding='utf-8'))
    with conn:
        conn.execute('INSERT OR IGNORE INTO entity_understanding(entity_id) SELECT id FROM entities')
        conn.execute("DELETE FROM understanding_sources WHERE extraction_method='xiaoheihe_advice_heading_v1'")
        reviewed=bool(conn.execute("SELECT 1 FROM sqlite_master WHERE name='xiao_entity_pages'").fetchone())
        if reviewed:
            pages=conn.execute('''SELECT DISTINCT s.* FROM source_pages s JOIN xiao_page_review p ON p.source_page_id=s.id
                JOIN xiao_entity_pages x USING(article_id) WHERE x.relationship!='member_of_group' ORDER BY s.id''').fetchall()
        else:
            pages = conn.execute('''SELECT DISTINCT p.* FROM source_pages p JOIN claims c ON c.source_page_id=p.id
                WHERE p.source_id='xiaoheihe' AND c.field_path='source.article_text' ORDER BY p.id''').fetchall()
        for page in pages:
            extracted = sections((ROOT/page['snapshot_path']).read_bytes())
            if reviewed:
                subjects=conn.execute("SELECT DISTINCT x.entity_id FROM xiao_entity_pages x JOIN xiao_page_review p USING(article_id) WHERE p.source_page_id=? AND x.relationship!='member_of_group'",(page['id'],)).fetchall()
            else:
                subjects = conn.execute("SELECT DISTINCT subject_entity_id FROM claims WHERE source_page_id=? AND field_path='source.article_text'", (page['id'],)).fetchall()
            for subject in subjects:
                for section in extracted:
                    key = '|'.join((subject[0], page['id'], section['locator']))
                    conn.execute('INSERT OR REPLACE INTO understanding_sources VALUES(?,?,?,?,?,?,?)',
                        ('understanding.'+hashlib.sha256(key.encode()).hexdigest()[:24], subject[0], page['id'],
                         section['heading'], section['locator'], section['excerpt'], 'xiaoheihe_advice_heading_v1'))
        update_understanding(conn)
    export_data(conn)
    output = ROOT/'data/records'
    output.mkdir(exist_ok=True)
    if reviewed:
        with (output/'xiaoheihe_articles.jsonl').open('w',encoding='utf-8',newline='\n') as f:
            for page in conn.execute('SELECT * FROM xiao_page_review ORDER BY article_id'):
                item=decode(page)
                item['directory']=[dict(r) for r in conn.execute('SELECT name,category,subcategory,scope FROM xiao_directory WHERE article_id=? ORDER BY category,subcategory,name',(page['article_id'],))]
                f.write(json.dumps(item,ensure_ascii=False,sort_keys=True)+'\n')
    counts = Counter()
    for kind in [r[0] for r in conn.execute('SELECT DISTINCT kind FROM entities ORDER BY kind')]:
        with (output/f'{kind}.jsonl').open('w',encoding='utf-8',newline='\n') as f:
            for row in conn.execute("SELECT * FROM entity_records WHERE kind=? AND lifecycle='active' ORDER BY id", (kind,)):
                f.write(json.dumps(record(conn,row),ensure_ascii=False,sort_keys=True)+'\n')
                counts[kind] += 1
    report = dict(records=dict(counts), understanding_by_kind=[dict(r) for r in conn.execute('''
        SELECT e.kind,e.lifecycle,count(*) AS total,sum(u.understanding IS NOT NULL) AS filled
        FROM entities e JOIN entity_understanding u ON u.entity_id=e.id
        GROUP BY e.kind,e.lifecycle ORDER BY e.kind,e.lifecycle''')],
        source_sections=conn.execute('SELECT count(*) FROM understanding_sources').fetchone()[0],
        note='Understanding is attributed source opinion, not a verified rule. Missing values are null. Images and independent guides are not read.')
    (ROOT/'reports/database-records.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    conn.close()


if __name__ == '__main__':
    main()
