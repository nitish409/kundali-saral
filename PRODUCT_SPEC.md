> **2026 upgrade note:** This original MVP specification describes existing behavior. For the expanded Antigravity build (full 3-language support, Romanized Hinglish target, North Indian D1, richer 17-topic report backlog), see `FEATURE_MASTER_LIST.md`, `LANGUAGE_SYSTEM.md`, `CALCULATION_AND_DATA_DESIGN.md`, `IMPLEMENTATION_ROADMAP.md`, and `ANTIGRAVITY_PROMPT.md`. Not-yet-built items are a roadmap, not current features.

# Kundali Saral — Product requirements (PRD)

## 1. Audience & unique value

**Who**: People who want a Vedic birth-chart experience without technical astrological jargon; users who prefer English, Hinglish or Hindi; first-time readers on a phone.

**Problem**: Traditional Kundali websites show complex charts and long, unclear texts; many fail to translate planet names and don't separate the actual chart placement from interpretations.

**Promise**: “Samajhne wali Kundali” — a clear, transparent educational birth chart that feels personal without making fate claims.

## 2. User journey

Landing page → select language → enter birth date, exact local time, birth city → verify location/timezone → generate → see 3 summary tiles → view sign/house Kundali → navigate section by section → review the traditional dasha timeline → print/save PDF / export own JSON.

### Essential inputs
- DOB, exact local birth time, city or lat+lon, IANA timezone
- Optional display name
- No religion, caste, sex, email, phone or registration needed
- Warn if time is uncertain; use timezone disambiguation for DST overlaps in v2

## 3. Supported languages

| Area | English | Hinglish | Hindi |
| --- | --- | --- | --- |
| Body | Plain English | Roman Hindi + familiar English words | Devanagari Hindi |
| Graha names | Sun/Moon/Mars/... | सूर्य/चंद्र/मंगल/बुध/गुरु/शुक्र/शनि/राहु/केतु | सूर्य/चंद्र/मंगल/बुध/गुरु/शुक्र/शनि/राहु/केतु |
| Rashis | Aries, Taurus etc | Mesh, Vrishabh, etc | मेष, वृषभ etc |
| Section headings | Simple English | Casual Hinglish | Simple Hindi |
| All calculations | Identical astronomical results for the same birth inputs, only language changes |

## 4. Report sections

1. **Overview & Lagna** — Lagna, Moon rashi, Sun rashi, nakshatra/pada, how to read chart.
2. **Kundali chart** — currently South Indian (fixed-sign) and readable full planet table; planned North Indian (fixed-house) view.
3. **Personality & strengths** — houses 1 and 3; how self/effort themes are traditionally read.
4. **Career & work** — 10 and 6; traditional work/public life themes; NEVER a guaranteed job or career result.
5. **Love & relationships** — 5 and 7; romance, respect and mutuality; no guaranteed partner/soulmate claims.
6. **Marriage & partnership** — 7 and 2; commitment themes; no marriage date or partner gender assumptions.
7. **Money & savings** — 2 and 11; resource/network themes; never a stock/return prediction.
8. **Education & learning** — 5 and 9; learning/mentor themes.
9. **Family & home** — 4 and 2; rootedness and family conversations.
10. **Wellbeing & routine** — 6 and 1; practical routines, no medical diagnosis.
11. **Personal growth** — 9 and 12; life philosophy/reflection.
12. **Vimshottari Mahadasha** — approximate traditional periods with current cycle highlighted.
13. **Methodology & limitations** — detailed chart model, uncertainty and license.

All topic sections show directly derived birth-chart **facts**, then clearly labeled **traditional explanations**, and one constructive reflection question.

## 5. Technical architecture

| Layer | MVP implementation | Scale-up option |
| --- | --- | --- |
| Web UI | Vanilla HTML, CSS, JavaScript (no bundler) | React/Next.js with i18n + tested components, if justified |
| API | FastAPI Python | Stateless FastAPI with job queue only if needed |
| Calculation | PySwissEph Moshier, sidereal Lahiri | Audit Swiss ephemeris file support and licensed usage |
| Location | 28 built-in locations + optional configured geocoder, manual lat/lon and TZ | Licensed geocoding + historical timezone resolver + large place database |
| Storage | None for births | Optional encrypted consent-based storage with deletion and retention policy |
| Hosting | Docker-capable VM/platform | Managed production stack after licensing/privacy review |

## 6. Acceptance tests

- Valid birth chart returns exactly nine grahas, twelve houses, one lagna and valid nakshatra/pada.
- Rahu-Ketu oppose by 180°; house mapping changes correctly with Lagna.
- Same details yield identical longitudes regardless of text language.
- Historical timezone conversion works; reject impossible DST times.
- Language switch changes all readings and Hindi/Hinglish graha names; no English planet names slip into topic readings.
- Mobile inputs, chart, table, navigation, print stylesheet are usable.
- No birth chart POST stores personal details in the app database (none exists).
- Avoid hallucinated certainties and unsubstantiated predictions.

## 7. Roadmap

**Phase 1 — in this ZIP:** full beginner MVP, 9 thematic sections, localized chart, demo, API, tests, downloads.

**Phase 2 — credibility & UX:** North Indian chart, stronger rule coverage with expert validation, verified Devanagari translations, accurate DST ambiguity handling, extensive astronomical regression tests, accessible mobile report, designed PDF.

**Phase 3 — optional premium:** charts stored only with opt-in and deletion, improved international geocoding, consent-based compatibility, comprehensive dashas and divisional charts after expert review, optional explanations of Yogas/Doshas with balanced tone, user account and payment only when core product is trustworthy.

## 8. Production launch checklist

- [ ] Swiss Ephemeris AGPL/professional licensing decision + required attribution and source disclosures
- [ ] Document user privacy and retention / no-storage claims for actual hosting provider
- [ ] HTTPS + secure headers, rate limiting, request size caps
- [ ] City search compliant with provider policy, attribution and timezones
- [ ] Expert validation of astrological conventions, nakshatra/dasha and 3-language text
- [ ] Tests for borders/cusp cases/timezones, concurrency, mobile browser and PDF
- [ ] SEO/title/social preview, accessibility, analytics only with consent
- [ ] Domain + actual public deployment and monitoring

