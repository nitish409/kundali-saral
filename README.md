# Kundali Saral ✦ | कुंडली सरल

A **three-language Vedic Kundali web application** (**English**, **Hinglish**, and **Hindi**) designed for people who find traditional online birth charts hard to understand.

The app calculates a sidereal natal chart from birth date, local time, birthplace coordinates, and historical IANA timezone rules, then explains the chart in clear, beginner-friendly language.

## Features

- **Three full locales**:
  - **English (`en`)**: Plain English throughout (`Sun`, `Moon`, `Mars`, etc.)
  - **Hinglish (`hinglish`)**: Conversational Roman-script Hinglish (`Surya`, `Chandra`, `Mangal`, etc.) with an optional toggle to display Devanagari names in brackets
  - **Hindi (`hi`)**: Natural Devanagari Hindi (`सूर्य`, `चंद्र`, `मंगल`, etc.)
- **Real offline celestial calculations** using PySwissEph's Moshier ephemeris (no AI-generated planetary positions)
- **Dual D1 Rashi chart views**:
  - **South Indian** fixed-sign chart
  - **North Indian** fixed-house diamond chart
  - **Side-by-side comparison** and interactive keyboard/click inspector for all 12 houses and 9 grahas
- **5 Summary Dashboard Tiles**: Ascendant (Lagna), Moon Sign, Sidereal Sun Sign, Birth Nakshatra & Pada, and Current Mahadasha
- **17 Independent Life Sections** grouped into 5 categories (`Myself & Identity`, `Career, Leadership & Study`, `Love, Marriage & Community`, `Money, Family & Home`, `Wellbeing, Travel & Growth`):
  - Separates **Calculated Chart Facts** from **Traditional Parashari Interpretation**
  - Includes explicit **Rule IDs**, **Why These Factors?**, **Potential Strengths**, **Balance / Growth Edge**, and **Practical Reflection Questions**
- **Birth-Time & Timezone Validation**:
  - Historical IANA timezone conversion to UTC
  - Rejects nonexistent daylight-saving spring-forward gap times
  - Detects and disambiguates repeated daylight-saving fallback hours (`dst_fold=0` vs `dst_fold=1`)
  - Birth-time uncertainty toggle with clear warnings on Ascendant/house sensitivity
- **58 built-in offline cities**, manual latitude/longitude/IANA timezone entry, and optional rate-limited geocoding lookup
- **Privacy-aware Export**: Print / Save as multi-page PDF and JSON export, with an option to hide the user's name (`Anonymous`)

## Run Locally

Requires **Python 3.11** (recommended on Windows for prebuilt `pyswisseph` binary wheels) or **Python 3.11–3.13** on Linux/macOS.

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

### Windows (PowerShell)

```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn main:app --reload
```



### Run Tests

```bash
python -m pip install pytest httpx
python -m pytest -q
```

### Docker

```bash
docker build -t kundali-saral .
docker run -p 8000:8000 kundali-saral
```

Open **https://kundali-saral.vercel.app/**.

## Calculation Methodology

| Component | Implementation |
| --- | --- |
| Zodiac | Sidereal, Lahiri ayanamsa |
| Houses | Whole-sign houses from Ascendant sign |
| Classical Planets | Sun, Moon, Mars, Mercury, Jupiter, Venus, Saturn |
| Lunar Nodes | Mean Rahu; Ketu exactly 180° opposite |
| Ephemeris | Swiss Ephemeris Moshier (offline) |
| Birth Timezone | Python `zoneinfo` + `tzdata`, local birth time converted to UTC with DST gap & overlap checks |
| Nakshatra & Pada | 27 equal nakshatras (13°20′ each), 4 padas each (3°20′), with Vimshottari rulers |
| Dashas | Approximate 120-year Vimshottari Mahadasha cycle (365.2425 days/year) |
| Aspects & Dignities | Traditional Parashari whole-sign Drishti and sign-level dignities |

## Project Structure

```text
kundali-saral/
├── static/
│   ├── index.html                    # Responsive UI
│   ├── styles.css                    # Visual & print styles
│   └── app.js                        # Localization, North/South charts, inspector, exports
├── tests/
│   ├── test_app.py                   # API, localization, DST & concurrency tests
│   └── test_language_math_parity.py  # Locale math parity & 12-Lagna rotation tests
├── astrology.py                      # Ephemeris math, houses, nakshatras, dashas
├── interpretations.py                # 17 life readings, house/planet guides, glossary
├── cities.py                         # Offline birthplace presets
├── main.py                           # FastAPI endpoints + static file server
├── requirements.txt
├── Dockerfile
└── LICENSE_NOTICE.md                 # Pre-publication licensing notice
```

## Privacy & Responsibility

- No registration, tracking pixels, or database storage. Birth details are processed transiently in memory.
- Astrology is presented as a cultural and spiritual interpretive tradition for self-reflection, not scientifically established prediction. Never use this report in place of professional medical, legal, financial, or mental-health guidance.

## Licensing

Calculations use `pyswisseph` / Swiss Ephemeris. Review [`LICENSE_NOTICE.md`](LICENSE_NOTICE.md) for GNU AGPL v3 or Swiss Ephemeris Professional License obligations before deploying a public network service.
