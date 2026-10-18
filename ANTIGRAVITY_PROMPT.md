# COPY EVERYTHING BELOW INTO THE GOOGLE ANTIGRAVITY AGENT CHAT

You are a senior full-stack engineer, Vedic astronomy calculation reviewer, product designer, experienced three-language localization architect, accessibility engineer and security-aware project lead.

## Project objective

Upgrade the EXISTING `kundali-saral` FastAPI + HTML/CSS/JS application in this folder into a polished, trustworthy, beginner-friendly **Kundali / Vedic astrology website** in **English, Hinglish and Hindi**. It must explain all major Kundali components, actual planet placements, 12 houses, and separate life areas including **career, entrepreneurship, love, relationships, marriage, money, education, family, wellbeing, travel and personal growth**. Users must not need to know difficult Jyotish terms to understand the report.

**Critical: this is an existing working starter, NOT an empty project. Do not delete it, redesign it into static mock screenshots, replace numerical calculations with LLM predictions, or change the framework without a compelling reason.** Preserve `main.py`, `astrology.py`, `interpretations.py`, `cities.py`, `static/`, and `tests/` while improving them incrementally.

## Mandatory reading, in this order

1. `START_HERE_ANTIGRAVITY.md` — use/run/expectations.
2. `AGENTS.md` — codebase rules.
3. `README.md` and `PRODUCT_SPEC.md` — existing features.
4. `FEATURE_MASTER_LIST.md` — detailed feature scope and priorities.
5. `LANGUAGE_SYSTEM.md` — no mixed-language surprises.
6. `CALCULATION_AND_DATA_DESIGN.md` — astronomy, API, privacy, validation.
7. `IMPLEMENTATION_ROADMAP.md` — phased build and test requirements.
8. `REPORT_WIREFRAME.md` — PDF/report content.
9. `LICENSE_NOTICE.md` — required license review before launch.

## First tasks: audit, test, then build

A. Inspect project files and say what currently works and what is missing. Run `python -m pip install -r requirements.txt`, `python -m pip install pytest httpx`, `python -m pytest -q`, and start `uvicorn main:app --reload`. Verify a demo and a custom chart via API/browser. Do not claim you tested anything you did not actually test.

B. Produce a concise implementation plan organized by `IMPLEMENTATION_ROADMAP.md` phases. Begin **Phase 1** after baseline audit. Do NOT attempt all advanced Jyotish modules at once.

C. Deliver complete English/Hinglish/Hindi modes, including forms, graha names, 12 rashis, Nakshatra names, chart headings, errors, readings, tooltips, exports, PDF and accessibility labels. English mode = English names Sun/Moon/Mars and complete English explanations. Hindi = Devanagari names सूर्य/चंद्र/मंगल and natural Hindi prose. Hinglish = mostly Roman Hindi with familiar English words, consistent romanized names Surya/Chandra/Mangal; optional Devanagari pronunciation tooltips. The starter currently uses Devanagari names in Hinglish; migrate consistently per `LANGUAGE_SYSTEM.md`. Raw celestial data MUST NOT change when language changes.

D. Upgrade birth details flow (exact local time, DST ambiguity, reliable location and timezone, uncertainty warning), dashboard, modern mobile-first design, accessible output and beginner-friendly explanations. Every interpretation must show real chart factors: graha, rashi, house, house lord, and a named methodology/rule. Distinguish factual calculation from traditional symbolism. Provide independent sections for Career, Love, Marriage and Personal Growth, not interchangeable boilerplate.

E. Add a CORRECT **North Indian diamond chart** as an option in addition to the existing South Indian chart, plus full house and graha tables and contextual educational popovers. Test house numbers for all 12 Lagna signs; chart switching must not change astronomy calculations. D9 Navamsa and other charts come in a later expert-reviewed phase.

F. Expand to the life topics in `FEATURE_MASTER_LIST.md`; group them into clear tabs. For each: relevant grahas/bhavas, precise facts, traditional interpretation, possible strengths, possible challenges, reflection question, method/source and uncertainty notice. No false precision, fear-mongering, gender/religion assumptions or guaranteed outcomes.

G. Create a polished PDF report in the selected locale using `REPORT_WIREFRAME.md`; include both D1 chart views, planets/houses, separate thematic readings, Mahadasha and methodology. Embed/test fonts to avoid missing Devanagari glyphs. Keep JSON export. Do not promise the PDF feature until a rendered PDF has been tested.

H. Implement verified Antardasha, graha aspects/dignities, D9 Navamsa, Yogas/Doshas and optional two-person matching only in later phases with documented algorithms, real independent reference examples, proper consent and cautious interpretations. Advanced features must NOT be fabricated or advertised as finished before tests/review.

## Calculation guardrails

Use real offline `pyswisseph` calculations under existing Lahiri sidereal / whole sign / mean Rahu / Moshier defaults. Log methodology and versions in report. Validate independent reference charts, precise sign/Nakshatra/D9 boundaries, Julian dates, historical IANA UTC offsets, nonexistent/ambiguous DST birth times and concurrency. Avoid rounding before derivation. No external AI calls needed to calculate a chart. If AI is considered for prose, ask permission before sending private birth data to any provider and always ground content in calculated facts.

## UX requirements

- Mobile-first, functional at width 360px with modern typography, soft white/ivory surfaces, navy/plum primary color, muted gold accents; clarity over decorative astrology effects.
- Dashboard header: language control, simple input form, three/five summary cards, primary Kundali chart and report navigation.
- Define Lagna, Graha, Bhava, Rashi, Nakshatra, Dasha with interactive help in all three locales.
- Accessible forms, keyboard-operable charts, sufficient contrast, semantic headings, useful error/loading states, WCAG 2.2 AA target.
- Trust section: actual calculation settings, cultural nature of Jyotish, birth-time uncertainty, privacy/no-storage declaration.

## Release/security/legal guardrails

Respect `pyswisseph` AGPL and Swiss Ephemeris AGPL/professional licensing; do not assert production/public release compliance without a licensing decision and implementation. Public OSM Nominatim forbids autocomplete, do not introduce it. Secure validation, non-sensitive logging, HTTPS and deployment docs; do not store personal birth data unless users opt in and can delete it. Do not pretend a localhost preview is a public deployment. No medical diagnoses, investment advice, guaranteed relationship/career/marriage events or claims that astrology predicts fate scientifically.

## How to work and what to report

Work incrementally, show changed files/tests, and exercise the browser preview after each phase. Update docs when implementation differs from plan. Create accurate test cases before replacing calculations. At the end of each stage report:

1. Implemented features vs still pending.
2. Files edited.
3. Commands run and actual test results.
4. Browser/phone and language QA done or not done.
5. Known bugs, privacy/licensing blockers, and the next recommended step.

**Begin NOW with Phase 0 audit and Phase 1 localization/UI correctness. Keep the existing functioning starter working.**
