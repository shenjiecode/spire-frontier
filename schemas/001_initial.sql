PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS schema_meta (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

INSERT OR IGNORE INTO schema_meta(key, value) VALUES
    ('schema_version', '1'),
    ('game', 'Slay the Spire 1'),
    ('ruleset', 'pc-original'),
    ('created_at', '2026-09-17');

CREATE TABLE IF NOT EXISTS sources (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    base_url TEXT NOT NULL,
    language TEXT NOT NULL CHECK(language IN ('zh-CN', 'en', 'mixed', 'und')),
    license TEXT,
    source_kind TEXT NOT NULL CHECK(source_kind IN ('wiki', 'game_data', 'experiment', 'guide', 'other')),
    scope_note TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS source_pages (
    id TEXT PRIMARY KEY,
    source_id TEXT NOT NULL REFERENCES sources(id),
    url TEXT NOT NULL UNIQUE,
    title TEXT,
    source_page_key TEXT,
    article_id TEXT,
    revision_id TEXT,
    edited_at TEXT,
    fetched_at TEXT NOT NULL,
    http_status INTEGER,
    content_type TEXT,
    snapshot_path TEXT,
    sha256 TEXT,
    parser_version TEXT,
    is_index_page INTEGER NOT NULL DEFAULT 0 CHECK(is_index_page IN (0, 1)),
    notes TEXT
);

CREATE TABLE IF NOT EXISTS entities (
    id TEXT PRIMARY KEY,
    kind TEXT NOT NULL CHECK(kind IN (
        'character', 'card', 'relic', 'potion', 'monster', 'encounter',
        'event', 'status', 'keyword', 'mechanic', 'resource', 'concept'
    )),
    game TEXT NOT NULL DEFAULT 'sts1' CHECK(game IN ('sts1', 'sts2', 'other')),
    subtype TEXT,
    game_id TEXT,
    lifecycle TEXT NOT NULL DEFAULT 'active' CHECK(lifecycle IN ('active', 'deprecated', 'candidate')),
    mapping_status TEXT NOT NULL DEFAULT 'unverified' CHECK(mapping_status IN (
        'unverified', 'provisional', 'confirmed', 'ambiguous', 'rejected'
    )),
    notes TEXT
);

CREATE TABLE IF NOT EXISTS names (
    entity_id TEXT NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    language TEXT NOT NULL CHECK(language IN ('zh-CN', 'en', 'ja', 'ko', 'und')),
    name TEXT NOT NULL,
    normalized TEXT NOT NULL,
    name_kind TEXT NOT NULL CHECK(name_kind IN (
        'preferred', 'source_name', 'localization', 'alias', 'old_alias', 'candidate'
    )),
    source_page_id TEXT REFERENCES source_pages(id),
    verification_status TEXT NOT NULL DEFAULT 'unverified' CHECK(verification_status IN (
        'unverified', 'single_source', 'agreed', 'conflict', 'verified_game'
    )),
    is_preferred INTEGER NOT NULL DEFAULT 0 CHECK(is_preferred IN (0, 1)),
    notes TEXT,
    PRIMARY KEY(entity_id, language, name, name_kind)
);

CREATE INDEX IF NOT EXISTS idx_names_lookup ON names(language, normalized);
CREATE INDEX IF NOT EXISTS idx_entities_kind ON entities(kind, subtype);

CREATE TABLE IF NOT EXISTS entity_variants (
    id TEXT PRIMARY KEY,
    entity_id TEXT NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    variant_kind TEXT NOT NULL CHECK(variant_kind IN (
        'base', 'upgrade', 'upgrade_level', 'beta', 'ascension', 'condition', 'other'
    )),
    level INTEGER,
    condition_json TEXT,
    label TEXT,
    UNIQUE(entity_id, variant_kind, level, label)
);

CREATE TABLE IF NOT EXISTS characters (
    entity_id TEXT PRIMARY KEY REFERENCES entities(id) ON DELETE CASCADE,
    initial_hp INTEGER,
    initial_gold INTEGER,
    potion_slots INTEGER,
    starting_relic_entity_id TEXT REFERENCES entities(id),
    starting_deck_json TEXT,
    resource_json TEXT,
    mechanics_json TEXT
);

CREATE TABLE IF NOT EXISTS cards (
    entity_id TEXT PRIMARY KEY REFERENCES entities(id) ON DELETE CASCADE,
    character_entity_id TEXT REFERENCES entities(id),
    color TEXT NOT NULL CHECK(color IN ('Red', 'Green', 'Blue', 'Purple', 'Colorless', 'Status', 'Curse', 'Other')),
    card_type TEXT NOT NULL CHECK(card_type IN ('Attack', 'Skill', 'Power', 'Status', 'Curse', 'Other')),
    rarity TEXT,
    target TEXT,
    availability TEXT,
    tags_json TEXT
);

CREATE TABLE IF NOT EXISTS card_variants (
    variant_id TEXT PRIMARY KEY REFERENCES entity_variants(id) ON DELETE CASCADE,
    cost_type TEXT CHECK(cost_type IN ('fixed', 'x', 'unplayable', 'conditional', 'unknown')),
    cost_value REAL,
    description_en TEXT,
    description_zh TEXT,
    parsed_json TEXT,
    image_asset_id TEXT REFERENCES assets(id)
);

CREATE TABLE IF NOT EXISTS relics (
    entity_id TEXT PRIMARY KEY REFERENCES entities(id) ON DELETE CASCADE,
    rarity TEXT,
    character_entity_id TEXT REFERENCES entities(id),
    acquisition_json TEXT,
    effect_json TEXT,
    trigger_timing TEXT,
    counter_json TEXT
);

CREATE TABLE IF NOT EXISTS potions (
    entity_id TEXT PRIMARY KEY REFERENCES entities(id) ON DELETE CASCADE,
    rarity TEXT,
    character_entity_id TEXT REFERENCES entities(id),
    target TEXT,
    use_timing TEXT,
    effect_json TEXT,
    enhancement_json TEXT
);

CREATE TABLE IF NOT EXISTS monsters (
    entity_id TEXT PRIMARY KEY REFERENCES entities(id) ON DELETE CASCADE,
    category TEXT CHECK(category IN ('normal', 'elite', 'boss', 'other')),
    act TEXT,
    hp_min INTEGER,
    hp_max INTEGER,
    initial_state_json TEXT,
    ascension_json TEXT,
    encounter_notes TEXT
);

CREATE TABLE IF NOT EXISTS monster_moves (
    id TEXT PRIMARY KEY,
    monster_entity_id TEXT NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    intent TEXT,
    damage INTEGER,
    hits INTEGER,
    effect_json TEXT,
    condition_json TEXT,
    probability_json TEXT,
    order_rules TEXT
);

CREATE TABLE IF NOT EXISTS encounters (
    entity_id TEXT PRIMARY KEY REFERENCES entities(id) ON DELETE CASCADE,
    act TEXT,
    room_type TEXT,
    pool_type TEXT,
    weight_json TEXT,
    repetition_rules TEXT
);

CREATE TABLE IF NOT EXISTS encounter_members (
    encounter_entity_id TEXT NOT NULL REFERENCES encounters(entity_id) ON DELETE CASCADE,
    monster_entity_id TEXT NOT NULL REFERENCES entities(id),
    quantity INTEGER NOT NULL DEFAULT 1,
    position INTEGER,
    PRIMARY KEY(encounter_entity_id, monster_entity_id, position)
);

CREATE TABLE IF NOT EXISTS events (
    entity_id TEXT PRIMARY KEY REFERENCES entities(id) ON DELETE CASCADE,
    acts_json TEXT,
    room_type TEXT,
    appearance_condition_json TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS event_options (
    id TEXT PRIMARY KEY,
    event_entity_id TEXT NOT NULL REFERENCES events(entity_id) ON DELETE CASCADE,
    ordinal INTEGER NOT NULL,
    label TEXT NOT NULL,
    condition_json TEXT,
    cost_json TEXT,
    outcome_json TEXT,
    locked_when_json TEXT
);

CREATE TABLE IF NOT EXISTS statuses (
    entity_id TEXT PRIMARY KEY REFERENCES entities(id) ON DELETE CASCADE,
    polarity TEXT CHECK(polarity IN ('positive', 'negative', 'neutral')),
    affects TEXT,
    stacking TEXT,
    duration TEXT,
    trigger_timing TEXT,
    removal TEXT
);

CREATE TABLE IF NOT EXISTS keywords (
    entity_id TEXT PRIMARY KEY REFERENCES entities(id) ON DELETE CASCADE,
    definition_json TEXT,
    applies_to TEXT
);

CREATE TABLE IF NOT EXISTS mechanics (
    entity_id TEXT PRIMARY KEY REFERENCES entities(id) ON DELETE CASCADE,
    definition_json TEXT,
    timing_json TEXT,
    exceptions_json TEXT
);

CREATE TABLE IF NOT EXISTS assets (
    id TEXT PRIMARY KEY,
    sha256 TEXT NOT NULL UNIQUE,
    original_url TEXT NOT NULL,
    local_path TEXT NOT NULL,
    mime_type TEXT,
    byte_size INTEGER,
    width INTEGER,
    height INTEGER,
    language TEXT,
    usage_kind TEXT,
    source_page_id TEXT REFERENCES source_pages(id),
    fetched_at TEXT NOT NULL,
    license_status TEXT NOT NULL DEFAULT 'unknown',
    attribution TEXT
);

CREATE TABLE IF NOT EXISTS entity_assets (
    entity_id TEXT NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    asset_id TEXT NOT NULL REFERENCES assets(id) ON DELETE CASCADE,
    variant_id TEXT REFERENCES entity_variants(id),
    role TEXT NOT NULL CHECK(role IN ('card_base', 'card_upgrade', 'icon', 'portrait', 'map', 'evidence', 'other')),
    PRIMARY KEY(entity_id, asset_id, role)
);

CREATE TABLE IF NOT EXISTS claims (
    id TEXT PRIMARY KEY,
    subject_entity_id TEXT NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    variant_id TEXT REFERENCES entity_variants(id) ON DELETE CASCADE,
    field_path TEXT NOT NULL,
    value_json TEXT NOT NULL,
    value_type TEXT NOT NULL CHECK(value_type IN ('text', 'number', 'boolean', 'object', 'array', 'null')),
    language TEXT,
    source_page_id TEXT NOT NULL REFERENCES source_pages(id),
    locator TEXT,
    extraction_method TEXT NOT NULL CHECK(extraction_method IN ('structured_html', 'wikitext', 'visible_text', 'image_ocr', 'manual', 'experiment')),
    verification_status TEXT NOT NULL DEFAULT 'unverified' CHECK(verification_status IN (
        'unverified', 'single_source', 'agreed', 'conflict', 'verified_game'
    )),
    created_at TEXT NOT NULL,
    notes TEXT
);

CREATE INDEX IF NOT EXISTS idx_claims_subject ON claims(subject_entity_id, field_path);

CREATE TABLE IF NOT EXISTS resolutions (
    id TEXT PRIMARY KEY,
    subject_entity_id TEXT NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    variant_id TEXT REFERENCES entity_variants(id) ON DELETE CASCADE,
    field_path TEXT NOT NULL,
    adopted_claim_id TEXT REFERENCES claims(id),
    value_json TEXT,
    status TEXT NOT NULL CHECK(status IN ('provisional', 'adopted', 'unknown', 'rejected')),
    rationale TEXT,
    decided_at TEXT NOT NULL,
    decided_by TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS relations (
    id TEXT PRIMARY KEY,
    source_entity_id TEXT NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    relation_type TEXT NOT NULL,
    target_entity_id TEXT NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    condition_json TEXT,
    source_page_id TEXT REFERENCES source_pages(id),
    status TEXT NOT NULL DEFAULT 'candidate' CHECK(status IN ('candidate', 'confirmed', 'conflict', 'rejected')),
    notes TEXT,
    UNIQUE(source_entity_id, relation_type, target_entity_id, condition_json)
);

CREATE INDEX IF NOT EXISTS idx_relations_source ON relations(source_entity_id, relation_type);
CREATE INDEX IF NOT EXISTS idx_relations_target ON relations(target_entity_id, relation_type);

-- P2 directory discovery is kept separate from reconciled entities.  An
-- inventory row records what a source lists; it does not assert that the
-- Chinese and English rows refer to the same game object.
CREATE TABLE IF NOT EXISTS inventory_items (
    id TEXT PRIMARY KEY,
    source_id TEXT NOT NULL REFERENCES sources(id) ON DELETE CASCADE,
    source_page_id TEXT REFERENCES source_pages(id) ON DELETE SET NULL,
    source_item_key TEXT NOT NULL,
    entity_kind TEXT NOT NULL,
    language TEXT NOT NULL CHECK(language IN ('zh-CN', 'en', 'und')),
    name TEXT NOT NULL,
    article_id TEXT,
    url TEXT NOT NULL,
    category TEXT,
    subcategory TEXT,
    character TEXT,
    metadata_json TEXT,
    discovered_at TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'discovered' CHECK(status IN (
        'discovered', 'fetched', 'parsed', 'mapped', 'excluded', 'failed'
    )),
    UNIQUE(source_id, source_item_key)
);

CREATE INDEX IF NOT EXISTS idx_inventory_kind ON inventory_items(entity_kind, language);
CREATE INDEX IF NOT EXISTS idx_inventory_source ON inventory_items(source_id, category);

CREATE TABLE IF NOT EXISTS inventory_mappings (
    id TEXT PRIMARY KEY,
    zh_inventory_id TEXT NOT NULL REFERENCES inventory_items(id) ON DELETE CASCADE,
    en_inventory_id TEXT NOT NULL REFERENCES inventory_items(id) ON DELETE CASCADE,
    status TEXT NOT NULL CHECK(status IN ('candidate', 'confirmed', 'conflict', 'rejected')),
    rationale TEXT,
    evidence_json TEXT,
    decided_at TEXT NOT NULL,
    UNIQUE(zh_inventory_id, en_inventory_id)
);

CREATE INDEX IF NOT EXISTS idx_inventory_mapping_zh ON inventory_mappings(zh_inventory_id, status);
CREATE INDEX IF NOT EXISTS idx_inventory_mapping_en ON inventory_mappings(en_inventory_id, status);

CREATE TABLE IF NOT EXISTS strategy_notes (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT,
    document_path TEXT,
    chapter_anchor TEXT,
    published_at TEXT,
    source_kind TEXT NOT NULL DEFAULT 'guide',
    notes TEXT
);

CREATE TABLE IF NOT EXISTS strategy_links (
    strategy_note_id TEXT NOT NULL REFERENCES strategy_notes(id) ON DELETE CASCADE,
    entity_id TEXT NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    link_kind TEXT NOT NULL CHECK(link_kind IN ('mention', 'synergy', 'evaluation', 'example', 'concept')),
    condition_json TEXT,
    excerpt TEXT,
    PRIMARY KEY(strategy_note_id, entity_id, link_kind)
);

CREATE TABLE IF NOT EXISTS build_runs (
    id TEXT PRIMARY KEY,
    started_at TEXT NOT NULL,
    finished_at TEXT,
    status TEXT NOT NULL CHECK(status IN ('running', 'success', 'failed')),
    parser_version TEXT NOT NULL,
    counts_json TEXT,
    notes TEXT
);

CREATE VIRTUAL TABLE IF NOT EXISTS names_fts USING fts5(
    entity_id UNINDEXED,
    language UNINDEXED,
    name,
    normalized,
    content='names',
    content_rowid='rowid'
);

CREATE TRIGGER IF NOT EXISTS names_ai AFTER INSERT ON names BEGIN
    INSERT INTO names_fts(rowid, entity_id, language, name, normalized)
    VALUES (new.rowid, new.entity_id, new.language, new.name, new.normalized);
END;

CREATE TRIGGER IF NOT EXISTS names_ad AFTER DELETE ON names BEGIN
    INSERT INTO names_fts(names_fts, rowid, entity_id, language, name, normalized)
    VALUES ('delete', old.rowid, old.entity_id, old.language, old.name, old.normalized);
END;

CREATE TRIGGER IF NOT EXISTS names_au AFTER UPDATE ON names BEGIN
    INSERT INTO names_fts(names_fts, rowid, entity_id, language, name, normalized)
    VALUES ('delete', old.rowid, old.entity_id, old.language, old.name, old.normalized);
    INSERT INTO names_fts(rowid, entity_id, language, name, normalized)
    VALUES (new.rowid, new.entity_id, new.language, new.name, new.normalized);
END;
