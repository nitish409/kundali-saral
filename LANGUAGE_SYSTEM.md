# Three-language contract: English / Hinglish / हिन्दी

## What the user actually sees

An English-mode visitor should not have to read Hindi script to understand any important data. A Hindi-mode visitor should not suddenly encounter English paragraphs. Hinglish must sound natural when read aloud and use predominantly **Roman Hindi + familiar English**.

**Recommended consistent default** (an intentional upgrade from the original MVP, which uses Hindi-script planets in Hinglish):

| Mode | Script/voice | Planet example | Example insight heading |
| --- | --- | --- | --- |
| English `en` | English, define Sanskrit concepts on first use | Sun, Moon, Mars | Career and work |
| Hinglish `hinglish` | Romanized Hindi + English; optional Devanagari in tooltips | Surya, Chandra, Mangal | Career aur kaam |
| Hindi `hi` | Devanagari Hindi, natural and proofread | सूर्य, चंद्र, मंगल | करियर और काम |

This site can optionally let users show the original Sanskrit script alongside Romanized Hinglish terms, e.g. **Surya (सूर्य)**, but avoid unexplained script switches mid-sentence.

## Nine grahas: canonical IDs and labels

| stable ID | English | Hinglish | Hindi |
| --- | --- | --- | --- |
| `sun` | Sun | Surya | सूर्य |
| `moon` | Moon | Chandra | चंद्र |
| `mars` | Mars | Mangal | मंगल |
| `mercury` | Mercury | Budh | बुध |
| `jupiter` | Jupiter | Guru / Brihaspati | गुरु / बृहस्पति |
| `venus` | Venus | Shukra | शुक्र |
| `saturn` | Saturn | Shani | शनि |
| `rahu` | Rahu (north lunar node) | Rahu | राहु |
| `ketu` | Ketu (south lunar node) | Ketu | केतु |

**Note:** Rahu and Ketu are lunar nodes, not physical planets. Explain this in the user interface while retaining “nine grahas” as a cultural Jyotish term. Do not translate a stable ID or substitute different bodies while switching languages.

## 12 rashis

| Index | English | Hinglish | Hindi |
| --- | --- | --- | --- |
| 0 | Aries | Mesh | मेष |
| 1 | Taurus | Vrishabh | वृषभ |
| 2 | Gemini | Mithun | मिथुन |
| 3 | Cancer | Kark | कर्क |
| 4 | Leo | Singh | सिंह |
| 5 | Virgo | Kanya | कन्या |
| 6 | Libra | Tula | तुला |
| 7 | Scorpio | Vrishchik | वृश्चिक |
| 8 | Sagittarius | Dhanu | धनु |
| 9 | Capricorn | Makar | मकर |
| 10 | Aquarius | Kumbh | कुंभ |
| 11 | Pisces | Meen | मीन |

## 12 house theme headings

| Bhava | English | Hinglish | Hindi |
| --- | --- | --- | --- |
| 1 | Self and identity | Apni pehchaan | स्वयं और पहचान |
| 2 | Family and resources | Parivaar aur paisa | परिवार और संसाधन |
| 3 | Effort and communication | Mehnat aur baatcheet | प्रयास और संवाद |
| 4 | Home and comfort | Ghar aur sukh | घर और सुख |
| 5 | Creativity and learning | Creativity aur padhai | रचनात्मकता और शिक्षा |
| 6 | Routine and challenges | Routine aur challenges | दिनचर्या और चुनौतियाँ |
| 7 | Partnerships | Rishte aur partnership | संबंध और साझेदारी |
| 8 | Change and shared resources | Badlav aur joint resources | परिवर्तन और साझा संसाधन |
| 9 | Beliefs and higher learning | Vichaar aur higher learning | दर्शन और उच्च शिक्षा |
| 10 | Career and public life | Career aur pehchaan | करियर और सार्वजनिक जीवन |
| 11 | Community and gains | Dost aur goals | समुदाय और लक्ष्य |
| 12 | Rest and introspection | Aaram aur self-reflection | विश्राम और आत्मचिंतन |

Avoid pretending house meanings are empirically proven. Some associations vary across schools: record the tradition in source data.

