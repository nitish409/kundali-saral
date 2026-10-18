# Copy this entire prompt into Google Antigravity

You are a senior full-stack engineer, thoughtful UI/UX designer, and responsible Jyotish application architect. I have opened a pre-existing working Python FastAPI + vanilla JS project called **Kundali Saral**. **Inspect all current code and keep the working features; do not create fake astrology calculations or replace the actual ephemeris engine with canned data.** Read README.md, PRODUCT_SPEC.md and LICENSE_NOTICE.md before making changes.

## Mission
Create a beautiful, production-ready, beginner-friendly Indian Vedic astrology web application where anyone can understand their Kundali. Every concept must have a clear explanation in **English, Hinglish and Hindi**. In BOTH Hinglish and Hindi use **Hindi-script names for all 9 grahas** throughout the interface, charts, tables, report, interpretations, navigation and PDF: सूर्य, चंद्र, मंगल, बुध, गुरु, शुक्र, शनि, राहु, केतु. Hinglish body text should be approachable Romanized Hindi, Hindi body text in Devanagari, English in simple English. Hindi zodiac sign translations should be reviewed by a native speaker. Do not sprinkle English planet labels into Hinglish or Hindi sections.

## Existing implementation (preserve / test)
- FastAPI app in `main.py`; no external AI API key required.
- Actual Swiss Ephemeris-based Lahiri sidereal chart from `astrology.py`: birth date/time, accurate timezone conversion, lat/lon, graha sign, 12 whole-sign houses, ascendant, Moon rashi, nakshatra/pada, approximate Vimshottari Mahadasha.
- `interpretations.py`: data-linked, fully localized explanations and reflection questions for personality, career, love, marriage, money, education, family, wellbeing, growth.
- `static/`: accessible responsive 3-language interface, South Indian fixed-sign chart, planet positions, dasha, JSON export and print.
- `tests/`: calculation and API smoke tests. Keep tests passing; write additional tests before changing astrology math.

## Improvements required, in order

1. **Audit and stabilize the existing MVP.** Install dependencies, run unit tests, exercise real birth charts in the browser and fix bugs. Use accurate reference test cases; verify longitude, sign boundaries, timezone DST behavior, ascendant, nakshatra, dasha birth balance and node opposition against the selected ephemeris conventions. Preserve user safety and privacy.
2. **World-class UX.** Fully responsive accessible interface for mobile and desktop, polished modern visual identity with tasteful navy, lavender, ivory and muted gold, intuitive input validation, contextual tooltips, beginner-friendly explanations, loading/error/empty states and keyboard-accessible chart. Make every visible string localizable, including all errors, badges, SEO copy and export. Use local font fallbacks for Devanagari.
3. **Traditional North Indian diamond Kundali view**, user-switchable with South Indian fixed-sign chart and a readable 12-house table. Carefully verify house geometry and position labeling; don't simply rearrange houses visually without testing.
4. **Better section readings.** For each life topic show (a) exact relevant houses/grahas/rashis, (b) transparent rule-based interpretation linked to those placements, (c) a short simple explanation of what the house and planetary ruler mean, (d) balanced strengths/challenges/areas to reflect on, (e) an uncertainty reminder. Avoid deterministic claims about marriage dates, lifespan, illness, infertility, death, financial returns or relationship success.
5. **Accurate verified additional features** after domain review: planetary dignities, aspects, Nakshatra lord, current Antardasha, divisional/Navamsa D9, safe yoga definitions, and optionally Ashtakoota compatibility where BOTH individuals consent. Do not label any unreviewed rule as accurate. Make settings for ayanamsa/house models explicit if added.
6. **Reports & sharing.** Generate a clean multi-page English/Hinglish/Hindi PDF Kundali report with chart graphics, readable Devanagari type, all nine topic areas, exact calculation settings and educational disclaimer; use server-side or browser-only PDF rendering. Include JSON export and print. Only offer a share link if explicit user opt-in and secure retention/deletion controls exist.
7. **Birthplace support.** Add a compliant, scalable geocoding/timezone provider or curated city dataset, with typed-search rate limiting, privacy protections, proper provider attribution, location disambiguation and historical timezone correctness. Public OSM Nominatim is disabled by default for a reason; do NOT build autocomplete on its shared public API.
8. **Production:** mobile QA, accessibility WCAG 2.2 AA target, localization QA by native speakers, no hard-coded secrets, security headers, request throttling, test/CI pipeline, Docker deploy, error observability (privacy-safe), SEO and appropriate deployment target. Make `README.md` contain verified end-to-end run/deploy commands. Do not invent URLs or pretend deployment succeeded.

## Domain-specific safeguards
- Clearly label **calculated astronomical facts** vs **traditional astrological interpretations**.
- Name the methodology: Lahiri ayanamsa, sidereal zodiac, whole-sign houses, mean Rahu, Moshier ephemeris, approximate dasha year convention.
- No fake 'AI accuracy percentage', no unsupported fate predictions, no superstitious fear or manipulative paid remedies.
- No medical diagnosis, investment advice, guaranteed fertility/marriage/career predictions.
- Add birth time uncertainty and DST overlap controls.
- Honor the Swiss Ephemeris / PySwissEph **AGPL-vs-professional license decision before public use**; do not declare the project commercially deployable without reviewing license.
- Strong protections around sensitive personal birth records; default no persistence.

## Acceptance criteria
- App starts with `uvicorn main:app --reload` after `pip install -r requirements.txt`.
- All tests pass; add snapshot/regression tests for specific astronomical inputs.
- User can generate a non-demo chart with real calculation and see 12 houses, 9 grahas, Lagna, rashi, Nakshatra, dasha and nine thematic sections.
- Hindi and Hinglish display Hindi-script graha names **everywhere** including PDF.
- Language changes update all dynamic sections, not just menu labels.
- App works on phone widths (360px) and screen-reader/keyboard flows.
- Accurate North/South Indian chart visual placements verified by test cases.
- Publishing steps and license requirements documented, with no secrets in repository.

Start by producing a short implementation plan, then inspect/test the current working code and improve it incrementally. Ask for feedback only when a genuine irreversible product or licensing choice is needed. Avoid unnecessary rewrites.
