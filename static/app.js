'use strict';
const $ = id => document.getElementById(id);

const state = {
  lang: 'en',
  chartStyle: 'south',
  activeCategory: 'all',
  showHinglishDevanagari: false,
  selectedInspector: { type: 'house', id: 1 },
  city: null,
  data: null,
  cities: [],
  searchTimer: null
};

const T = {
  en: {
    createNav: 'Create Chart',
    glossaryNav: 'Key Terms',
    howItWorks: 'How it works',
    about: 'Privacy & Method',
    showDevanagariHint: 'Show हिंदी script in brackets',
    eyebrow: 'VEDIC WISDOM, MADE UNDERSTANDABLE',
    heroTitle: 'Your Kundali.<br><em>Finally, in your language.</em>',
    heroDescription: 'No confusing charts or difficult astrology words. Explore career, love, marriage, money, education and 17 life areas — explained simply with real astronomical calculations.',
    feature1: 'English · Hinglish · हिंदी',
    feature2: 'North & South Indian D1 charts',
    feature3: 'Privacy first · No database',
    stepLabel: 'STEP 01 · YOUR BIRTH DETAILS',
    formTitle: 'Let’s discover your chart',
    formDescription: 'Enter the date, exact local time, and city where you were born (not your current location).',
    private: 'No account or tracking',
    name: 'Your name (optional)',
    namePlaceholder: 'What should we call you?',
    birthDate: 'Date of birth',
    birthTime: 'Local time of birth',
    timeHint: 'Ascendant (Lagna) shifts roughly every 2 hours.',
    timeUncertainLabel: 'Birth time is uncertain / approximate',
    birthplace: 'Birth city / place (at birth)',
    cityPlaceholder: 'Search your birth city',
    searchPlace: 'Find place',
    cityHint: 'Select a suggestion to set birthplace coordinates and historical timezone.',
    advanced: 'Advanced: coordinates, timezone & DST overlap',
    advancedHint: 'Verify birthplace coordinates or resolve daylight-saving clock overlaps',
    latitude: 'Latitude (-90 to 90)',
    longitude: 'Longitude (-180 to 180)',
    timezone: 'IANA timezone',
    dstFoldLabel: 'Daylight-saving repeated hour',
    dstAuto: 'Ask me if time is ambiguous',
    dstFold0: 'Earlier occurrence (Daylight Saving / Summer time)',
    dstFold1: 'Later occurrence (Standard / Winter time)',
    generate: '✧ Generate my Kundali',
    demo: 'Try a sample chart',
    stepResults: 'STEP 02 · YOUR PERSONAL KUNDALI REPORT',
    excludeNameExport: 'Hide name on export/print',
    print: 'Print / Save PDF Report',
    export: 'Export JSON',
    lagna: 'Ascendant / Lagna',
    lagnaNote: 'First house (H1) & self approach',
    moonSign: 'Moon sign / Rashi',
    moonNote: 'Mind, emotions & inner world',
    sunSign: 'Sun sign (Sidereal)',
    sunNote: 'Vitality & core direction',
    nakshatra: 'Birth Nakshatra',
    currentDashaTile: 'Current Mahadasha',
    badgeCalculated: 'Astronomical Calculation: Lahiri Sidereal',
    badgeTraditional: 'Traditional Jyotish Interpretation',
    explore: 'Explore your Kundali',
    yourChart: 'YOUR BIRTH CHART (D1 RASHI)',
    chartHeading: 'Your birth chart, decoded',
    southStyleBtn: 'South Indian',
    northStyleBtn: 'North Indian (Diamond)',
    bothStyleBtn: 'Show Both',
    chartDescription: 'Click or press Enter on any house or planet to inspect its meaning, ruler, and placements. Switching chart style never alters astronomical positions.',
    southChartTitle: 'South Indian D1 (Fixed Zodiac Signs)',
    northChartTitle: 'North Indian D1 (Fixed Houses, Lagna at Top)',
    inspectorTitle: 'INTERACTIVE CHART INSPECTOR',
    guideTitle: 'How to read North & South charts',
    guide1: 'South Indian chart keeps zodiac signs fixed clockwise; H1 marks your Lagna.',
    guide2: 'North Indian diamond chart keeps House 1 fixed at the top center diamond and counts counter-clockwise; numbers 1–12 show the Rashi (1=Aries … 12=Pisces).',
    guide3: 'Click any house or planet row to see why it matters and where its ruler sits.',
    guide4: 'An empty house is completely normal and never means a bad outcome.',
    planetPositions: '9 Grahas — Astronomical & Nakshatra Positions',
    planetTableHint: 'Click any row to inspect that Graha. Rahu and Ketu are mathematical lunar nodes, not physical planets.',
    planet: 'Graha',
    sign: 'Rashi (Sign)',
    house: 'House',
    degree: 'Degree',
    nakshatraCol: 'Nakshatra (Pada)',
    dignityCol: 'Traditional Status',
    houseTableHeading: '12 Bhavas (Houses) — Signs, Rulers & Occupants',
    houseThemeCol: 'Life Area',
    houseLordCol: 'House Lord (Placement)',
    occupantsCol: 'Occupants & Aspects',
    lifeAreasKicker: '17 LIFE AREAS EXPLAINED',
    lifeAreasHeading: 'Life areas: calculated placements & traditional meaning',
    lifeAreasDesc: 'Filter by category or read all 17 independent sections. Every section separates astronomical chart facts from traditional Parashari symbolism.',
    allCategories: 'All 17 Areas',
    timing: 'TRADITIONAL TIME CYCLES',
    dasha: 'Vimshottari Mahadasha',
    dashaDescription: 'Traditional planetary periods derived from your Moon nakshatra. Uses an approximate 365.2425-day year convention.',
    trustKicker: 'TRANSPARENCY, METHODOLOGY & PRIVACY',
    method: 'How we calculated this & important limits',
    safety: 'Astrology is a cultural and spiritual interpretive tradition, not a scientifically validated way to predict outcomes. Never use this report instead of evidence-based medical, mental health, legal, financial or relationship decisions.',
    glossaryKicker: 'NEW TO KUNDALI?',
    glossaryHeading: 'Key Jyotish words, explained in one line',
    glossarySub: 'You never need to memorize Sanskrit terms to read your chart, but here is what the common words mean.',
    simple: 'SIMPLE BY DESIGN',
    howHeading: 'Ancient concepts. Modern clarity.',
    how1Title: 'Enter birth details',
    how1Body: 'Your birth date, local time, and birthplace coordinates convert accurately to UTC using historical IANA timezone rules.',
    how2Title: 'Real astronomical math',
    how2Body: 'Swiss Ephemeris Moshier computes sidereal (Lahiri) longitudes, whole-sign houses, and Nakshatra padas offline — never guessed by AI.',
    how3Title: 'Facts vs. tradition',
    how3Body: 'Explore 17 life areas with clear rule IDs, balanced strengths and growth edges, and practical self-reflection prompts.',
    footerDesc: 'Making traditional Jyotish easier to understand, transparent about its math, and free of fear-based claims.',
    footerPrivacy: 'Privacy first: birth details are processed in memory only to compute your chart. No user account, tracking pixel, or database storage is used.',
    resultsTitle: 'Your personal Kundali',
    anonymous: 'Anonymous',
    for: 'Birthplace',
    pada: 'Pada',
    ruledBy: 'Ruled by',
    facts: 'Calculated chart placements (Astronomical Facts)',
    whyThis: 'Why am I seeing this? (Methodology & Rule ID)',
    reading: 'Traditional Jyotish interpretation',
    strengthsHeading: 'Potential strengths to build on',
    challengesHeading: 'Balance & growth edge',
    reflection: 'Practical reflection',
    note: 'Important context',
    current: 'CURRENT',
    housePrefix: 'House',
    rashiNumLabel: 'Rashi #',
    emptyHouseLabel: 'Empty house (see Lord)',
    intro: 'Overview',
    positions: 'Charts & Tables',
    periods: 'Mahadasha',
    methodNav: 'Method & Privacy',
    dateRequired: 'Please enter both your date and local time of birth.',
    locationRequired: 'Choose a birth city from suggestions, or enter valid coordinates and an IANA timezone under Advanced.',
    calculating: 'Calculating…',
    failure: 'Could not calculate chart.',
    chartCenter: 'D1 RASHI CHART',
    retrograde: 'Retrograde',
    lunarNodeBadge: 'Lunar Node',
    methodBody: 'Sidereal (Lahiri) zodiac · Whole-sign houses · Swiss Ephemeris Moshier engine · Mean Rahu/Ketu lunar nodes. Local birth time is converted to UTC using the birthplace IANA timezone (including historical daylight-saving transitions). Vimshottari Mahadasha dates use a 365.2425-day solar year convention. Because the Ascendant moves ~1° every 4 minutes, small birth-time errors near a 30° sign boundary can change the Lagna and house numbers.',
    privacyStatus: 'Storage status: Not saved to any server database. Processed transiently in memory for this session only.',
    unknown: 'Unknown place',
    yearsLabel: 'yrs'
  },
  hinglish: {
    createNav: 'Kundali Banao',
    glossaryNav: 'Key Terms',
    howItWorks: 'Kaise kaam karta hai',
    about: 'Privacy aur Method',
    showDevanagariHint: 'Graha naam ke saath हिंदी script dikhayein',
    eyebrow: 'VEDIC KNOWLEDGE, SIMPLE LANGUAGE MEIN',
    heroTitle: 'Aapki Janam Kundali.<br><em>Ab aapki language mein.</em>',
    heroDescription: 'Na confusing charts, na mushkil astrology words. Career, pyaar, shaadi, paisa, padhai aur 17 life areas — real astronomical calculations ke saath simple words mein samjhein.',
    feature1: 'English · Hinglish · हिंदी',
    feature2: 'North aur South Indian D1 charts',
    feature3: 'Privacy first · Koi database nahi',
    stepLabel: 'STEP 01 · AAPKI BIRTH DETAILS',
    formTitle: 'Chaliye aapki Janam Kundali dekhte hain',
    formDescription: 'Apne janam ki date, local time aur birth city daalein (jahan janam hua tha, current city nahi).',
    private: 'Account ya tracking nahi',
    name: 'Aapka naam (optional)',
    namePlaceholder: 'Aapka naam kya hai?',
    birthDate: 'Janam ki date',
    birthTime: 'Janam ka local time',
    timeHint: 'Lagna lagbhag har 2 ghante mein badalta hai.',
    timeUncertainLabel: 'Birth time exact nahi pata / approximate hai',
    birthplace: 'Janam ka shehar / place (birthplace)',
    cityPlaceholder: 'Apna birth city search karein',
    searchPlace: 'Place dhundhein',
    cityHint: 'Suggestion select karein taaki coordinates aur historical timezone set ho jayein.',
    advanced: 'Advanced: coordinates, timezone aur DST overlap',
    advancedHint: 'Birthplace coordinates check karein ya daylight-saving overlap select karein',
    latitude: 'Latitude (-90 se 90)',
    longitude: 'Longitude (-180 se 180)',
    timezone: 'IANA timezone',
    dstFoldLabel: 'Daylight-saving repeated hour',
    dstAuto: 'Ambiguous hone par mujhse poochhein',
    dstFold0: 'Pehla ghanta (Daylight Saving / Summer time)',
    dstFold1: 'Doosra ghanta (Standard / Winter time)',
    generate: '✧ Meri Kundali banao',
    demo: 'Sample chart dekhein',
    stepResults: 'STEP 02 · AAPKI PERSONAL KUNDALI REPORT',
    excludeNameExport: 'Export/print mein naam chhupayein',
    print: 'Report print / PDF save karein',
    export: 'JSON export karein',
    lagna: 'Lagna (Ascendant)',
    lagnaNote: 'First bhav (H1) aur aapki approach',
    moonSign: 'Chandra Rashi',
    moonNote: 'Mann, feelings aur inner comfort',
    sunSign: 'Surya Rashi (Sidereal)',
    sunNote: 'Vitality aur core direction',
    nakshatra: 'Janam Nakshatra',
    currentDashaTile: 'Abhi ki Mahadasha',
    badgeCalculated: 'Calculate ki gayi position: Lahiri Sidereal',
    badgeTraditional: 'Paramparik Jyotish Matlab',
    explore: 'Apni Kundali explore karein',
    yourChart: 'AAPKI JANAM KUNDALI (D1 RASHI)',
    chartHeading: 'Aapka birth chart, simple words mein',
    southStyleBtn: 'South Indian',
    northStyleBtn: 'North Indian (Diamond)',
    bothStyleBtn: 'Dono Dikhayein',
    chartDescription: 'Kisi bhi house ya graha par click ya Enter karein uska matlab, lord aur placement dekhne ke liye. Chart style badalne se calculations nahi badalti.',
    southChartTitle: 'South Indian D1 (Fixed Rashi Boxes)',
    northChartTitle: 'North Indian D1 (Fixed Bhav Diamond, Lagna Top Par)',
    inspectorTitle: 'INTERACTIVE CHART INSPECTOR',
    guideTitle: 'North aur South chart kaise padhein',
    guide1: 'South Indian chart mein rashiyan fixed rehti hain; H1 aapka Lagna dikhata hai.',
    guide2: 'North Indian diamond chart mein House 1 hamesha top center diamond mein rehta hai; 1 se 12 numbers Rashi dikhate hain (1=Mesh … 12=Meen).',
    guide3: 'Kisi bhi bhav ya graha row par click karke uski detail aur lord ki position dekhein.',
    guide4: 'Empty bhav bilkul normal hai aur iska matlab koi problem nahi hota.',
    planetPositions: '9 Graha — Calculate Ki Gayi Positions aur Nakshatra',
    planetTableHint: 'Kisi bhi row par click karke graha ki detail dekhein. Rahu aur Ketu lunar nodes hain, physical planets nahi.',
    planet: 'Graha',
    sign: 'Rashi',
    house: 'Bhav (House)',
    degree: 'Degree',
    nakshatraCol: 'Nakshatra (Pada)',
    dignityCol: 'Paramparik Status',
    houseTableHeading: '12 Bhav (Houses) — Rashi, Bhav Lord aur Occupants',
    houseThemeCol: 'Life Area',
    houseLordCol: 'Bhav Lord (Placement)',
    occupantsCol: 'Graha aur Drishti',
    lifeAreasKicker: '17 LIFE AREAS EXPLAINED',
    lifeAreasHeading: 'Life areas: chart positions aur paramparik matlab',
    lifeAreasDesc: 'Category chunein ya saare 17 topics padhein. Har section mein chart facts aur traditional interpretation alag-alag dikhaye gaye hain.',
    allCategories: 'Saare 17 Topics',
    timing: 'TRADITIONAL TIME CYCLES',
    dasha: 'Vimshottari Mahadasha',
    dashaDescription: 'Chandra ke birth nakshatra se nikli traditional Mahadasha periods (365.2425 days/year approximate convention).',
    trustKicker: 'TRANSPARENCY, METHODOLOGY AUR PRIVACY',
    method: 'Calculation kaise hui aur zaroori baatein',
    safety: 'Astrology ek cultural aur spiritual parampara hai, future predict karne ka scientific tareeqa nahi. Health, legal, paisa ya rishton ke faisle hamesha real-world salah aur evidence par lein.',
    glossaryKicker: 'KUNDALI MEIN NAYE HAIN?',
    glossaryHeading: 'Zaroori Jyotish words, ek line mein',
    glossarySub: 'Report samajhne ke liye mushkil terms yaad rakhne ki zaroorat nahi hai, par inka simple matlab yahan dekhein.',
    simple: 'SIMPLE BY DESIGN',
    howHeading: 'Purani knowledge. Modern clarity.',
    how1Title: 'Birth details daalein',
    how1Body: 'Aapki birth date, local time aur birthplace coordinates historical IANA timezone rules se UTC mein convert hote hain.',
    how2Title: 'Real astronomical math',
    how2Body: 'Swiss Ephemeris Moshier se Lahiri sidereal longitudes, whole-sign bhav aur Nakshatra pada calculate hote hain — bina kisi AI guessing ke.',
    how3Title: 'Facts aur tradition alag-alag',
    how3Body: '17 life areas mein exact placements, rule IDs, balanced strengths/challenges aur reflection questions dekhein.',
    footerDesc: 'Traditional Jyotish ko simple, transparent aur bina kisi darr (fear) ke samjhana.',
    footerPrivacy: 'Privacy first: aapki birth details sirf chart calculate karne ke liye memory mein process hoti hain. Koi account ya database storage nahi hai.',
    resultsTitle: 'Aapki Janam Kundali',
    anonymous: 'Anonymous',
    for: 'Janam sthan',
    pada: 'Pada',
    ruledBy: 'Lord',
    facts: 'Calculate ki gayi positions (Chart Facts)',
    whyThis: 'Aisa kyun dikh raha hai? (Method aur Rule ID)',
    reading: 'Paramparik matlab (Traditional Interpretation)',
    strengthsHeading: 'Possible strengths',
    challengesHeading: 'Balance aur growth point',
    reflection: 'Is par sochein (Reflection)',
    note: 'Dhyan dein',
    current: 'ABHI',
    housePrefix: 'Bhav',
    rashiNumLabel: 'Rashi #',
    emptyHouseLabel: 'Koi graha nahi (Lord dekhein)',
    intro: 'Overview',
    positions: 'Charts aur Tables',
    periods: 'Mahadasha',
    methodNav: 'Method aur Privacy',
    dateRequired: 'Kripya janam ki date aur local time dono daalein.',
    locationRequired: 'Suggestion se birth city chunein ya Advanced mein sahi coordinates aur IANA timezone daalein.',
    calculating: 'Calculate ho raha hai…',
    failure: 'Chart calculate nahi ho paya.',
    chartCenter: 'D1 RASHI CHART',
    retrograde: 'Vakri',
    lunarNodeBadge: 'Lunar Node',
    methodBody: 'Sidereal (Lahiri) zodiac · Whole-sign bhav · Swiss Ephemeris Moshier calculation · Mean Rahu/Ketu nodes. Local birth time ko historical timezone rules se UTC mein badla jaata hai. Mahadasha years 365.2425 days approximate hain. Lagna har 4 minute mein ~1° badalta hai, isliye boundary ke paas thoda sa time farak Lagna badal sakta hai.',
    privacyStatus: 'Storage status: Kisi server database mein save nahi kiya gaya. Sirf is session ke liye memory mein calculate hua.',
    unknown: 'Place nahi mila',
    yearsLabel: 'saal'
  },
  hi: {
    createNav: 'कुंडली बनाएँ',
    glossaryNav: 'प्रमुख शब्द',
    howItWorks: 'कैसे काम करता है',
    about: 'गोपनीयता और पद्धति',
    showDevanagariHint: 'देवनागरी नाम दिखाएँ',
    eyebrow: 'वैदिक ज्योतिष, सरल और स्पष्ट भाषा में',
    heroTitle: 'आपकी जन्म कुंडली।<br><em>अब आपकी भाषा में।</em>',
    heroDescription: 'न उलझे हुए चार्ट, न कठिन ज्योतिषीय शब्दावली। करियर, प्रेम, विवाह, धन, शिक्षा और 17 जीवन-क्षेत्रों को वास्तविक खगोलीय गणना के साथ सरल भाषा में समझें।',
    feature1: 'English · Hinglish · हिंदी',
    feature2: 'उत्तर और दक्षिण भारतीय D1 चार्ट',
    feature3: 'गोपनीयता प्रथम · कोई डेटाबेस नहीं',
    stepLabel: 'चरण 01 · आपका जन्म विवरण',
    formTitle: 'आइए आपकी जन्म कुंडली देखें',
    formDescription: 'अपने जन्म की तारीख, स्थानीय समय और जन्म का शहर भरें (वर्तमान निवास नहीं, बल्कि जन्मस्थान)।',
    private: 'अकाउंट या ट्रैकिंग नहीं',
    name: 'आपका नाम (वैकल्पिक)',
    namePlaceholder: 'आपका नाम क्या है?',
    birthDate: 'जन्म तिथि',
    birthTime: 'जन्म का स्थानीय समय',
    timeHint: 'लग्न लगभग हर 2 घंटे में बदलता है।',
    timeUncertainLabel: 'जन्म समय निश्चित नहीं है / अनुमानित है',
    birthplace: 'जन्म का शहर / स्थान (जन्म के समय)',
    cityPlaceholder: 'जन्मस्थान खोजें',
    searchPlace: 'जगह खोजें',
    cityHint: 'सुझाव चुनें ताकि अक्षांश-देशांतर और ऐतिहासिक समय-क्षेत्र अपने आप भर जाएँ।',
    advanced: 'अतिरिक्त: निर्देशांक, समय-क्षेत्र और DST विकल्प',
    advancedHint: 'जन्मस्थान के निर्देशांक जाँचें या डेलाइट-सेविंग समय चुनें',
    latitude: 'अक्षांश (-90 से 90)',
    longitude: 'देशांतर (-180 से 180)',
    timezone: 'समय-क्षेत्र (IANA)',
    dstFoldLabel: 'डेलाइट-सेविंग दोहराया गया घंटा',
    dstAuto: 'द्विअर्थी समय होने पर मुझसे पूछें',
    dstFold0: 'पहला समय (डेलाइट सेविंग / ग्रीष्म समय)',
    dstFold1: 'दूसरा समय (मानक / शीतकालीन समय)',
    generate: '✧ मेरी कुंडली बनाएँ',
    demo: 'नमूना कुंडली देखें',
    stepResults: 'चरण 02 · आपकी व्यक्तिगत कुंडली रिपोर्ट',
    excludeNameExport: 'प्रिंट/निर्यात में नाम छुपाएँ',
    print: 'रिपोर्ट प्रिंट / PDF सेव करें',
    export: 'JSON डाउनलोड करें',
    lagna: 'लग्न (Ascendant)',
    lagnaNote: 'प्रथम भाव (H1) और जीवन दृष्टिकोण',
    moonSign: 'चंद्र राशि',
    moonNote: 'मन, भावनाएँ और आंतरिक शांति',
    sunSign: 'सूर्य राशि (निरयन)',
    sunNote: 'ऊर्जा और आत्मविश्वास',
    nakshatra: 'जन्म नक्षत्र',
    currentDashaTile: 'वर्तमान महादशा',
    badgeCalculated: 'गणना की गई स्थिति: लाहिड़ी निरयन',
    badgeTraditional: 'पारंपरिक ज्योतिषीय व्याख्या',
    explore: 'कुंडली के विषय',
    yourChart: 'आपकी जन्म कुंडली (D1 राशि चक्र)',
    chartHeading: 'आपकी जन्म कुंडली, आसान भाषा में',
    southStyleBtn: 'दक्षिण भारतीय',
    northStyleBtn: 'उत्तर भारतीय (डायमंड)',
    bothStyleBtn: 'दोनों दिखाएँ',
    chartDescription: 'किसी भी भाव या ग्रह पर क्लिक या Enter करें और उसका अर्थ, स्वामी और स्थिति देखें। चार्ट शैली बदलने से गणितीय स्थिति नहीं बदलती।',
    southChartTitle: 'दक्षिण भारतीय D1 (स्थिर राशि क्रम)',
    northChartTitle: 'उत्तर भारतीय D1 (स्थिर भाव, लग्न ऊपर मध्य में)',
    inspectorTitle: 'इंटरएक्टिव चार्ट विवरण',
    guideTitle: 'उत्तर और दक्षिण भारतीय चार्ट कैसे पढ़ें',
    guide1: 'दक्षिण भारतीय चार्ट में राशियाँ स्थिर रहती हैं; H1 आपका लग्न दर्शाता है।',
    guide2: 'उत्तर भारतीय डायमंड चार्ट में प्रथम भाव (H1) हमेशा ऊपर के मध्य खाने में रहता है; 1 से 12 की संख्या राशि क्रम (1=मेष … 12=मीन) दिखाती है।',
    guide3: 'किसी भी भाव या ग्रह पंक्ति पर क्लिक करके उसका विस्तृत अर्थ और भावेश की स्थिति देखें।',
    guide4: 'खाली भाव पूरी तरह सामान्य है और इसका अर्थ कोई अशुभ परिणाम नहीं होता।',
    planetPositions: '9 ग्रह — खगोलीय अंश और नक्षत्र स्थिति',
    planetTableHint: 'विस्तृत जानकारी के लिए किसी भी ग्रह पंक्ति पर क्लिक करें। राहु और केतु छाया ग्रह (चंद्र पात) हैं, भौतिक पिंड नहीं।',
    planet: 'ग्रह',
    sign: 'राशि',
    house: 'भाव',
    degree: 'अंश',
    nakshatraCol: 'नक्षत्र (चरण)',
    dignityCol: 'पारंपरिक स्थिति',
    houseTableHeading: '12 भाव — राशियाँ, भावेश और स्थित ग्रह',
    houseThemeCol: 'जीवन क्षेत्र',
    houseLordCol: 'भावेश (स्थिति)',
    occupantsCol: 'स्थित ग्रह और दृष्टि',
    lifeAreasKicker: '17 जीवन-क्षेत्रों की व्याख्या',
    lifeAreasHeading: 'जीवन के विषय: गणना की गई स्थिति और पारंपरिक अर्थ',
    lifeAreasDesc: 'श्रेणी चुनें या सभी 17 स्वतंत्र विषयों को पढ़ें। प्रत्येक विषय में खगोलीय तथ्य और पारंपरिक पाराशरी व्याख्या अलग-अलग स्पष्ट हैं।',
    allCategories: 'सभी 17 विषय',
    timing: 'पारंपरिक समय चक्र',
    dasha: 'विंशोत्तरी महादशा',
    dashaDescription: 'चंद्रमा के जन्म नक्षत्र से निकली पारंपरिक ग्रह दशाएँ (365.2425 दिन प्रति वर्ष के अनुमानित मान पर आधारित)।',
    trustKicker: 'पारदर्शिता, गणना पद्धति और गोपनीयता',
    method: 'गणना कैसे की गई और महत्वपूर्ण सीमाएँ',
    safety: 'ज्योतिष एक सांस्कृतिक और आध्यात्मिक व्याख्या परंपरा है, भविष्य बताने की वैज्ञानिक रूप से प्रमाणित विधि नहीं। स्वास्थ्य, कानून, धन या संबंधों के निर्णय हमेशा वास्तविक प्रमाण और विशेषज्ञ सलाह से लें।',
    glossaryKicker: 'कुंडली में नए हैं?',
    glossaryHeading: 'प्रमुख ज्योतिषीय शब्द, एक पंक्ति में',
    glossarySub: 'कुंडली समझने के लिए कठिन संस्कृत शब्द याद रखना जरूरी नहीं है, फिर भी मुख्य शब्दों का सरल अर्थ यहाँ दिया गया है।',
    simple: 'सरल और पारदर्शी डिज़ाइन',
    howHeading: 'प्राचीन अवधारणाएँ। आधुनिक स्पष्टता।',
    how1Title: 'जन्म विवरण भरें',
    how1Body: 'आपकी जन्म तिथि, स्थानीय समय और जन्मस्थान के निर्देशांक ऐतिहासिक समय-क्षेत्र नियमों से UTC में बदले जाते हैं।',
    how2Title: 'वास्तविक खगोलीय गणित',
    how2Body: 'स्विस एफेमेरिस मोशियर से लाहिड़ी निरयन अंश, पूर्ण-राशि भाव और नक्षत्र चरण निकाले जाते हैं — बिना किसी AI अनुमान के।',
    how3Title: 'तथ्य और परंपरा का स्पष्ट अंतर',
    how3Body: '17 जीवन-क्षेत्रों में सटीक ग्रह स्थिति, नियम संख्या, संभावित सबल पक्ष, संतुलन बिंदु और आत्मचिंतन प्रश्न देखें।',
    footerDesc: 'पारंपरिक ज्योतिष को सरल, पारदर्शी और भय-मुक्त रूप में प्रस्तुत करना।',
    footerPrivacy: 'गोपनीयता प्रथम: जन्म विवरण केवल गणना के लिए मेमोरी में प्रोसेस होता है। कोई अकाउंट, ट्रैकिंग या डेटाबेस स्टोरेज नहीं है।',
    resultsTitle: 'आपकी जन्म कुंडली',
    anonymous: 'अनाम (Anonymous)',
    for: 'जन्मस्थान',
    pada: 'चरण',
    ruledBy: 'स्वामी',
    facts: 'गणना की गई स्थिति (कुंडली के तथ्य)',
    whyThis: 'यह व्याख्या क्यों दिखाई गई है? (पद्धति और नियम)',
    reading: 'पारंपरिक ज्योतिषीय व्याख्या',
    strengthsHeading: 'संभावित सबल पक्ष',
    challengesHeading: 'संतुलन और ध्यान देने योग्य बिंदु',
    reflection: 'आत्मचिंतन प्रश्न',
    note: 'महत्वपूर्ण संदर्भ',
    current: 'वर्तमान',
    housePrefix: 'भाव',
    rashiNumLabel: 'राशि क्र.',
    emptyHouseLabel: 'कोई ग्रह नहीं (भावेश देखें)',
    intro: 'सारांश',
    positions: 'चार्ट और तालिकाएँ',
    periods: 'महादशा',
    methodNav: 'पद्धति और गोपनीयता',
    dateRequired: 'कृपया जन्म तिथि और जन्म का सही स्थानीय समय भरें।',
    locationRequired: 'सुझाव से जन्मस्थान चुनें या अतिरिक्त विकल्प में सही निर्देशांक और समय-क्षेत्र लिखें।',
    calculating: 'गणना हो रही है…',
    failure: 'कुंडली की गणना नहीं हो सकी।',
    chartCenter: 'D1 राशि चक्र',
    retrograde: 'वक्री',
    lunarNodeBadge: 'छाया ग्रह',
    methodBody: 'निरयन (लाहिड़ी अयनांश) राशि-पद्धति · पूर्ण-राशि (Whole Sign) भाव · स्विस एफेमेरिस मोशियर गणना · माध्य राहु/केतु। जन्म समय को जन्मस्थान के ऐतिहासिक समय-क्षेत्र नियमों से UTC में बदला जाता है। विंशोत्तरी दशा में 365.2425 दिन का वर्ष माना गया है। लग्न हर 4 मिनट में लगभग 1° बढ़ता है, इसलिए राशि संधि के पास समय के छोटे अंतर से लग्न बदल सकता है।',
    privacyStatus: 'डेटा संग्रहण स्थिति: किसी भी सर्वर डेटाबेस में सहेजा नहीं गया है। केवल इस सत्र में गणना के लिए उपयोग किया गया।',
    unknown: 'अज्ञात स्थान',
    yearsLabel: 'वर्ष'
  }
};