## Important nouns and UI headings

| English | Hinglish | Hindi |
| --- | --- | --- |
| Birth chart | Janam Kundali | जन्म कुंडली |
| Ascendant (Lagna) | Lagna | लग्न |
| Moon sign | Chandra Rashi | चंद्र राशि |
| Sun sign | Surya Rashi | सूर्य राशि |
| House | Bhav | भाव |
| Planet / Graha | Graha | ग्रह |
| Nakshatra | Nakshatra | नक्षत्र |
| Lunar mansion quarter (Pada) | Pada / Charan | चरण |
| Retrograde | Vakri | वक्री |
| Current Mahadasha | Abhi ki Mahadasha | वर्तमान महादशा |
| Traditional interpretation | Paramparik matlab | पारंपरिक व्याख्या |
| Calculated position | Calculate ki gayi position | गणना की गई स्थिति |
| Why this interpretation? | Aisa kyun dikh raha hai? | यह व्याख्या क्यों दिखाई गई है? |
| Career | Career | करियर |
| Love and relationships | Pyaar aur rishte | प्रेम और संबंध |
| Marriage | Shaadi | विवाह |
| Growth | Personal growth | व्यक्तिगत विकास |
| Money | Paisa | धन |
| Education | Padhai | शिक्षा |
| Family | Parivaar | परिवार |
| Wellbeing | Sehat aur routine | सेहत और दिनचर्या |
| Download report | Report download karein | रिपोर्ट डाउनलोड करें |
| Accurate time unknown | Birth time exact nahi pata | जन्म समय निश्चित नहीं है |

## First-mention content example — no invented placements

**English:** “Career and work — this traditional reading reviews your 10th house, its ruler and relevant chart placements. These are symbolic themes, not promises about your job.”

**Hinglish:** “Career aur kaam — is reading mein 10th bhav, uske lord aur aapki chart positions ko dekha gaya hai. Yeh paramparik interpretation hai, job ki guarantee nahi.”

**Hindi:** “करियर और काम — इस व्याख्या में दसवें भाव, उसके स्वामी और कुंडली में ग्रहों की स्थितियों को देखा गया है। यह पारंपरिक व्याख्या है, नौकरी का निश्चित परिणाम नहीं।”

## Localizing the whole product

- Never localize calculation keys (`sun`, `moon`, `houses[0]`, `longitude`, API enum values). Localize ONLY display labels, explanatory content, validation errors, date formats and localized PDF.
- Central message dictionaries `en`, `hinglish`, `hi`: headings, nav, tooltips, forms, errors, loading text, table headers, planet captions, Nakshatra names, disclaimers, SEO, screen-reader descriptions, PDF headings and help articles.
- Distinguish readable date vs machine ISO date; keep `YYYY-MM-DD` in data and render per locale. Preserve numeric degrees and precision across languages.
- Font fallback must support Devanagari; test PDFs separately since embedded fonts are not guaranteed by a browser print stylesheet.
- Avoid male/female assumptions, caste/religious assumptions, marital-status assumptions; support neutral language for all users.
- Use native-speaker QA for Hindi and approachable Roman Hinglish; transliteration should follow one consistent style throughout.
- `lang` attribute: `en` in English, `hi-Latn` for Roman-script Hinglish when supported, `hi` for Hindi; keep language selectors accessible.
- If a translation is missing, show safe English with a logged QA warning during development; block production release with missing critical translations.
- For switching after a chart is generated, keep UTC/longitudes/house indices unchanged. Only re-render labels or call a localization endpoint; it must not depend on the current date to recompute a different natal result.
- Do not allow HTML injection through translation strings or report data; use text nodes or escaped templates.

## Localization test cases

1. Generate the same example for all 3 locales: planet longitude/sign index/house number/nakshatra index exactly equal.
2. In English, all 9 graha names are English; in Hindi all 9 Hindi; Hinglish Roman by the new style decision.
3. Change languages after generating: no loss of report, no planetary position changes.
4. All 17 life sections and PDFs have correct language + no truncated Hindi glyphs.
5. Input errors, city searching states, download labels and accessibility names are translated.
6. Verify punctuation, plural forms, English article grammar and Romanized spelling manually.
