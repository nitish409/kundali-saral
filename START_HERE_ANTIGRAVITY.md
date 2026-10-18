# START HERE — Build Kundali Saral in Google Antigravity

**Your existing code is included. This is an upgrade kit, not just a concept description.**

## What to open or upload

Use the **extracted `kundali-saral/` folder**, which contains the source code AND the new instructions. Do not upload just the Markdown prompt while leaving the Python application behind. Google Antigravity's current Project workflow associates a local folder/repository with an agent.

**Files that matter:**
- `ANTIGRAVITY_PROMPT.md`: paste into agent chat — the main build instruction.
- `AGENTS.md`: persistent rules for anyone editing this code.
- `PRODUCT_SPEC.md`: original requirements; `FEATURE_MASTER_LIST.md`: expanded feature catalogue.
- `LANGUAGE_SYSTEM.md`: exact English/Hinglish/Hindi language behaviour and terminology.
- `CALCULATION_AND_DATA_DESIGN.md`: astronomy rules, API and privacy architecture.
- `IMPLEMENTATION_ROADMAP.md`: build stages and measurable acceptance tests.
- `REPORT_WIREFRAME.md`: what every final Kundali report must contain.
- `LICENSE_NOTICE.md`: licensing before going public.
- `main.py`, `astrology.py`, `interpretations.py`, `cities.py`, `static/`, `tests/`: **existing application**. Preserve and improve, don't discard.

## Google Antigravity steps

1. Extract this ZIP into a local folder called `kundali-saral`.
2. Install/open Google Antigravity: https://antigravity.google/download
3. In the app, choose **New Project** (folder + icon), **Add Folder**, choose extracted `kundali-saral`, then **Create**.
4. Start an agent in **Local mode** for edits to your current project, or **New worktree mode** if you prefer isolated changes.
5. Open `ANTIGRAVITY_PROMPT.md`, copy its contents into agent chat, and ask the agent to start at Phase 0, then implement the highest-priority changes stage by stage.
6. Check the implementation plan, diffs and test results. Ask to preview on both mobile and desktop before publishing.

Official Google steps: https://antigravity.google/docs/getting-started

## Run locally

Use **Python 3.11, 3.12, or 3.13**, from the project folder. Commands below are for a terminal where `python` refers to the correct interpreter.

```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pip install pytest httpx
python -m pytest -q
uvicorn main:app --reload
```

Visit **http://127.0.0.1:8000**; click **Try a sample chart**. If `python` is unavailable on Windows, try `py`.

Verified on the supplied project in this environment: `python -m pytest -q` yielded **6 passing tests** before any Antigravity modifications. This does NOT prove all astrological rules are audited or all deployment cases are safe.

## Exact language expectation

- **English**: readable English everywhere; Sun, Moon, Mars, etc.
- **Hinglish**: mostly Roman-script conversational Hindi + English; Surya/Chandra/Mangal, optionally show familiar Hindi spellings in tooltips. Do **not** mix random English-only reports or unexplained Devanagari into Hinglish sentences.
- **Hindi**: natural Devanagari Hindi throughout; सूर्य/चंद्र/मंगल, etc.
- Current starter uses Devanagari planet names in Hinglish. **The agent should standardize it as described in `LANGUAGE_SYSTEM.md`**; no change to celestial calculations.

## What's real today vs still to build

**Implemented starter:** Lahiri sidereal D1 calculations, whole sign houses, nine grahas, 27 nakshatras/pada, South Indian display, approximate Mahadasha, nine beginner topics, print-to-PDF and JSON export, basic cities, tests.

**Not implemented or not audited:** North Indian D1 renderer, D9 and other divisional charts, verified yogas/doshas/aspects/dignities, Antardasha, transits, advanced compatibility, proper PDF layout, broad city search, production accessibility/security, professional interpretation review.

Do not let an agent advertise those missing features as working until coded, tested and reviewed.

## Publishing and safety

Antigravity edits code; opening a project **does not automatically deploy it publicly**. A hosting platform, domain, HTTPS, privacy review and third-party licensing review are separate launch steps. The installed `pyswisseph` package is AGPL-licensed; the Swiss Ephemeris engine has AGPL/professional licensing options. Read `LICENSE_NOTICE.md` before launching a public network service.