const STATIC_GLOSSARY = {
  en: [
    { term: 'Lagna (Ascendant)', short: 'The zodiac sign rising on the eastern horizon at your exact birth time and place; it marks House 1.' },
    { term: 'Rashi (Zodiac Sign)', short: 'One of the 12 equal 30° sidereal zodiac segments (Aries to Pisces) calculated with Lahiri ayanamsa.' },
    { term: 'Bhava (House)', short: 'One of the 12 life areas (self, resources, work, relationships, etc.). In Whole Sign houses, each sign equals one house.' },
    { term: 'Graha (Planet / Node)', short: 'The 9 celestial markers in Jyotish: Sun, Moon, Mars, Mercury, Jupiter, Venus, Saturn, plus the lunar nodes Rahu and Ketu.' },
    { term: 'Nakshatra & Pada', short: 'One of the 27 equal lunar constellations (13°20′ each), divided into 4 quarters (padas) of 3°20′.' },
    { term: 'Mahadasha', short: 'Traditional Vimshottari planetary time cycles started from the Moon’s birth Nakshatra position.' },
    { term: 'Drishti (Aspect)', short: 'Traditional Parashari directional sight cast by a graha onto other houses (all 7 planets aspect the 7th house from themselves).' },
    { term: 'Vakri (Retrograde)', short: 'When a planet appears to move backward along the zodiac from Earth’s perspective; Sun and Moon are never retrograde.' }
  ],
  hinglish: [
    { term: 'Lagna (Ascendant)', short: 'Aapke exact birth time aur place par eastern horizon par udit hone wali rashi; yahi House 1 banti hai.' },
    { term: 'Rashi (Zodiac Sign)', short: 'Sidereal zodiac ke 12 barabar (30°) hisse — Mesh se Meen tak (Lahiri ayanamsa ke saath).' },
    { term: 'Bhav (House)', short: 'Kundali ke 12 life areas (jaise self, paisa, career, rishte). Whole-sign system mein ek rashi poora ek bhav hoti hai.' },
    { term: 'Graha (9 Bodies)', short: 'Jyotish ke 9 graha: Surya, Chandra, Mangal, Budh, Guru, Shukra, Shani aur do lunar nodes Rahu-Ketu.' },
    { term: 'Nakshatra aur Pada', short: 'Zodiac ke 27 barabar nakshatra (har ek 13°20′), aur har nakshatra ke 4 charan (pada, 3°20′).' },
    { term: 'Mahadasha', short: 'Chandra ke birth nakshatra se shuru hone wale traditional Vimshottari time periods.' },
    { term: 'Drishti (Aspect)', short: 'Parashari parampara mein graha ki doosre bhavon par drishti (sabhi 7 graha apne se 7th bhav ko dekhte hain).' },
    { term: 'Vakri (Retrograde)', short: 'Jab Prithvi se dekhne par koi graha peeche chalta hua dikhta hai; Surya aur Chandra kabhi vakri nahi hote.' }
  ],
  hi: [
    { term: 'लग्न (Ascendant)', short: 'आपके जन्म के सटीक समय और स्थान पर पूर्वी क्षितिज पर उदित होने वाली राशि; यही प्रथम भाव (H1) होती है।' },
    { term: 'राशि (Zodiac Sign)', short: 'निरयन राशिचक्र के 12 बराबर (30°) भाग — मेष से मीन तक (लाहिड़ी अयनांश के अनुसार)।' },
    { term: 'भाव (House)', short: 'कुंडली के 12 जीवन-क्षेत्र (स्वयं, धन, करियर, संबंध आदि)। पूर्ण-राशि पद्धति में एक राशि पूरा एक भाव होती है।' },
    { term: 'ग्रह (9 Grahas)', short: 'ज्योतिष के 9 ग्रह: सूर्य, चंद्र, मंगल, बुध, गुरु, शुक्र, शनि तथा दो छाया ग्रह (चंद्र पात) राहु और केतु।' },
    { term: 'नक्षत्र और चरण (Pada)', short: 'राशिचक्र के 27 समान नक्षत्र (प्रत्येक 13°20′) और प्रत्येक नक्षत्र के 4 चरण (प्रत्येक 3°20′)।' },
    { term: 'महादशा (Mahadasha)', short: 'जन्म के चंद्र नक्षत्र से प्रारंभ होने वाले पारंपरिक विंशोत्तरी समय-चक्र।' },
    { term: 'दृष्टि (Aspect)', short: 'पाराशरी परंपरा के अनुसार ग्रह की अन्य भावों पर दृष्टि (सभी 7 ग्रह अपने से सप्तम भाव को देखते हैं)।' },
    { term: 'वक्री (Retrograde)', short: 'जब पृथ्वी से देखने पर कोई ग्रह राशिचक्र में पीछे की ओर गति करता प्रतीत होता है; सूर्य और चंद्र कभी वक्री नहीं होते।' }
  ]
};

