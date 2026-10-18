# Kundali Saral — Complete feature catalogue

This is a **feature backlog**, NOT a claim that all features already work. Priority: P0 must-have, P1 valuable next, P2 advanced and only after domain review. The app uses **traditional Jyotish interpretation**, not scientifically validated predictive ability. Every result should show its calculation basis and uncertainty.

## A. Core user journey — P0

- Responsive SEO-friendly landing page explaining the product, chart methodology, three languages, privacy and caveats.
- Language choice (English / Hinglish / Hindi) before entering details; retain in report and export.
- Birth form: optional name, YYYY-MM-DD date, precise local 12/24-hour time, city/country suggestion, verified coordinates and time zone, uncertain-time toggle, daylight-saving overlap disambiguation.
- Birthplace must be birthplace **at birth**, not current location; account for historical UTC offsets.
- Generate birth chart with real math; clear errors on impossible times, invalid location, out-of-range birth year or missing city.
- Explain what accurate/approximate birth time means: if time uncertain, mark ascendant/houses as potentially inaccurate; never silently show them as certain.
- Dashboard cards: Lagna, Moon sign, Sun sign, Nakshatra and pada, current Mahadasha, primary strengths/themes (interpretive).
- Detailed 12-house interactive chart; desktop and mobile; text-based table fallback; accessible legends and keyboard navigation.
- Menu to access each life section. Show same data in all three locales.
- User-owned export as JSON and professionally styled downloadable/printable PDF, with each output displaying method and locale.
- No login or tracking required to calculate; explicit permission needed for saving charts.

## B. Charts, planet tables and calculations

| Feature | Priority | Requirements |
| --- | --- | --- |
| D1 Rashi (birth) chart | P0 | North Indian diamond and South Indian fixed-sign views, same underlying house/sign mapping |
| All 9 grahas | P0 | Sun/Moon/Mars/Mercury/Jupiter/Venus/Saturn/Rahu/Ketu with stable keys + localized names |
| 12 Rashis and houses | P0 | Sign, degree, ascendant degree, house ruler, house lord location, occupants |
| Longitudes and nakshatra | P0 | Degrees/minutes, Nakshatra, Pada, Nakshatra lord; clear precision/rounding |
| Speed/retrograde | P0 | Where meaningful, calculated from ephemeris; Rahu/Ketu mean/true setting disclosed |
| Dasha | P0 basic / P1 refined | Mahadasha first; verified Antardasha and Pratyantardasha only after review; identify birth balance, current period and time convention |
| Graha aspects / drishti | P1 | Declare Parashari or another tradition; mathematical positions, display contributing aspects |
| Dignities / avasthas | P1 | Exaltation, debilitation, own sign, combustion (if reviewed) with formula + references |
| D9 Navamsa | P1 | Correct longitude-to-varga mapping, native chart renderer, reference tests |
| Other Vargas | P2 | D10 career, D7 children, D12 parents, etc., only with explicit domain formulas |
| Yogas | P2 | Each yoga rule explicitly defined and validated; avoid blanket good/bad labels |
| Doshas | P2 | Manglik, Kaal Sarp etc. only when exact school of interpretation and known exceptions are explicit; do not induce fear |
| Transits / Gochar | P2 | Date-based ephemeris positions, not fabricated; distinguish natal and transit charts |
| Panchang | P2 | Tithi, Vara, Nakshatra, Yoga, Karana with correct sunrise/place convention |
| Matching / Ashtakoota | P2 | Two-person explicit consent, 8 factor scores, tradition method, cultural caveat; compatibility is not relationship fate |

## C. The life report: 17 independent sections

Each section needs: **why these houses/grahas**, relevant **actual birth placements**, plain-language **traditional interpretation**, **possible strengths**, **possible challenges**, **practical reflection**, disclaimer on uncertainty, and no fear-based tone.

