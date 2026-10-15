# Spire Frontier

English | [简体中文](README.zh.md)

Exploring the limits of AI in **Slay the Spire 1**, from a traceable knowledge base and strategy collection to agents that play, learn from feedback, and improve through measured experiments.

## Research scope and current stage

- **Knowledge foundation — implemented:** bilingual Wiki sources, a SQLite knowledge base, structured records, provenance, and review workflows.
- **Game interaction — prototype:** a CommunicationMod bridge, a rule-based agent, and an offline smoke test.
- **Strategy collection — planned:** organize guides, decision rationales, and their conditions separately from game facts.
- **Agent evaluation — planned:** compare models, tools, and memory approaches through reproducible experiments and failure analysis.
- **Agent self-improvement — exploratory:** investigate how gameplay feedback can improve strategies and memory, and measure whether those changes help.

The current focus is knowledge-base construction and verification. Autonomous learning and a complete evaluation framework are research directions, not implemented capabilities.

## Current knowledge base

SQLite (`data/spire.sqlite`) is the primary store. Category-based JSONL records are available in `data/records/`; `docs/wiki/` is a generated browsing layer. The current system does not use RAG or vector retrieval.

- 1,157 entities: 974 active, 173 candidate, and 10 deprecated records.
- 895 Xiaoheihe articles covered by the review inventory; coverage does not mean every rule has been semantically verified.
- 584 card variants with directly confirmed game values and 714 with rendered bilingual descriptions.
- 35 active entities with attributed source advice; missing advice remains null.

Sources include [Slay the Spire Wiki](https://slaythespire.wiki.gg/), [Xiaoheihe Wiki](https://web.xiaoheihe.cn/wiki/home?wiki_id=646570), and locally extracted game evidence. Source opinions, unresolved differences, and verified facts remain distinguishable.

## Getting started

Use Python 3.10 or later. From the repository root:

```powershell
python -m pip install -r requirements.txt
$env:PYTHONIOENCODING='utf-8'
python -B -m unittest discover -s tests -p "test_kb_*.py" -v
python -B tests/smoke_test.py
python scripts/kb/validate_kb.py
```

The smoke test runs offline without launching the game. Validation writes `reports/p1-validation.json`. Actual gameplay requires your own installation of Slay the Spire and the appropriate mod setup.

## Project layout and documentation

- `bridge/`: game bridge and rule-based agent.
- `scripts/kb/`, `schemas/`: ingestion, review, export, query, and database tools.
- `data/`: database, structured exports, review decisions, and source evidence.
- `tests/`: knowledge-base regression tests and bridge smoke test.
- [Knowledge-base workflow and detailed status (Chinese)](README.zh.md#知识库).
- [Database record guide (Chinese)](docs/数据库记录说明.md).
- [Source review report (Chinese)](reports/xiaoheihe-full-review.md).
- [Original agent design (Chinese)](docs/设计文档-杀戮尖塔视频学习Agent.md).

## License

Original project code and documentation are licensed under the [MIT License](LICENSE). Third-party Wiki content, game text, images, and vendored code retain their own rights and licensing terms; see [Third-party notices](docs/THIRD_PARTY_NOTICES.md).

This is an independent research project and is not affiliated with or endorsed by the game's creators.