const navIcons = {
  chart: '◈', personality: '✦', creativity: '❀', resilience: '☽',
  career: '▣', entrepreneurship: '⚡', education: '▤', leadership: '♛',
  love: '♡', marriage: '❦', friends: '☺', money: '◉',
  family: '⌂', children: '🌱', health: '✿', travel: '✈',
  spirituality: '☸', growth: '☼', dasha: '◷', method: 'ⓘ'
};

const SOUTH_GRID = [
  [11, 0, 1, 2],
  [10, -1, -1, 3],
  [9, -1, -1, 4],
  [8, 7, 6, 5]
];

// North Indian fixed-house diamond geometry (400x400 coordinate space, counter-clockwise from top center H1)
const NORTH_HOUSES = [
  { house: 1, points: '200,0 100,100 200,200 300,100', cx: 200, cy: 100 },
  { house: 2, points: '0,0 200,0 100,100', cx: 100, cy: 38 },
  { house: 3, points: '0,0 100,100 0,200', cx: 38, cy: 100 },
  { house: 4, points: '100,100 0,200 100,300 200,200', cx: 100, cy: 200 },
  { house: 5, points: '0,200 100,300 0,400', cx: 38, cy: 300 },
  { house: 6, points: '0,400 100,300 200,400', cx: 100, cy: 362 },
  { house: 7, points: '200,200 100,300 200,400 300,300', cx: 200, cy: 300 },
  { house: 8, points: '200,400 300,300 400,400', cx: 300, cy: 362 },
  { house: 9, points: '400,400 300,300 400,200', cx: 362, cy: 300 },
  { house: 10, points: '200,200 300,300 400,200 300,100', cx: 300, cy: 200 },
  { house: 11, points: '400,200 300,100 400,0', cx: 362, cy: 100 },
  { house: 12, points: '200,0 300,100 400,0', cx: 300, cy: 38 }
];