| Section / tabs | Typical factors to review (tradition-dependent; non-exhaustive) | Suggested coverage |
| --- | --- | --- |
| 1. Personality & identity | Lagna, Lagna lord, 1st house, Moon | Temperament themes, motivation, self-expression, strengths, growth edges |
| 2. Career & profession | 10th/6th/2nd/11th, house lords, D10 when validated | Work style, skills, collaboration, visibility, career transitions as open-ended themes |
| 3. Business & entrepreneurship | 7th/10th/11th/3rd | Independence, partnerships, risk reflection, teamwork; not financial promises |
| 4. Education & examinations | 4th/5th/9th, Mercury/Jupiter | Learning preferences, focus, mentoring, practical study habits; no score guarantee |
| 5. Love & dating | 5th/7th, Venus/Moon | Communication, attachment themes, respect, boundaries; no soulmate certainty |
| 6. Marriage & partnership | 7th/2nd, Venus/Jupiter per chosen tradition | Shared values, communication and partnership patterns; never fixed marriage age/date |
| 7. Friends & social life | 3rd/11th | Peer networks, social support, belonging, cooperation |
| 8. Money & budgeting | 2nd/11th/6th | Spending habits and planning prompts; no earnings, profits or stock recommendations |
| 9. Home, family & parents | 4th/2nd/9th | Home stability, relatives, care and belonging; respect cultural diversity |
| 10. Children & nurturing | 5th | Parenting/nurturing themes only; never fertility or pregnancy predictions |
| 11. Health & wellbeing | 1st/6th | Work-life balance, healthy routines only; no diagnoses or treatment claims |
| 12. Emotional resilience | Moon, 4th, 12th | Emotional reflection without mental health diagnosis or labels |
| 13. Creativity & interests | 5th/3rd, Venus/Mercury | Creative expression, hobbies, communications |
| 14. Travel & relocation | 3rd/9th/12th | Curiosity, mobility symbolism, planning questions, no relocation guarantees |
| 15. Spirituality & beliefs | 9th/12th, Jupiter | Values, reflection and meaning; never assume the user's religion |
| 16. Leadership & public image | 10th/1st/11th, Sun/Saturn | Responsibility, reputation, collaboration, social participation |
| 17. Personal growth & habits | Lagna lord, 3rd/6th/9th | Self-improvement questions, choices within user's control |

**Important:** The current code includes 9 beginner topics. The table above is a new feature checklist; many topics overlap and can be grouped to avoid a 17-tab cluttered interface. A user-facing organization could be: `Myself`, `Career & Study`, `Relationships`, `Money & Home`, `Wellbeing & Growth`, `Timing & Charts`.

## D. Explain like I'm new to Kundali — P0/P1

- On every term: one-line tooltip — Graha, Lagna, Rashi, Bhava, Nakshatra, Pada, Drishti, Dasha, Navamsa, Yoga.
- Click a planet: its English/Hinglish/Hindi name, symbol, degree, sign, house, longitude, interpretive keywords, reason for inclusion in relevant section.
- Click a house: universal house theme, natal sign, lord, occupants, relevant aspects if verified, and what an empty house means.
- Click any reading: “Why am I seeing this?” linking to real factors used, rule ID, tradition/convention and degree of certainty.
- Detailed educational guide: how North/South layouts differ; houses vs signs; why birth time matters; why astrologers using different ayanamsa/house rules may give different charts.

## E. Visuals, usability, trust — P0/P1

- Elegant modern Indian-inspired but non-stereotypical aesthetic, generous spacing, responsive 360px–desktop, readable chart labels and legends.
- Light and dark modes optional. Use high-contrast text and a tested Devanagari font/license.
- Loading skeleton, empty/error/success states, mobile-first form validation, keyboard and screen reader support, WCAG 2.2 AA target.
- Downloadable PDF with cover, profile, chart(s), planet table, life sections, dasha dates, methodology, references and disclaimer; no missing Hindi glyphs.
- Print stylesheet, page breaks and explicit chart metadata. Export selected language, option to exclude name on export.
- Separate “Astronomical calculation” from “Traditional interpretation” visually and in API schema.
- Transparent policies: no persistent storage by default, opt-in for accounts/favorites, data deletion when enabled, privacy disclosures.
- No sales pressure, bogus ‘99% accuracy’ indicators, fear-based dosha language, or paid-remedy manipulation.

## F. Optional advanced product scope — P2

- Save multiple profiles locally only with consent, or account/cloud with authenticated encryption and deletion.
- Partner comparison requires both individuals to agree to use of their birth data.
- Multi-report comparison by methodology settings. Personal journaling and notes kept private.
- Practitioner review/editor workflow for interpretive templates with versioning and evidence trail.
- Paid plans ONLY after core calculations, licensing, privacy and interpretations pass external review.
- Any AI “explain this term” feature must not calculate planets or promise outcomes. Disclose AI involvement and require explicit opt-in before sending birth data to external services.
