# Working rules for the Kundali Saral codebase

1. This is an existing FastAPI + vanilla JavaScript project, NOT an empty repo. Inspect all existing files before editing. Preserve astronomy math and runnable features while upgrading incrementally.
2. Read `START_HERE_ANTIGRAVITY.md`, `PRODUCT_SPEC.md`, `FEATURE_MASTER_LIST.md`, `LANGUAGE_SYSTEM.md`, `CALCULATION_AND_DATA_DESIGN.md`, `IMPLEMENTATION_ROADMAP.md`, and `LICENSE_NOTICE.md`.
3. Run `python -m pytest -q` BEFORE and AFTER major changes. Write deterministic regression tests for birth time UTC conversion, Lahiri sidereal positions, Rahu/Ketu opposition, house mapping, D9 and dashas when introduced. Never invent chart data.
4. English, Hinglish and Hindi are full locale modes, not translation of headings only. Astrology calculations are locale-neutral; translations must not change positions. Follow `LANGUAGE_SYSTEM.md`.
5. Separate *computed facts*, *traditional interpretations*, *practical reflection*, and *method limitations*. Never present astrology as scientifically proven future prediction. No guaranteed job/marriage, fertility/death claims, or medical/investment advice.
6. Stage advanced features behind disabled/experimental flags until formulas, reference examples, and reviewer sign-off exist.
7. Privacy first: no birth data saved by default, HTTPS before production, input validation, safe handling of API logs, no hidden third-party AI sharing, and no secrets committed.
8. Respect PySwissEph/Swiss Ephemeris licensing and external geocoding policies. Do not enable public Nominatim autocomplete.
9. Favor small, reviewed changes over a full-stack rewrite. No change of framework or deployment assertions without specific justification.
10. For each phase: show the plan, files changed, UI preview, tests and known unfinished points.