const PLANET_GLYPHS = {
  sun: '☉', moon: '☽', mars: '♂', mercury: '☿',
  jupiter: '♃', venus: '♀', saturn: '♄', rahu: '☊', ketu: '☋'
};

function esc(input) {
  return String(input ?? '').replace(/[&<>"']/g, ch => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  }[ch]));
}

function tr(key) {
  return T[state.lang]?.[key] ?? T.en[key] ?? key;
}

function formatPlanetDisplayName(p) {
  if (!p) return '';
  if (state.lang === 'hinglish' && state.showHinglishDevanagari && p.name_hi) {
    return `${p.name} (${p.name_hi})`;
  }
  return p.name;
}

function renderGlossary(items) {
  const list = items || STATIC_GLOSSARY[state.lang] || STATIC_GLOSSARY.en;
  const grid = $('glossary-grid');
  if (!grid) return;
  grid.innerHTML = list.map(item => `
    <article class="glossary-card">
      <h3>${esc(item.term)}</h3>
      <p>${esc(item.short)}</p>
    </article>
  `).join('');
}

function applyLanguage(lang) {
  state.lang = lang;
  document.documentElement.lang = lang === 'hinglish' ? 'hi-Latn' : lang;
  document.querySelectorAll('[data-lang]').forEach(b => {
    const active = b.dataset.lang === lang;
    b.classList.toggle('active', active);
    b.setAttribute('aria-pressed', String(active));
  });
  const scriptWrap = $('hinglish-script-wrap');
  if (scriptWrap) {
    scriptWrap.hidden = lang !== 'hinglish';
  }
  document.querySelectorAll('[data-i18n]').forEach(el => {
    el.textContent = tr(el.dataset.i18n);
  });
  document.querySelectorAll('[data-i18n-html]').forEach(el => {
    el.innerHTML = tr(el.dataset.i18nHtml);
  });
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    el.placeholder = tr(el.dataset.i18nPlaceholder);
  });
  renderGlossary(state.data?.reading?.glossary);
  if (state.data) {
    generate(false);
  }
}

