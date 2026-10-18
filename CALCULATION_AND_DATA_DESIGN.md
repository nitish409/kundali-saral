# Technical and calculation design — enforce before advanced features

## Baseline: what this repository currently computes

- Python FastAPI: `main.py`; browser: `static/index.html`, `app.js`, `styles.css`.
- Computation: `astrology.py` uses installed `pyswisseph`, Moshier ephemeris, **sidereal Lahiri**, geocentric longitudes, **mean Rahu** + Ketu 180° away, 12 whole-sign houses based on the sidereal ascendant.
- The birth city's geographical coordinates and **IANA time zone** convert local wall time to UTC via Python `zoneinfo`; the code rejects DST-gap times but does not yet disambiguate repeated-hour overlaps.
- Moon longitude determines Nakshatra/quarter and an *approximate* Vimshottari Mahadasha timeline (365.2425-day years). These are tradition-dependent calculations; label conventions.
- Nine topic explanations are heuristic deterministic rule-based text. They are not fully reviewed Jyotish readings.

## Scientific reproducibility versus interpretive traditions

**Astronomy**: calculated Julian day, observer coordinates, sidereal body longitudes, movement direction. Have tests against independent reference ephemeris examples and stable inputs.

**Jyotish rules**: ayanamsa, house system, which Rahu node, which drishti/yoga definition, Dasha year length, Varga algorithm and interpretation school. Display the settings, version them and avoid silently changing them between releases.

**Interpretations**: cite actual placements and deterministic rule IDs. If confidence means strength of a rule match, describe it as coverage/review status, NOT a probability that a future event will occur.

## Backend suggestions

Keep FastAPI/Python and test it. Split future growth into `core/ephemeris.py`, `core/charts.py`, `core/dashas.py`, `core/divisional.py`, `core/rules.py`, `i18n/`, `tests/` only when needed; don't rewrite the functioning app in one pass.

Prefer this clean separation:

1. `birth_input` -> validated local date/time, place lat/lon and IANA time zone, DST overlap selection.
2. `natal_math` -> immutable, locale-independent JSON with stable planet IDs, sign IDs, houses and raw longitude + calculation version.
3. `tradition_rules` -> rule IDs and factors applied to this chart; do not make up placements.
4. `report_sections` -> structured report content: `facts`, `interpretation`, `possible_strengths`, `possible_challenges`, `reflection`, `disclaimer`, `sources`.
5. `localization` -> translate labels/rule content for the selected locale; all report exports use this same source.
6. `renderers` -> North and South Indian charts + table, mobile cards, printable/PDF report.

Proposed stable API contract (illustrative only; **not already implemented**):

```json
{
  "meta": {
    "calculation_version": "1.0",
    "locale": "en",
    "zodiac": "sidereal",
    "ayanamsa": "lahiri",
    "house_system": "whole_sign",
    "node_mode": "mean_rahu",
    "ephemeris": "moshier",
    "dasha_year_convention": "365.2425_days"
  },
  "birth": {"local_time": "1998-08-15T08:30:00", "time_zone": "Asia/Kolkata", "latitude": 28.6139, "longitude": 77.209},
  "chart": {
    "ascendant": {"longitude": null, "sign_index": null},
    "planets": [{"id": "sun", "longitude": null, "sign_index": null, "house": null}],
    "houses": [],
    "nakshatra": {"index": null, "pada": null},
    "dashas": []
  },
  "report": [{"section_id": "career", "rule_ids": [], "facts": [], "interpretation": [], "reflection": ""}]
}
```

`null` above marks **illustrative schema values**, not actual planetary calculations. The real API response must come from the ephemeris.

## Accuracy and edge-case checklist

- Validate date/time parsing and calendar policies; reject future birth dates when used as a natal app if appropriate, or clearly define intended historical range.
- DST **nonexistent** local times: error; DST **ambiguous** repeated local times: ask user which UTC offset, do not silently pick `fold=0`.
- Historical time zones and city changes, fractional offsets and southern hemisphere places.
- Asynchronous or concurrent requests: avoid shared mutable ephemeris settings that can make two charts interfere; test or serialize if binding is not thread-safe.
- Normalize longitudes to `[0,360)`; zodiac sign boundaries at exact multiples of 30°; nakshatra boundaries at 13°20′; D9 boundaries at 3°20′.
- Round **only at display boundary**, not before deriving signs, padas, divisional placements, dashas or interpretations.
- Confirm sidereal ascendant calculation, high-latitude exceptions and coordinate direction (negative west/south).
- Rahu and Ketu must be opposite by exactly 180° in selected node model; do not label lunar nodes physical planets.
- Retrograde display: meaning of node retrograde and motion for fast bodies; use ephemeris velocities.
- Distinguish local civil date versus date in UTC and exact instant; never calculate natal chart from current location.
- Dasha birth fraction check, first ruler sequence, transition boundaries, leap years and inclusive/exclusive dates. Method must be visible.
- D9 Navamsa algorithm and North Indian/South Indian geometry require reference test cases, not visual guessing.
- Cross-check at least 20 independently sourced birth examples across signs, timezones and languages; document version/inputs/reference screenshots or numbers and allowable differences.
- Regression tests must be offline/deterministic, no external geocode API during tests, no invented fixed results.

## Geocoding and privacy

- The current starter has a small curated location list and optional user-triggered public Nominatim calls. Do NOT turn the OSM Foundation's shared Nominatim API into autocomplete; it expressly prohibits that usage. For real traffic, choose a compliant licensed geocoder or self-host and provide attribution, caching and rate limits.
- A geocoder supplies coordinates, but a robust system must verify the historical IANA time zone separately (especially border locations).
- No personal charts written to a database by default. Do not log full birth input, names or precise chart content into analytics/exception reports. Set retention policies if accounts are introduced.
- Obtain consent before sharing another person's birth data, partner matching, external AI reports, email sends or public share links.

## API, security, performance, deployment

- API POST `/api/chart` remains supported or gets a versioned compatibility adapter.
- Validate size, length, Unicode name, lat/lon, valid time zone, allowed years, locale enumeration, and request rate.
- Add tests for injection/XSS and safe HTML rendering, malicious locale payloads, oversize inputs and logging privacy.
- Production: HTTPS, CORS restricted, security headers, dependency pinning/lockfiles, CI, observability with private-field redaction, secrets in environment/secret manager, privacy/terms and opt-in persistence controls.
- Docker builds can be deployed to Python-capable infrastructure; Antigravity itself is a development environment, not the production host.
- Open-source/commercial license decision for `pyswisseph` and the underlying Swiss Ephemeris is required **before** operating a public service. Read `LICENSE_NOTICE.md` and official sources.

## Suggested future UI implementation structure

```text
static/
  components/   # optional component modules if site grows
  i18n/         # en.json, hinglish.json, hi.json; locale-neutral stable keys
  charts/       # chart SVG+accessible table view
  print.css     # PDFs/printing layouts, if necessary
```

One codebase, one actual chart engine, many renderers/locales. Keep the existing site functioning while improving it.
