CREATE TABLE IF NOT EXISTS xiao_directory (
    article_id TEXT NOT NULL,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    subcategory TEXT NOT NULL,
    scope TEXT NOT NULL,
    PRIMARY KEY(article_id,name,category,subcategory)
);
CREATE TABLE IF NOT EXISTS xiao_page_review (
    article_id TEXT PRIMARY KEY,
    source_page_id TEXT REFERENCES source_pages(id),
    content_json TEXT,
    status TEXT NOT NULL,
    notes TEXT
);
CREATE TABLE IF NOT EXISTS xiao_entity_pages (
    entity_id TEXT NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    article_id TEXT NOT NULL REFERENCES xiao_page_review(article_id),
    relationship TEXT NOT NULL,
    PRIMARY KEY(entity_id,article_id)
);
CREATE TABLE IF NOT EXISTS xiao_field_checks (
    id TEXT PRIMARY KEY,
    entity_id TEXT NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    article_id TEXT REFERENCES xiao_page_review(article_id),
    field_path TEXT NOT NULL,
    current_json TEXT,
    source_json TEXT,
    status TEXT NOT NULL,
    note TEXT
);
CREATE INDEX IF NOT EXISTS idx_xiao_checks_entity ON xiao_field_checks(entity_id);
CREATE TABLE IF NOT EXISTS xiao_corrections (
    id TEXT PRIMARY KEY,
    entity_id TEXT NOT NULL REFERENCES entities(id),
    field_path TEXT NOT NULL,
    old_json TEXT,
    new_json TEXT,
    source_page_id TEXT REFERENCES source_pages(id),
    reason TEXT NOT NULL
);