function applyChartStyle(style) {
  state.chartStyle = style;
  document.querySelectorAll('[data-chart-style]').forEach(b => {
    const active = b.dataset.chartStyle === style;
    b.classList.toggle('active', active);
    b.setAttribute('aria-pressed', String(active));
  });
  const stage = $('charts-stage');
  if (stage) stage.dataset.mode = style;
  const southBox = $('south-chart-box');
  const northBox = $('north-chart-box');
  if (southBox && northBox) {
    southBox.hidden = style === 'north';
    northBox.hidden = style === 'south';
  }
}

async function getCities() {
  try {
    const r = await fetch('/api/cities');
    if (r.ok) {
      state.cities = (await r.json()).cities;
      const city = state.cities.find(c => c.name === 'New Delhi');
      if (city) pickCity(city);
    }
  } catch {
    pickCity({ name: 'New Delhi', country: 'India', latitude: 28.6139, longitude: 77.2090, time_zone: 'Asia/Kolkata' });
  }
}

function pickCity(city) {
  state.city = city;
  $('city').value = `${city.name}${city.country ? ', ' + city.country : ''}`;
  $('lat').value = city.latitude;
  $('lon').value = city.longitude;
  $('tz').value = city.time_zone || '';
  $('city-options').hidden = true;
  $('city').setAttribute('aria-expanded', 'false');
}

