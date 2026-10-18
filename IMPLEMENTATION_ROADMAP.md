# Antigravity development roadmap and definition of done

All phases must keep the previous phase working. Mark a feature "done" only with code, tests and visible UI evidence.

## Phase 0 — Baseline audit (first agent task)

- [ ] Read all existing files. Confirm original behavior and feature limitations.
- [ ] Run `python -m pytest -q` and record results; check server and sample API request.
- [ ] Audit date/time, concurrent `pyswisseph` use, chart positioning, reflected HTML and public API error handling.
- [ ] Ensure existing website runs at `http://127.0.0.1:8000` and document actual result.
- [ ] Do not swap out existing engine for mock/static astrology data.

## Phase 1 — Language-first, polished baseline (must do first)

- [ ] Centralize all three locales following `LANGUAGE_SYSTEM.md` for UI, chart, house table, full reading, help, errors, and export.
- [ ] Convert Hinglish to mostly Roman-script as default (provide optional original Hindi-script graha display, if useful); consistent phrase choices.
- [ ] Introduce stable internal planet/rashi identifiers separated from localized labels.
- [ ] Add full planet details panel and all 12 house explanations with source placements.
- [ ] Make reading sections better: factual evidence / symbolic interpretation / possible strength / possible challenge / reflection.
- [ ] Add optional birth-time-uncertain warning + proper input validation and timezone DST-overlap handling.
- [ ] Mobile-friendly UI and screen-reader accessible labels; 360px QA.
- [ ] Tests: calculation parity across languages, UI language coverage, valid/invalid input and sample regressions.

## Phase 2 — Charts and clear explanations

- [ ] North Indian diamond chart with accurate fixed-house geometry and dynamically assigned rashis/grahas.
- [ ] Preserve South Indian sign-fixed style; allow user to switch immediately without recalculating.
- [ ] Every chart house is clickable/keyboard-operable; show house lord and sign, planetary position and meaning.
- [ ] Add explanations of Lagna, Nakshatra, Bhava, Graha, Pada, dashas. Add 27-nakshatra dictionary in each language.
- [ ] Verify chart positions against D1 reference cases; table fallback matches graphical data.
- [ ] Tests for rotation/mapping of every ascendant sign and for crowded/empty houses.

## Phase 3 — Deeper readings and reports

- [ ] Expand life sections towards the 17 topics in `FEATURE_MASTER_LIST.md` (grouped by intuitive categories, not 17 cluttered tabs).
- [ ] Each reading names the relevant house(s), ruling planet(s), actual placement, method/rule ID, balanced strengths/challenges and concrete reflection question.
- [ ] Introduce versioned, reviewed traditional rules for aspects and dignities; don't infer a yoga/dosha from generic prose.
- [ ] Design multi-page PDF with both chart styles, data tables, reports, timing, metadata and fully embedded Unicode/Devanagari fonts.
- [ ] Test English/Hinglish/Hindi PDF output for glyph completeness and print page breaks.
- [ ] Continue providing original JSON export.

## Phase 4 — Expert-validated advanced Jyotish

- [ ] Implement and test Nakshatra lord, detailed Dasha balances and Antardasha; double-check time-convention and boundaries.
- [ ] Implement D9 Navamsa only after formula review and independent validation; D10 later, if justified.
- [ ] Add transits, aspects, dignities, Yogas/Doshas or compatibility only as separate tested features with method-specific evidence and non-alarmist writing.
- [ ] Optional two-person matching only with appropriate consent from both people; make no deterministic marriage outcome claims.
- [ ] Create a comparison sheet of at least 20 independently validated chart examples and sources.

## Phase 5 — Launch readiness (separate decision)

- [ ] Swiss Ephemeris / PySwissEph license compliance route decided and implemented in notices/distributions.
- [ ] Privacy policy and hosting data retention documented accurately; no unauthorized storage or external AI data sharing.
- [ ] Replace public Nominatim use with compliant production geocoding (or keep curated offline list + manual details).
- [ ] HTTPS, security headers, CORS, rate limits, error monitoring without private birth details, backups if any storage.
- [ ] Accessibility WCAG 2.2 AA, 360/390/768/1024/1440px review, browser QA, native-language review.
- [ ] Build, test, start and deploy instructions verified for chosen hosting provider; real domain and actual live URL only after successful deployment.

## Minimum product acceptance: 12 visible checks

1. Any person can enter DOB, exact time and location and generate a **calculated**, non-demo D1 chart.
2. Exactly 9 grahas / 12 bhavas / Lagna / Nakshatra/pada are visible and mathematically consistent.
3. English mode shows English graha names throughout; Hindi uses Devanagari; Hinglish is consistent Roman Hinglish by default.
4. Language switching changes all output prose without changing raw longitude or house IDs.
5. User can switch between North and South chart views; table matches both.
6. User sees individual explanation for each of 12 houses and each graha.
7. Career, love, marriage and growth each have independent, meaningful, placement-linked interpretation with source factors.
8. Report explicitly distinguishes math results vs cultural interpretation; no certain future claims.
9. Current Mahadasha displays correctly with declared approximation settings.
10. Full selected-language PDF/report and JSON export are available, with Devanagari rendered correctly.
11. Site works at 360px width, keyboard and screen-reader navigation; clear error messages.
12. Tests pass; release checklist completed separately before going public.

## Definition of done per phase

For each phase Antigravity should output: changed file names, a short screenshot/preview description (actual browser evidence if available), new/updated test list and result, known limitations, and **only then** the next phase proposal. Report failures rather than claiming success.
