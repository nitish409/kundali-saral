> **Antigravity upgrade kit:** Start with [`START_HERE_ANTIGRAVITY.md`](START_HERE_ANTIGRAVITY.md) and paste [`ANTIGRAVITY_PROMPT.md`](ANTIGRAVITY_PROMPT.md) into the agent. Extra files describe planned improvements, **not features already built**. The new locale target is Roman-script Hinglish, while the starter currently shows Hindi-script graha names in Hinglish.

# Kundali Saral ✦ | कुंडली सरल

A working **three-language Vedic Kundali web app starter** for people who find traditional online birth charts hard to understand. This is a usable **MVP (first version)**, not a fully audited commercial astrology platform.

The app calculates a sidereal natal chart from date, time, birthplace coordinates and historical IANA timezone rules. It then explains the chart in **English**, **Hinglish**, and **Hindi**, including **Hindi-script graha names in both Hinglish and Hindi**.

## Ready now

- Beautiful, mobile-friendly website and birth details form
- English / Hinglish / Hindi switching (all nine topic explanations follow the selected language)
- Graha names: सूर्य, चंद्र, मंगल, बुध, गुरु, शुक्र, शनि, राहु, केतु in both Hindi/Hinglish
- Real offline celestial calculations from PySwissEph's Moshier ephemeris, not made-up placements
- Lahiri sidereal zodiac; whole-sign houses; South Indian fixed-sign visual chart
- Lagna, Moon rashi, Sun rashi, nakshatra, nakshatra pada, 9 grahas, 12 houses, house lords and basic retrograde status
- 9 clear readings: **personality, career, love, marriage, money, education, family, health/wellbeing and personal growth**
- Each reading displays chart facts separately from traditional interpretations, plus a practical reflection question
- Approximate Vimshottari Mahadasha timeline
- 28 preset birth locations, manual latitude/longitude/timezone, optional search for additional places
- Demo button, JSON export, browser Print / Save PDF
- FastAPI API documentation at `/api/docs`, test suite, Dockerfile, no account required

## Open it in Google Antigravity

1. **Extract** `kundali-saral.zip` into a folder on your computer.
2. Open [Google Antigravity](https://antigravity.google/).
3. Click **New Project** (folder with a + icon) → **Add Folder** → choose the extracted `kundali-saral` folder → **Create**.
4. Open `ANTIGRAVITY_PROMPT.md`, **copy the prompt** from that file into Antigravity's agent chat. Tell the agent to **inspect existing files and improve them; do not replace the working backend with a fake chart**.
5. Follow the run steps below. Antigravity can edit files, run tests and help prepare hosting.

> Antigravity is a development tool; the project folder must also be hosted on a server before everyone can open your app via a public URL. Adding the folder alone does **not** publish the website.

## Run locally

You need **Python 3.11–3.13**. Open a terminal inside the extracted `kundali-saral` folder.

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

### Windows (PowerShell)

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

Open **http://127.0.0.1:8000** and click **Try a sample chart**.

To run automated tests:

```bash
python -m pip install pytest httpx
python -m pytest -q
```

### Docker

```bash
docker build -t kundali-saral .
docker run -p 8000:8000 kundali-saral
```

Open http://localhost:8000.

## Using a different birth city

Popular sample cities are provided offline. For a city not in the list:

1. Type the city and see if it matches a local suggestion.
2. If no suggestion appears, use **Advanced: coordinates & timezone** and enter the birthplace latitude, longitude and **IANA timezone** (for example `Asia/Kolkata`, `Europe/London`, or `America/New_York`).
3. Optional: configure an approved place-search provider. An opt-in prototype OpenStreetMap Nominatim implementation exists but is **disabled by default**. Set environment variable `NOMINATIM_USER_AGENT` to an identifying app name plus a real operator contact, and only enable it after you read [Nominatim's usage policy](https://operations.osmfoundation.org/policies/nominatim/). Search occurs **only when the visitor clicks “Find place”**; no automatic public-API autocomplete. The shared public service is not appropriate for a high-traffic launch: swap to a contracted geocoding provider or your own deployment, with caching, quotas, accurate timezone lookup, and attribution.

## Important calculation details

| Component | This version |
| --- | --- |
| Zodiac | Sidereal, Lahiri ayanamsa |
| Houses | Whole-sign by ascendant sign |
| Planets | Sun, Moon, Mars, Mercury, Jupiter, Venus, Saturn |
| Nodes | Mean Rahu; Ketu exactly 180° opposite |
| Ephemeris | Swiss Ephemeris Moshier (no external data files) |
| Birth timezone | Python `zoneinfo`, local birth time converted to UTC; invalid DST-gap times rejected |
| Nakshatra/pada | 27 equal nakshatras, 4 padas each, from Moon longitude |
| Dashas | Approximate 120-year Vimshottari cycle, fractional birth balance, 365.2425 days/year |
| Interpretations | Explicit, deterministic, rule-based educational text, not AI-synthesized predictions |

**Birth time accuracy is important.** A slight error can change the ascendant, especially near a sign boundary. Birthplace must be the place of birth, *not* the current home. Daylight-saving ambiguity during repeated local time hours is not yet separately resolved. This version intentionally does **not** assert Manglik Dosha, Ashtakoota scores, yogas, divisional charts, remedies, precise marriage timelines or verified professional predictions. Those require separately reviewed domain logic.

## Files

```text
kundali-saral/
├── static/
│   ├── index.html       # Responsive UI
│   ├── styles.css       # All visual styles
│   └── app.js           # Forms, localization, charts, exports
├── tests/test_app.py    # Backend API and calculation checks
├── astrology.py         # Chart math and Mahadasha calculations
├── interpretations.py   # 9 accessible readings in 3 languages
├── cities.py            # Offline birthplace presets
├── main.py              # FastAPI endpoints + website server
├── requirements.txt
├── Dockerfile
├── ANTIGRAVITY_PROMPT.md # Copy-paste instructions for the Antigravity agent
├── PRODUCT_SPEC.md      # Full product requirements and roadmap
└── LICENSE_NOTICE.md   # Mandatory pre-publication licensing guidance
```

## Privacy & responsibility

- No registration, tracking pixels or database. POSTed birth details are processed in memory; check infrastructure request logging and provider rules before publishing.
- The browser can download a JSON copy; standard browser Print → Save as PDF works without installing a PDF engine.
- For a production service add HTTPS, structured privacy/retention policy, abuse controls, security review, monitoring, backups as needed and user consent for storing other people's details.
- Astrology should be presented as a cultural/spiritual tradition, not scientifically proven fate. It must not substitute for professional medical, legal or financial guidance.

## Licensing — read before putting this website online

The calculations use `pyswisseph` / Swiss Ephemeris. **Swiss Ephemeris has AGPL or professional/commercial licensing obligations**. Read `LICENSE_NOTICE.md`. Decide which license model applies **before distributing or activating a public service**, and follow all attribution/source publication terms or obtain the relevant professional license. This repository includes original application files, **not** a paid license or permission to bypass third-party licensing.

## Build next

See `PRODUCT_SPEC.md` for the expansion plan (North Indian chart, downloadable designed PDF reports, verified traditional calculations, accessibility, accounts with opt-in retention, certified translations, hosting, monitoring).