function showCities(cities) {
  const ul = $('city-options');
  ul.innerHTML = '';
  cities.slice(0, 8).forEach(c => {
    const li = document.createElement('li');
    const button = document.createElement('button');
    button.type = 'button';
    button.role = 'option';
    button.textContent = c.display_name || `${c.name}, ${c.country}`;
    button.addEventListener('click', () => pickCity(c));
    li.append(button);
    ul.append(li);
  });
  ul.hidden = !cities.length;
  $('city').setAttribute('aria-expanded', String(!!cities.length));
}

async function citySearch() {
  const query = $('city').value.trim();
  if (query.length < 2) {
    showCities([]);
    return;
  }
  const offline = state.cities.filter(c => (`${c.name}, ${c.country}`).toLowerCase().includes(query.toLowerCase()));
  showCities(offline);
}

function formError(message) {
  const el = $('form-error');
  el.textContent = message;
  el.hidden = false;
}

function clearError() {
  $('form-error').hidden = true;
}

async function generate(shouldScroll = true) {
  clearError();
  const date = $('birth-date').value;
  const time = $('birth-time').value;
  if (!date || !time) {
    formError(tr('dateRequired'));
    return;
  }
  const lat = Number($('lat').value);
  const lon = Number($('lon').value);
  const tz = $('tz').value.trim();
  if (!$('lat').value || !$('lon').value || !tz || !Number.isFinite(lat) || !Number.isFinite(lon) || Math.abs(lat) > 90 || Math.abs(lon) > 180) {
    $('advanced').open = true;
    formError(tr('locationRequired'));
    return;
  }
  const foldRaw = $('dst-fold') ? $('dst-fold').value : '';
  const dst_fold = foldRaw === '0' ? 0 : foldRaw === '1' ? 1 : null;
  const time_uncertain = Boolean($('time-uncertain')?.checked);

  const payload = {
    name: $('name').value,
    city: $('city').value,
    birth_date: date,
    birth_time: time,
    latitude: lat,
    longitude: lon,
    time_zone: tz,
    language: state.lang,
    dst_fold,
    time_uncertain
  };

  const button = $('generate-btn');
  button.disabled = true;
  button.querySelector('span').textContent = tr('calculating');
  try {
    const res = await fetch('/api/chart', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    if (!res.ok) {
      const msg = typeof data.detail === 'string' ? data.detail : tr('failure');
      if (msg.toLowerCase().includes('ambiguous daylight-saving')) {
        $('advanced').open = true;
        $('dst-fold')?.focus();
      }
      throw new Error(msg);
    }
    state.data = data;
    renderResult(data);
    $('results').hidden = false;
    if (shouldScroll) {
      $('results').scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  } catch (error) {
    formError(error.message || tr('failure'));
  } finally {
    button.disabled = false;
    button.querySelector('span').textContent = tr('generate');
  }
}

function getDisplayName(data) {
  if ($('anon-export')?.checked) return tr('anonymous');
  return data.name ? data.name : '';
}

function renderResult(data) {
  const chart = data.chart;
  const read = data.reading;
  const displayName = getDisplayName(data);
  const planetByKey = Object.fromEntries(chart.planets.map(p => [p.key, p]));

  $('results-title').textContent = displayName ? `${displayName} · ${tr('resultsTitle')}` : tr('resultsTitle');
  const subtitleParts = [
    chart.birth.date,
    chart.birth.time + (chart.birth.time_uncertain ? ' (~)' : ''),
    data.city || tr('unknown'),
    `${chart.birth.time_zone}`
  ];
  $('results-subtitle').textContent = subtitleParts.join(' · ');

  const printMeta = $('print-meta-line');
  if (printMeta) {
    printMeta.textContent = `${displayName || tr('anonymous')} | ${subtitleParts.join(' · ')} | ${chart.system.zodiac} | ${chart.system.houses}`;
  }

  const uncBanner = $('uncertainty-alert');
  if (uncBanner) {
    if (read.uncertainty_banner) {
      uncBanner.textContent = '⚠ ' + read.uncertainty_banner;
      uncBanner.hidden = false;
    } else {
      uncBanner.hidden = true;
    }
  }

  $('lagna-result').textContent = `${chart.lagna.sign} (${chart.lagna.dms || chart.lagna.degree + '°'})`;
  $('lagna-note').textContent = `${tr('ruledBy')}: ${chart.lagna.lord || ''}`;
  const moonP = planetByKey.moon;
  const sunP = planetByKey.sun;
  $('moon-result').textContent = `${chart.moon_sign}${moonP ? ' (' + moonP.dms + ')' : ''}`;
  $('sun-result').textContent = `${chart.sun_sign}${sunP ? ' (' + sunP.dms + ')' : ''}`;
  $('nakshatra-result').textContent = chart.nakshatra.name;
  $('pada-result').textContent = `${tr('pada')} ${chart.nakshatra.pada}${chart.nakshatra.lord ? ' · ' + tr('ruledBy') + ' ' + chart.nakshatra.lord : ''}`;

  const currentDasha = chart.dashas.find(d => d.current) || chart.dashas[0];
  if (currentDasha) {
    $('dasha-tile-result').textContent = currentDasha.name;
    $('dasha-tile-dates').textContent = `${currentDasha.start} → ${currentDasha.end}`;
  }

  $('read-summary').textContent = read.summary;
  $('read-intro').textContent = read.intro;

  renderChartsAndTables(chart, read);
  renderCategoryTabs(read.categories, read.sections);
  renderTopics(read.sections);
  renderDashas(chart.dashas);
  renderGlossary(read.glossary);

  $('method-text').innerHTML = `
    <p>${esc(tr('methodBody'))}</p>
    <p class="method-meta-box">
      <b>UTC Instant:</b> ${esc(chart.birth.utc)} ·
      <b>Coordinates:</b> ${esc(chart.birth.latitude)}, ${esc(chart.birth.longitude)} ·
      <b>Timezone:</b> ${esc(chart.birth.time_zone)} ·
      <b>Engine:</b> ${esc(chart.system.ephemeris)} (v${esc(chart.system.calculation_version || '1.0')})
    </p>
    <p class="privacy-confirm-line">♧ ${esc(tr('privacyStatus'))}</p>
  `;
  buildNav(read.sections);
}

function selectInspector(type, id) {
  state.selectedInspector = { type, id };
  if (!state.data) return;
  const chart = state.data.chart;
  const read = state.data.reading;
  const headingEl = $('inspector-heading');
  const bodyEl = $('inspector-body');
  const metaEl = $('inspector-meta');

  document.querySelectorAll('[data-inspect-house]').forEach(el => {
    el.classList.toggle('is-selected', type === 'house' && Number(el.dataset.inspectHouse) === Number(id));
  });
  document.querySelectorAll('[data-inspect-planet]').forEach(el => {
    el.classList.toggle('is-selected', type === 'planet' && el.dataset.inspectPlanet === id);
  });

  if (type === 'planet') {
    const pg = (read.planet_guide || []).find(p => p.key === id) || chart.planets.find(p => p.key === id);
    if (!pg) return;
    const glyph = PLANET_GLYPHS[pg.key] || '✦';
    headingEl.textContent = `${glyph} ${pg.name} (${pg.name_en} / ${pg.name_hinglish} / ${pg.name_hi})`;
    bodyEl.textContent = pg.description || '';
    metaEl.innerHTML = `
      <span class="mini-tag">${esc(tr('sign'))}: ${esc(pg.sign)} (${esc(pg.dms || pg.degrees + '°')})</span>
      <span class="mini-tag">${esc(tr('housePrefix'))} ${esc(pg.house)}</span>
      <span class="mini-tag">${esc(pg.nakshatra)} · ${esc(tr('pada'))} ${esc(pg.pada)}</span>
      <span class="mini-tag">${esc(pg.dignity || '')}</span>
      ${pg.retrograde ? `<span class="mini-tag retro-tag">℞ ${esc(tr('retrograde'))}</span>` : ''}
      <p class="inspector-note">${esc(pg.node_note || '')} ${esc(pg.retro_note || '')}</p>
    `;
  } else {
    const hNum = Number(id) || 1;
    const hg = (read.house_guide || []).find(h => h.number === hNum);
    const rawH = chart.houses.find(h => h.number === hNum);
    if (!rawH) return;
    headingEl.textContent = `H${rawH.number} · ${hg ? hg.heading : ''} — ${rawH.sign} (${tr('rashiNumLabel')}${rawH.rashi_number || (rawH.sign_index + 1)})`;
    bodyEl.textContent = hg ? `${hg.summary} ${hg.occupants_text}` : '';
    metaEl.innerHTML = `
      <span class="mini-tag">${esc(tr('ruledBy'))}: ${esc(rawH.lord)} (H${esc(rawH.lord_house)})</span>
      <span class="mini-tag">${esc(hg ? hg.theme : '')}</span>
      ${hg && hg.aspects_text ? `<p class="inspector-note">${esc(hg.aspects_text)}</p>` : ''}
    `;
  }
}

function bindInteractiveKeyOrClick(el, callback) {
  el.addEventListener('click', callback);
  el.addEventListener('keydown', e => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      callback();
    }
  });
}

