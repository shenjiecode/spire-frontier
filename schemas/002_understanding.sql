CREATE TABLE IF NOT EXISTS entity_understanding (
    entity_id TEXT PRIMARY KEY REFERENCES entities(id) ON DELETE CASCADE,
    understanding TEXT,
    origin TEXT NOT NULL DEFAULT 'empty',
    verification_status TEXT NOT NULL DEFAULT 'unreviewed'
);

CREATE TABLE IF NOT EXISTS understanding_sources (
    id TEXT PRIMARY KEY,
    entity_id TEXT NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    source_page_id TEXT NOT NULL REFERENCES source_pages(id),
    heading TEXT NOT NULL,
    locator TEXT NOT NULL,
    excerpt TEXT NOT NULL,
    extraction_method TEXT NOT NULL,
    UNIQUE(entity_id, source_page_id, locator)
);

CREATE VIEW IF NOT EXISTS entity_records AS
SELECT e.*,
 (SELECT n.name FROM names n WHERE n.entity_id=e.id AND n.language='zh-CN'
  ORDER BY n.is_preferred DESC, n.name LIMIT 1) AS name_zh,
 (SELECT n.name FROM names n WHERE n.entity_id=e.id AND n.language='en'
  ORDER BY n.is_preferred DESC, n.name LIMIT 1) AS name_en,
 u.understanding, u.origin AS understanding_origin,
 u.verification_status AS understanding_status
FROM entities e LEFT JOIN entity_understanding u ON u.entity_id=e.id;
