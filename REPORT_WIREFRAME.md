# What the finished Kundali report should look like

This is a **wireframe/content template**, NOT an actual horoscope. Bracketed items must be replaced with verified output calculated from the user's birth details. Never fabricate data or use generic claims as if they came from the chart.

## Page 1: Introduction

**Your Kundali / Aapki Janam Kundali / आपकी जन्म कुंडली**

- Name: `[optional name or Anonymous]`
- Born: `[local birth date and birth time, uncertainty indicator]`
- Location: `[selected birth city/country, lat, lon, timezone]`
- Language: `[English / Hinglish / Hindi]`
- Most important summary cards: `[Lagna]`, `[Moon sign]`, `[Sun sign]`, `[Nakshatra and pada]`, `[current Mahadasha]`
- A short explanation of how a Jyotish chart is read and how birth time changes Lagna.

## Pages 2–3: Chart pages

- North Indian D1 with clear house numbers, graha names and Lagna.
- South Indian D1 with clearly labeled signs, house numbers and Lagna.
- Accessible plain table for all 12 houses and nine grahas.
- Every graha table row: `[name] [degree°′] [rashi] [house] [retrograde?] [nakshatra/pada if computed]`.
- D9 should only appear when implemented, independently verified and labeled.

## Page 4: Planet & house literacy

- 9 grahas, including the explanation that Rahu/Ketu are lunar nodes.
- 12 houses each with `[birth-chart sign] [lord] [house position of lord] [occupants]`.
- One-line meanings in exactly the chosen language.

## Pages 5–10: Life themes (repeat a compact card for each section)

### `[Section: Career / Love / Marriage / Personal growth / ...]`

- **Chart facts:** “House `[H]` is in `[Rashi]`; its lord `[Graha]` is in House `[X]`; `[Grahas]` occupy the house.”
- **Why these factors?** Short explanation of tradition-specific choice.
- **Traditional interpretation:** Balanced plain-language reading tied to the actual placements.
- **Potential strength:** A non-deterministic area for self-reflection.
- **Potential challenge:** A manageable trade-off or question, never a frightening certainty.
- **Reflect:** Practical, constructive question or action.
- **Method / rule ID:** `[rule reference and version]`.

Keep separate reports for: personality, career, entrepreneurship, learning, love, marriage, friendships, money, family, nurturing, wellbeing, emotional resilience, creativity, travel, beliefs, leadership and growth. Group on-screen but retain navigation/search.

## Page 11: Timing and cycles

- Traditional Vimshottari Mahadasha timeline: ruler, birth balance, periods, current period and calculations convention.
- Antardasha/other timing only if reviewed and actually calculated.
- Do not claim certainty of marriage dates, job offers, recovery from illness, investments, travel or life events.

## Last page: Your method and privacy

- Sidereal zodiac, Lahiri ayanamsa, whole-sign house mapping, mean nodes, Moshier ephemeris, dasha-year convention, time-zone data details.
- “Calculated placements” vs “traditional interpretation” split.
- Birth-time accuracy limitation and possible differences between traditions/providers.
- Report generated on `[local date]` with computation/rules release ID.
- Privacy: was this chart persisted? If yes, where and for how long? If none, explicitly say no application database storage.
- Clear educational disclaimer: astrology is a cultural/spiritual tradition and not scientifically established as a prediction method; not professional medical, financial or legal advice.

## PDF quality checklist

- [ ] All captions and paragraphs in one selected language.
- [ ] English names don't unexpectedly appear in Hindi graha table; Hinglish remains readable Roman-script.
- [ ] Fonts support Hindi including conjuncts; no tofu glyphs.
- [ ] Chart lines and planet labels aren't clipped or overcrowded.
- [ ] Page numbers, section navigation, readable print colors and table headings.
- [ ] No birth name, address or sensitive details added without input/consent.