function renderSouthChart(chart, planetByKey) {
  const grid = $('vedic-chart');
  grid.innerHTML = '';
  for (let row = 0; row < 4; row++) {
    for (let col = 0; col < 4; col++) {
      const signIdx = SOUTH_GRID[row][col];
      if (signIdx < 0) continue;
      const house = chart.houses.find(h => h.sign_index === signIdx);
      const div = document.createElement('div');
      div.className = 'sign-cell' + (house.number === 1 ? ' is-lagna' : '');
      div.style.gridColumn = String(col + 1);
      div.style.gridRow = String(row + 1);
      div.tabIndex = 0;
      div.setAttribute('role', 'button');
      div.dataset.inspectHouse = String(house.number);
      const pNames = house.planets.map(p => formatPlanetDisplayName(planetByKey[p.key] || p));
      div.setAttribute('aria-label', `${tr('housePrefix')} ${house.number}, ${house.sign}, ${pNames.join(', ') || tr('emptyHouseLabel')}`);
      div.innerHTML = `
        <span class="sign-top">${esc(house.sign)} <small>#${signIdx + 1}</small></span>
        <span class="house-num">H${house.number}${house.number === 1 ? ' ✦ Lagna' : ''}</span>
        <span class="planets">${pNames.map(n => esc(n)).join(' · ') || '—'}</span>
      `;
      bindInteractiveKeyOrClick(div, () => selectInspector('house', house.number));
      grid.append(div);
    }
  }
  const center = document.createElement('div');
  center.className = 'chart-center';
  center.innerHTML = `<span>✥</span>${esc(tr('chartCenter'))}<small>${esc(chart.lagna.sign)}</small>`;
  grid.append(center);
}

function renderNorthChart(chart, planetByKey) {
  const container = $('north-chart');
  if (!container) return;
  const houseMap = Object.fromEntries(chart.houses.map(h => [h.number, h]));

  const polygonsSvg = NORTH_HOUSES.map(nh => {
    const h = houseMap[nh.house];
    const isLagna = nh.house === 1;
    const pNames = h.planets.map(p => formatPlanetDisplayName(planetByKey[p.key] || p));
    const pLine1 = pNames.slice(0, 2).join(' · ');
    const pLine2 = pNames.slice(2, 5).join(' · ');
    const rashiNum = h.rashi_number || (h.sign_index + 1);
    return `
      <g class="north-house-group ${isLagna ? 'is-lagna' : ''}" data-inspect-house="${nh.house}" tabindex="0" role="button"
         aria-label="${esc(tr('housePrefix'))} ${nh.house}, ${esc(h.sign)} (${rashiNum}), ${esc(pNames.join(', ') || tr('emptyHouseLabel'))}">
        <polygon points="${nh.points}" class="north-polygon ${isLagna ? 'lagna-poly' : ''}" />
        <text x="${nh.cx}" y="${nh.cy - 16}" text-anchor="middle" class="north-house-tag">H${nh.house}${isLagna ? ' ✦' : ''}</text>
        <text x="${nh.cx}" y="${nh.cy}" text-anchor="middle" class="north-rashi-label">${rashiNum} · ${esc(h.sign)}</text>
        <text x="${nh.cx}" y="${nh.cy + 15}" text-anchor="middle" class="north-planets-line">${esc(pLine1 || '—')}</text>
        ${pLine2 ? `<text x="${nh.cx}" y="${nh.cy + 28}" text-anchor="middle" class="north-planets-line">${esc(pLine2)}</text>` : ''}
      </g>
    `;
  }).join('');

  container.innerHTML = `
    <svg viewBox="0 0 400 400" class="north-svg" role="img" aria-label="North Indian Diamond Kundali Chart">
      <rect x="1" y="1" width="398" height="398" fill="#fbf9fe" stroke="#b9a3dc" stroke-width="2" rx="8" />
      ${polygonsSvg}
    </svg>
  `;

  container.querySelectorAll('.north-house-group').forEach(g => {
    const hNum = Number(g.dataset.inspectHouse);
    bindInteractiveKeyOrClick(g, () => selectInspector('house', hNum));
  });
}

function renderChartsAndTables(chart, read) {
  const planetByKey = Object.fromEntries(chart.planets.map(p => [p.key, p]));
  renderSouthChart(chart, planetByKey);
  renderNorthChart(chart, planetByKey);
  applyChartStyle(state.chartStyle);

  // 9 Grahas Table
  const pRows = $('planet-rows');
  pRows.innerHTML = chart.planets.map(p => {
    const dispName = formatPlanetDisplayName(p);
    return `
      <tr class="interactive-row" data-inspect-planet="${esc(p.key)}" tabindex="0" role="button" aria-label="${esc(dispName)}, ${esc(p.sign)}, ${esc(tr('housePrefix'))} ${p.house}">
        <td>
          <span class="planet-glyph" aria-hidden="true">${PLANET_GLYPHS[p.key]}</span>
          <span>${esc(dispName)}</span>
          ${p.retrograde ? ` <span class="badge-inline retro" title="${esc(tr('retrograde'))}">℞ ${esc(tr('retrograde'))}</span>` : ''}
          ${p.is_node ? ` <span class="badge-inline node">${esc(tr('lunarNodeBadge'))}</span>` : ''}
        </td>
        <td>${esc(p.sign)} <small class="muted">#${p.rashi_number || (p.sign_index + 1)}</small></td>
        <td>H${p.house}</td>
        <td>${esc(p.dms || p.degrees.toFixed(2) + '°')}</td>
        <td>${esc(p.nakshatra || '—')} <small class="muted">(${esc(tr('pada'))} ${p.pada || '—'})</small></td>
        <td><span class="status-pill">${esc(p.dignity || '—')}</span></td>
      </tr>
    `;
  }).join('');

  pRows.querySelectorAll('tr[data-inspect-planet]').forEach(row => {
    bindInteractiveKeyOrClick(row, () => selectInspector('planet', row.dataset.inspectPlanet));
  });

  // 12 Houses Table
  const hRows = $('house-rows');
  if (hRows) {
    const hGuideMap = Object.fromEntries((read.house_guide || []).map(hg => [hg.number, hg]));
    hRows.innerHTML = chart.houses.map(h => {
      const hg = hGuideMap[h.number];
      const occ = h.planets.map(p => `${formatPlanetDisplayName(planetByKey[p.key] || p)} (${p.dms || p.degrees + '°'})`).join(', ') || tr('emptyHouseLabel');
      const asp = (h.aspected_by || []).map(a => `${a.name} (H${a.from_house})`).join(', ');
      return `
        <tr class="interactive-row" data-inspect-house="${h.number}" tabindex="0" role="button" aria-label="${esc(tr('housePrefix'))} ${h.number}, ${esc(h.sign)}">
          <td><b>H${h.number}</b>${h.number === 1 ? ' ✦' : ''}</td>
          <td>${esc(hg ? hg.heading : '')}</td>
          <td>${esc(h.sign)} <small class="muted">#${h.rashi_number || (h.sign_index + 1)}</small></td>
          <td>${esc(h.lord)} <small class="muted">(H${h.lord_house}${h.lord_sign ? ' · ' + h.lord_sign : ''})</small></td>
          <td>
            <div>${esc(occ)}</div>
            ${asp ? `<small class="muted">Drishti: ${esc(asp)}</small>` : ''}
          </td>
        </tr>
      `;
    }).join('');

    hRows.querySelectorAll('tr[data-inspect-house]').forEach(row => {
      bindInteractiveKeyOrClick(row, () => selectInspector('house', Number(row.dataset.inspectHouse)));
    });
  }

  selectInspector(state.selectedInspector.type, state.selectedInspector.id);
}

function renderCategoryTabs(categories, sections) {
  const wrap = $('category-tabs');
  if (!wrap) return;
  const items = [{ key: 'all', title: `${tr('allCategories')} (${sections.length})` }, ...(categories || [])];
  wrap.innerHTML = '';
  items.forEach(cat => {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.role = 'tab';
    const active = state.activeCategory === cat.key;
    btn.className = 'cat-tab' + (active ? ' active' : '');
    btn.setAttribute('aria-selected', String(active));
    btn.textContent = cat.title;
    btn.addEventListener('click', () => {
      state.activeCategory = cat.key;
      renderCategoryTabs(categories, sections);
      filterTopicPanels();
    });
    wrap.append(btn);
  });
}

function filterTopicPanels() {
  document.querySelectorAll('.topic-panel').forEach(panel => {
    const match = state.activeCategory === 'all' || panel.dataset.category === state.activeCategory;
    panel.classList.toggle('filtered-out', !match);
  });
}

function renderTopics(sections) {
  const root = $('topic-panels');
  root.innerHTML = '';
  sections.forEach((s, i) => {
    const panel = document.createElement('section');
    panel.className = 'report-panel topic-panel';
    panel.id = 'topic-' + s.key;
    panel.dataset.category = s.category || 'all';
    panel.innerHTML = `
      <div class="panel-kicker">${String(i + 2).padStart(2, '0')} / ${esc(s.category_title || '')} · ${esc(s.rule_id || '')}</div>
      <h3><span aria-hidden="true">${navIcons[s.key] || '✦'}</span> ${esc(s.title)}</h3>
      <div class="topic-meta">
        <span class="mini-tag">${esc(tr('housePrefix'))} ${s.primary_house}</span>
        <span class="mini-tag">${esc(tr('housePrefix'))} ${s.secondary_house}</span>
        ${s.karaka ? `<span class="mini-tag">Karaka: ${esc(s.karaka)}</span>` : ''}
      </div>

      <h4 class="sub-heading"><span class="dot-calc" aria-hidden="true">●</span> ${esc(tr('facts'))}</h4>
      <ul class="fact-list">${s.facts.map(f => `<li><span>${esc(f)}</span></li>`).join('')}</ul>

      ${s.why_factors ? `
      <details class="why-box">
        <summary>${esc(tr('whyThis'))}</summary>
        <p>${esc(s.why_factors)}</p>
      </details>` : ''}

      <h4 class="sub-heading"><span class="dot-trad" aria-hidden="true">◆</span> ${esc(tr('reading'))}</h4>
      <div class="interprets">${s.interpretation.map(a => `<p>${esc(a)}</p>`).join('')}</div>

      ${(s.possible_strengths || s.possible_challenges) ? `
      <div class="balance-grid">
        ${s.possible_strengths ? `<div class="balance-card strength-card"><strong>✦ ${esc(tr('strengthsHeading'))}</strong><p>${esc(s.possible_strengths)}</p></div>` : ''}
        ${s.possible_challenges ? `<div class="balance-card challenge-card"><strong>⚖ ${esc(tr('challengesHeading'))}</strong><p>${esc(s.possible_challenges)}</p></div>` : ''}
      </div>` : ''}

      <div class="reflection">
        <strong>✧ ${esc(tr('reflection'))}</strong>
        <p>${esc(s.reflection)}</p>
      </div>
      <p class="caution">${esc(s.note)}</p>
    `;
    root.append(panel);
  });
  filterTopicPanels();
}

function renderDashas(dashas) {
  let currentIdx = dashas.findIndex(d => d.current);
  if (currentIdx < 0) currentIdx = 0;
  const before = Math.max(0, currentIdx - 1);
  const show = dashas.slice(before, before + 9);
  $('dasha-list').innerHTML = show.map(d => `
    <div class="dasha-item ${d.current ? 'current' : ''}">
      <div class="dasha-name">
        <span class="planet-glyph" aria-hidden="true">${PLANET_GLYPHS[d.key] || '✦'}</span>
        ${esc(d.name)}
        ${d.years ? `<small class="muted">(${d.years} ${esc(tr('yearsLabel'))})</small>` : ''}
        ${d.current ? `<span class="current-pill">${esc(tr('current'))}</span>` : ''}
      </div>
      <div class="dasha-date">${esc(d.start)} → ${esc(d.end)}</div>
    </div>
  `).join('');
}

function buildNav(sections) {
  const choices = [
    ['chart', tr('positions'), 'chart-panel'],
    ...sections.map(s => [s.key, s.title, 'topic-' + s.key]),
    ['dasha', tr('periods'), 'dasha-panel'],
    ['method', tr('methodNav'), 'method-panel']
  ];
  const nav = $('nav-buttons');
  nav.innerHTML = '';
  choices.forEach(([key, label, target], i) => {
    const b = document.createElement('button');
    b.type = 'button';
    b.className = i === 0 ? 'active' : '';
    b.innerHTML = `<span class="nav-emoji" aria-hidden="true">${navIcons[key] || '✦'}</span><span>${esc(label)}</span>`;
    b.onclick = () => {
      document.querySelectorAll('#nav-buttons button').forEach(x => x.classList.remove('active'));
      b.classList.add('active');
      if (target.startsWith('topic-') && state.activeCategory !== 'all') {
        state.activeCategory = 'all';
        renderCategoryTabs(state.data.reading.categories, state.data.reading.sections);
        filterTopicPanels();
      }
      $(target)?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    };
    nav.append(b);
  });
}

function saveJSON() {
  if (!state.data) return;
  const exportCopy = JSON.parse(JSON.stringify(state.data));
  if ($('anon-export')?.checked) {
    exportCopy.name = tr('anonymous');
  }
  const content = JSON.stringify(exportCopy, null, 2);
  const blob = new Blob([content], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `kundali-saral-${state.lang}.json`;
  a.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

function init() {
  renderGlossary();
  getCities();

  $('birth-form').addEventListener('submit', e => {
    e.preventDefault();
    generate();
  });

  document.querySelectorAll('[data-lang]').forEach(b => {
    b.addEventListener('click', () => applyLanguage(b.dataset.lang));
  });

  document.querySelectorAll('[data-chart-style]').forEach(b => {
    b.addEventListener('click', () => applyChartStyle(b.dataset.chartStyle));
  });

  const devToggle = $('hinglish-devanagari');
  if (devToggle) {
    devToggle.addEventListener('change', () => {
      state.showHinglishDevanagari = devToggle.checked;
      if (state.data) renderChartsAndTables(state.data.chart, state.data.reading);
    });
  }

  const anonToggle = $('anon-export');
  if (anonToggle) {
    anonToggle.addEventListener('change', () => {
      if (state.data) renderResult(state.data);
    });
  }

  $('city').addEventListener('input', () => {
    state.city = null;
    $('lat').value = '';
    $('lon').value = '';
    $('tz').value = '';
    clearTimeout(state.searchTimer);
    state.searchTimer = setTimeout(citySearch, 300);
  });

  $('city').addEventListener('blur', () => setTimeout(() => showCities([]), 220));

  $('online-search-btn').addEventListener('click', async () => {
    const query = $('city').value.trim();
    if (query.length < 2) {
      formError(tr('locationRequired'));
      return;
    }
    const button = $('online-search-btn');
    button.disabled = true;
    try {
      const res = await fetch('/api/search-cities?q=' + encodeURIComponent(query));
      const data = await res.json();
      if (data.warning) formError(data.warning);
      showCities(data.cities || []);
    } catch {
      formError(tr('unknown'));
    } finally {
      button.disabled = false;
    }
  });

  $('demo-btn').addEventListener('click', () => {
    $('name').value = '';
    $('birth-date').value = '1998-08-15';
    $('birth-time').value = '08:30';
    if ($('time-uncertain')) $('time-uncertain').checked = false;
    if ($('dst-fold')) $('dst-fold').value = '';
    pickCity(
      state.cities.find(c => c.name === 'New Delhi') ||
      { name: 'New Delhi', country: 'India', latitude: 28.6139, longitude: 77.2090, time_zone: 'Asia/Kolkata' }
    );
    generate();
  });

  $('print-btn').addEventListener('click', () => window.print());
  $('json-btn').addEventListener('click', saveJSON);
}

init();
