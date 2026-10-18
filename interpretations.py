"""Transparent, localized, rule-based educational Jyotish readings across 17 life areas, 12 houses, 9 grahas, and 27 nakshatras."""

CATEGORIES = {
    'en': {
        'myself': 'Myself & Identity',
        'career_study': 'Career, Leadership & Study',
        'relationships': 'Love, Marriage & Community',
        'money_home': 'Money, Family & Home',
        'wellbeing_growth': 'Wellbeing, Travel & Growth',
    },
    'hinglish': {
        'myself': 'Main aur Meri Pehchaan',
        'career_study': 'Career, Leadership aur Padhai',
        'relationships': 'Pyaar, Shaadi aur Rishte',
        'money_home': 'Paisa, Parivaar aur Ghar',
        'wellbeing_growth': 'Sehat, Travel aur Personal Growth',
    },
    'hi': {
        'myself': 'स्वयं और पहचान',
        'career_study': 'करियर, नेतृत्व और शिक्षा',
        'relationships': 'प्रेम, विवाह और संबंध',
        'money_home': 'धन, परिवार और घर',
        'wellbeing_growth': 'सेहत, यात्रा और आत्म-विकास',
    },
}

# (key, category, primary_house, secondary_house, karaka_key, rule_id, en_title, hg_title, hi_title)
TOPICS = [
    ('personality', 'myself', 1, 3, 'sun', 'KS-BPHS-D1-01-SELF', 'Personality & identity', 'Apni pehchaan aur strengths', 'व्यक्तित्व और पहचान'),
    ('creativity', 'myself', 5, 3, 'venus', 'KS-BPHS-D1-13-CREATIVITY', 'Creativity & interests', 'Creativity aur interests', 'रचनात्मकता और रुचियाँ'),
    ('resilience', 'myself', 4, 12, 'moon', 'KS-BPHS-D1-12-EMOTION', 'Emotional resilience', 'Emotional balance aur mann', 'भावनात्मक संतुलन'),
    ('career', 'career_study', 10, 6, 'saturn', 'KS-BPHS-D1-02-CAREER', 'Career & profession', 'Career aur kaam', 'करियर और कार्यक्षेत्र'),
    ('entrepreneurship', 'career_study', 7, 11, 'mercury', 'KS-BPHS-D1-03-BUSINESS', 'Business & entrepreneurship', 'Business aur independent kaam', 'व्यापार और उद्यमिता'),
    ('education', 'career_study', 5, 9, 'jupiter', 'KS-BPHS-D1-04-EDUCATION', 'Education & learning', 'Padhai aur learning', 'शिक्षा और अध्ययन'),
    ('leadership', 'career_study', 10, 1, 'sun', 'KS-BPHS-D1-16-LEADERSHIP', 'Leadership & public image', 'Leadership aur public image', 'नेतृत्व और सामाजिक छवि'),
    ('love', 'relationships', 5, 7, 'venus', 'KS-BPHS-D1-05-LOVE', 'Love & dating', 'Pyaar aur rishte', 'प्रेम और अपनापन'),
    ('marriage', 'relationships', 7, 2, 'jupiter', 'KS-BPHS-D1-06-MARRIAGE', 'Marriage & partnership', 'Shaadi aur partnership', 'विवाह और साझेदारी'),
    ('friends', 'relationships', 11, 3, 'mercury', 'KS-BPHS-D1-07-FRIENDS', 'Friends & social life', 'Dost aur social circle', 'मित्रता और सामाजिक जीवन'),
    ('money', 'money_home', 2, 11, 'jupiter', 'KS-BPHS-D1-08-MONEY', 'Money & budgeting', 'Paisa aur savings', 'धन और बजट प्रबंधन'),
    ('family', 'money_home', 4, 2, 'moon', 'KS-BPHS-D1-09-FAMILY', 'Home, family & parents', 'Parivaar aur ghar', 'घर, परिवार और जड़ें'),
    ('children', 'money_home', 5, 4, 'jupiter', 'KS-BPHS-D1-10-NURTURING', 'Mentoring, children & nurturing', 'Nurturing aur care', 'देखभाल, मार्गदर्शन और संतान भाव'),
    ('health', 'wellbeing_growth', 6, 1, 'sun', 'KS-BPHS-D1-11-WELLBEING', 'Wellbeing & daily routine', 'Sehat aur daily routine', 'सेहत और दिनचर्या'),
    ('travel', 'wellbeing_growth', 9, 12, 'moon', 'KS-BPHS-D1-14-TRAVEL', 'Travel & new horizons', 'Travel aur naye experiences', 'यात्रा और नए अनुभव'),
    ('spirituality', 'wellbeing_growth', 9, 12, 'ketu', 'KS-BPHS-D1-15-VALUES', 'Values, meaning & philosophy', 'Values aur inner meaning', 'मूल्य, दर्शन और आत्मचिंतन'),
    ('growth', 'wellbeing_growth', 9, 6, 'saturn', 'KS-BPHS-D1-17-GROWTH', 'Personal growth & habits', 'Personal growth aur habits', 'व्यक्तिगत विकास और आदतें'),
]

# Exact 12-house headings from LANGUAGE_SYSTEM.md
HOUSE_HEADINGS = {
    'en': [
        'Self and identity', 'Family and resources', 'Effort and communication', 'Home and comfort',
        'Creativity and learning', 'Routine and challenges', 'Partnerships', 'Change and shared resources',
        'Beliefs and higher learning', 'Career and public life', 'Community and gains', 'Rest and introspection'
    ],
    'hinglish': [
        'Apni pehchaan', 'Parivaar aur paisa', 'Mehnat aur baatcheet', 'Ghar aur sukh',
        'Creativity aur padhai', 'Routine aur challenges', 'Rishte aur partnership', 'Badlav aur joint resources',
        'Vichaar aur higher learning', 'Career aur pehchaan', 'Dost aur goals', 'Aaram aur self-reflection'
    ],
    'hi': [
        'स्वयं और पहचान', 'परिवार और संसाधन', 'प्रयास और संवाद', 'घर और सुख',
        'रचनात्मकता और शिक्षा', 'दिनचर्या और चुनौतियाँ', 'संबंध और साझेदारी', 'परिवर्तन और साझा संसाधन',
        'दर्शन और उच्च शिक्षा', 'करियर और सार्वजनिक जीवन', 'समुदाय और लक्ष्य', 'विश्राम और आत्मचिंतन'
    ],
}

HOUSE_THEMES = {
    'en': [
        'personal identity, physical vitality and overall approach',
        'resources, savings, speech and close family values',
        'courage, communication, siblings and daily initiative',
        'home environment, emotional roots, motherly care and inner peace',
        'creativity, learning, joy, romance and mentoring',
        'daily work routines, service, problem-solving and practical habits',
        'one-to-one partnerships, marriage, agreements and mutual respect',
        'deep transitions, resilience, shared resources and research',
        'long-term philosophy, higher learning, mentors and ethical values',
        'career direction, public contribution, reputation and leadership',
        'friendships, community networks, aspirations and collaborative gains',
        'rest, solitude, letting go, distant horizons and quiet reflection'
    ],
    'hinglish': [
        'apni identity, vitality aur life ki general approach',
        'savings, resources, bolchaal aur family values',
        'mehnat, communication, initiative aur daily courage',
        'ghar ka mahaul, emotional roots aur sukoon',
        'creativity, padhai, खुशी (joy), romance aur mentoring',
        'daily routine, service, problem-solving aur practical habits',
        'equal partnerships, shaadi, agreements aur mutual respect',
        'bade badlav, resilience, shared resources aur deep understanding',
        'higher learning, mentors, life values aur long-term vision',
        'career direction, public life, kaam aur zimmewari',
        'dost, social networks, long-term goals aur teamwork',
        'aaram, solitude, travel aur quiet self-reflection'
    ],
    'hi': [
        'व्यक्तिगत पहचान, ऊर्जा और जीवन के प्रति दृष्टिकोण',
        'संसाधन, बचत, वाणी और पारिवारिक मूल्य',
        'प्रयास, संवाद, साहस और दैनिक पहल',
        'घर का वातावरण, भावनात्मक जड़ें और मानसिक शांति',
        'रचनात्मकता, अध्ययन, प्रेम और मार्गदर्शन',
        'दैनिक दिनचर्या, सेवा, समस्या-समाधान और व्यावहारिक आदतें',
        'साझेदारी, विवाह, आपसी समझौते और सम्मान',
        'गहरे परिवर्तन, धैर्य, साझा संसाधन और शोध',
        'उच्च शिक्षा, मार्गदर्शक, जीवन-दर्शन और नैतिक मूल्य',
        'करियर की दिशा, सामाजिक योगदान, प्रतिष्ठा और नेतृत्व',
        'मित्र समूह, सामुदायिक नेटवर्क, लक्ष्य और सामूहिक उपलब्धि',
        'विश्राम, एकांत, दूरस्थ अनुभव और आत्मचिंतन'
    ],
}
# Fix any accidental Devanagari in Hinglish HOUSE_THEMES[4]:
HOUSE_THEMES['hinglish'][4] = 'creativity, padhai, khushi, romance aur mentoring'

SIGN_QUALITIES = {
    'en': [
        'direct initiative, courage and brisk action',
        'steadiness, practical patience and reliability',
        'curiosity, dialogue and intellectual adaptability',
        'emotional care, protective warmth and belonging',
        'expressive confidence, dignity and creative warmth',
        'careful analysis, organization and helpful service',
        'balance, fairness and thoughtful cooperation',
        'emotional depth, focus and quiet determination',
        'broad-minded exploration, principle and optimism',
        'structured effort, realism and long-term endurance',
        'independent thinking, systems view and community focus',
        'empathetic imagination, synthesis and reflective calm'
    ],
    'hinglish': [
        'seedhi initiative, courage aur fast action',
        'stability, practical patience aur bharosa',
        'curiosity, baatcheet aur flexible soch',
        'emotional care, apnapan aur protective nature',
        'confidence, warmth aur creative self-expression',
        'detail-oriented soch, planning aur helpful nature',
        'balance, fairness aur mil-julkar kaam karna',
        'gehra focus, commitment aur strong determination',
        'khule vichaar, learning aur long-term optimism',
        'discipline, practical mehnat aur lamba patience',
        'nayi soch, systems approach aur community spirit',
        'empathy, imagination aur shant self-reflection'
    ],
    'hi': [
        'सीधी पहल, साहस और सक्रियता',
        'स्थिरता, व्यावहारिक धैर्य और विश्वसनीयता',
        'जिज्ञासा, संवाद और लचीली सोच',
        'भावनात्मक देखभाल, अपनापन और संवेदनशीलता',
        'आत्मविश्वास, गरिमा और रचनात्मक अभिव्यक्ति',
        'सूक्ष्म विश्लेषण, व्यवस्था और सहयोगी स्वभाव',
        'संतुलन, निष्पक्षता और आपसी तालमेल',
        'गंभीर एकाग्रता, निष्ठा और दृढ़ संकल्प',
        'व्यापक दृष्टिकोण, सीखने की रुचि और आशावाद',
        'अनुशासन, व्यावहारिक परिश्रम और दीर्घकालिक धैर्य',
        'मौलिक सोच, व्यापक समझ और सामुदायिक भावना',
        'कल्पनाशीलता, सहानुभूति और शांत आत्मचिंतन'
    ],
}

SIGN_CHALLENGES = {
    'en': [
        'pacing impatience and pausing before reacting quickly',
        'staying open to change when routines feel overly fixed',
        'finishing one priority before scattering focus across many ideas',
        'maintaining healthy boundaries without absorbing every mood around you',
        'sharing the spotlight and inviting feedback without defensiveness',
        'avoiding perfectionism or over-critiquing small details',
        'making timely decisions rather than over-weighing every side to please others',
        'letting go of old grievances and sharing concerns openly',
        'grounding big visions into everyday step-by-step follow-through',
        'balancing heavy responsibility with rest and emotional warmth',
        'staying emotionally present alongside abstract ideals',
        'keeping clear practical boundaries when feeling overwhelmed'
    ],
    'hinglish': [
        'jaldbazi se bachna aur react karne se pehle thoda rukna',
        'jab zaroorat ho tab naye badlav ke liye flexible rehna',
        'ek samay par bahut saare ideas mein focus bikharaane se bachna',
        'dusron ke mood ko apne upar haavi na hone dena aur boundaries rakhna',
        'feedback ko khule mann se lena aur ego ko beech mein na aane dena',
        'har chhoti baat mein over-thinking ya perfectionism se bachna',
        'sabko khush karne ke chakkar mein decision lene mein deri na karna',
        'purani baaton ko pakadkar na rakhna aur bharosa banana',
        'bade plans ke saath roz ke chhote steps par bhi dhyan dena',
        'kaam aur zimmewari ke beech aaram aur apno ke liye waqt nikalna',
        'sirf ideas mein rehne ke bajay emotional connection banaye rakhna',
        'overwhelm hone par clear aur practical boundaries banana'
    ],
    'hi': [
        'जल्दबाजी से बचना और प्रतिक्रिया देने से पहले थोड़ा रुकना',
        'आवश्यकता पड़ने पर बदलाव के प्रति लचीलापन बनाए रखना',
        'एक साथ कई विचारों में ध्यान भटकाने के बजाय प्राथमिकता तय करना',
        'स्वस्थ भावनात्मक सीमाएँ रखना और हर बात को मन पर न लेना',
        'सुझावों को खुले मन से स्वीकार करना',
        'अत्यधिक पूर्णतावाद या छोटी बातों की चिंता से बचना',
        'निर्णय लेने में अनावश्यक संकोच या देरी से बचना',
        'पुरानी बातों को छोड़कर संवाद को सरल रखना',
        'बड़े विचारों को दैनिक व्यवहार और नियमितता से जोड़ना',
        'जिम्मेदारियों के साथ विश्राम और आत्मीयता का संतुलन रखना',
        'वैचारिक दृष्टिकोण के साथ भावनात्मक जुड़ाव बनाए रखना',
        'अस्पष्टता से बचने के लिए व्यावहारिक सीमाएँ तय करना'
    ],
}

PLANET_MEANINGS = {
    'en': {
        'sun': 'vitality, self-confidence, integrity and healthy responsibility',
        'moon': 'emotional sensitivity, adaptability, memory and inner comfort',
        'mars': 'focused energy, courage, technical execution and clear boundaries',
        'mercury': 'communication, analytical clarity, learning and adaptability',
        'jupiter': 'wisdom, ethical perspective, teaching, synthesis and mentorship',
        'venus': 'appreciation, relationship harmony, art, comfort and diplomacy',
        'saturn': 'discipline, patience, realism, craft and long-term accountability',
        'rahu': 'unconventional curiosity, ambitious reach and crossing familiar boundaries',
        'ketu': 'detachment, internal reflection, simplification and intuitive focus',
    },
    'hinglish': {
        'sun': 'self-confidence, vitality, clarity aur zimmewari',
        'moon': 'emotions, mann ka sukoon, adaptability aur care',
        'mars': 'energy, courage, action lene ki kshamta aur boundaries',
        'mercury': 'communication, analytical samajh, learning aur logic',
        'jupiter': 'gyan, long-term samajh, guidance aur ethical values',
        'venus': 'rishton mein harmony, creativity, comfort aur balance',
        'saturn': 'discipline, patience, lagataar mehnat aur जिम्मेदारी (accountability)',
        'rahu': 'naye raaste, badi ambition aur out-of-the-box curiosity',
        'ketu': 'detachment, simplicity, gehra focus aur self-reflection',
    },
    'hi': {
        'sun': 'आत्मविश्वास, जीवन-ऊर्जा, स्पष्टता और जिम्मेदारी',
        'moon': 'भावनात्मक संवेदनशीलता, अनुकूलन क्षमता और मन की शांति',
        'mars': 'ऊर्जा, साहस, कार्य-क्षमता और स्पष्ट सीमाएँ',
        'mercury': 'संवाद, तार्किक विश्लेषण, सीखने की क्षमता और समझ',
        'jupiter': 'ज्ञान, व्यापक दृष्टिकोण, मार्गदर्शन और नैतिक मूल्य',
        'venus': 'संबंधों में सामंजस्य, सौंदर्य-बोध, कला और संतुलन',
        'saturn': 'अनुशासन, धैर्य, निरंतर परिश्रम और दीर्घकालिक निष्ठा',
        'rahu': 'नए रास्तों की खोज, महत्वाकांक्षा और लीक से हटकर सोच',
        'ketu': 'वैराग्य, आत्मचिंतन, सादगी और सूक्ष्म एकाग्रता',
    },
}
PLANET_MEANINGS['hinglish']['saturn'] = 'discipline, patience, lagataar mehnat aur accountability'

PROMPTS = {
    'en': {
        'personality': 'What daily habits make you feel most grounded and authentic to yourself?',
        'creativity': 'Which creative skill or curiosity do you want to practice purely for the joy of learning?',
        'resilience': 'What environment or routine helps you reset when your mind feels overloaded?',
        'career': 'Which core skill gives you the strongest sense of usefulness and steady progress at work?',
        'entrepreneurship': 'When taking independent initiative, how do you balance bold action with clear risk limits?',
        'education': 'Do you absorb complex subjects better through structured notes, hands-on practice, or discussion?',
        'leadership': 'How can you lead and take responsibility in a way that earns quiet trust rather than pressure?',
        'love': 'What does mutual respect, honest communication, and emotional safety look like for you?',
        'marriage': 'Which shared daily values and communication habits matter most in a long-term partnership?',
        'friends': 'Which friendships leave you feeling energized, respected, and aligned with your values?',
        'money': 'What simple, repeatable budgeting or saving habit would bring more calm to your month?',
        'family': 'What small conversation or boundary helps create warmth and peace at home?',
        'children': 'How do you like to nurture, mentor, or support the growth of younger people or creative projects?',
        'health': 'Which sustainable sleep, movement, or nutrition habit best supports your everyday energy?',
        'travel': 'What kind of new place or perspective broadens your thinking without exhausting your routine?',
        'spirituality': 'What personal values or contemplative practices help you find meaning during uncertain times?',
        'growth': 'Which single small habit, practiced consistently for 90 days, would improve your life the most?',
    },
    'hinglish': {
        'personality': 'Kaunsi roz ki aadat aapko sabse zyada confident aur grounded feel karati hai?',
        'creativity': 'Kaunsi creative skill ya hobby aap bina kisi pressure ke seekhna ya practice karna chahenge?',
        'resilience': 'Jab mann thaka hua ya overwhelmed ho, tab aapko shant hone mein kya sabse zyada help karta hai?',
        'career': 'Kaam mein kaunsi skill ko बेहतर (better) banana aapko sabse zyada satisfaction deta hai?',
        'entrepreneurship': 'Apना (apna) kaam ya initiative lete waqt aap risk aur planning ka balance kaise rakhte hain?',
        'education': 'Aap naye topics practice se, likhkar ya discussion karke sabse achhe se kaise seekhte hain?',
        'leadership': 'Zimmewari निभाते (nibhate) waqt aap team ke saath bharosa aur clarity kaise bana sakte hain?',
        'love': 'Ek healthy, barabari wale aur respectful rishte mein aapke liye sabse zaroori kya hai?',
        'marriage': 'Long-term partnership mein kaunsi values aur baatcheet ki aadatein sabse zyada maayne rakhti hain?',
        'friends': 'Kaunse dost aur groups aapko positive energy aur sahi support dete hain?',
        'money': 'Har mahine ki kaunsi simple saving ya budgeting habit aapki financial planning ko calm banayegi?',
        'family': 'Ghar mein sukoon aur apnapan badhane ke liye kaunsi chhoti pehal madadgar ho sakti hai?',
        'children': 'Aap kisi project, student ya chhote sadasya ko guide aur nurture karte waqt kya sikhana pasand karte hain?',
        'health': 'Neend, exercise ya routine ki kaunsi practical aadat aapki roz ki energy ko support karti hai?',
        'travel': 'Kis tarah ki jagah ya naye experiences aapki soch ko fresh aur open banate hain?',
        'spirituality': 'Kaunse life values ya quiet reflection aapko mushkil waqt mein clarity dete hain?',
        'growth': 'Agle 90 dinon mein kaunsi ek chhoti habit aapki life mein sabse achha badlav la sakti hai?',
    },
    'hi': {
        'personality': 'कौन-सी दैनिक आदतें आपको सबसे अधिक सहज और आत्मविश्वासी महसूस कराती हैं?',
        'creativity': 'कौन-सी रचनात्मक कला या कौशल आप केवल सीखने के आनंद के लिए अपनाना चाहेंगे?',
        'resilience': 'जब मन थका या उलझा हो, तब कौन-सा वातावरण या आदत आपको शांति देती है?',
        'career': 'कार्यक्षेत्र में किस कौशल को निखारना आपको सबसे अधिक संतोष देता है?',
        'entrepreneurship': 'स्वतंत्र पहल करते समय आप उत्साह और व्यावहारिक योजना के बीच संतुलन कैसे रखते हैं?',
        'education': 'आप अभ्यास, चर्चा या व्यवस्थित नोट्स में से किस माध्यम से सबसे अच्छा सीखते हैं?',
        'leadership': 'जिम्मेदारी निभाते समय आप सहयोग और विश्वास का वातावरण कैसे बना सकते हैं?',
        'love': 'आपके लिए सम्मानपूर्ण, पारदर्शी और बराबरी का संबंध कैसा दिखता है?',
        'marriage': 'दीर्घकालिक साझेदारी में कौन-से साझा मूल्य और संवाद की आदतें सबसे महत्वपूर्ण हैं?',
        'friends': 'कौन-सी मित्रता और संगति आपको सकारात्मक ऊर्जा और प्रेरणा देती है?',
        'money': 'कौन-सी सरल और नियमित बचत आदत आपके आर्थिक जीवन को अधिक संतुलित बना सकती है?',
        'family': 'घर में शांति और अपनापन बढ़ाने के लिए कौन-सा छोटा कदम उपयोगी हो सकता है?',
        'children': 'किसी नई रचना, विद्यार्थी या छोटों के मार्गदर्शन में आप किन मूल्यों को महत्व देते हैं?',
        'health': 'नींद, व्यायाम या भोजन से जुड़ी कौन-सी प्रमाण-आधारित आदत आपकी ऊर्जा को बनाए रखती है?',
        'travel': 'किस प्रकार की यात्रा या नए अनुभव आपके दृष्टिकोण को व्यापक बनाते हैं?',
        'spirituality': 'कौन-से जीवन-मूल्य या आत्मचिंतन के क्षण आपको दिशा और अर्थ देते हैं?',
        'growth': 'अगले 90 दिनों तक लगातार अपनाई गई कौन-सी एक छोटी आदत आपके लिए सबसे उपयोगी होगी?',
    },
}
# Ensure pure Roman script in Hinglish prompts:
PROMPTS['hinglish']['career'] = 'Kaam mein kaunsi skill ko better banana aapko sabse zyada satisfaction deta hai?'
PROMPTS['hinglish']['entrepreneurship'] = 'Apna kaam ya initiative lete waqt aap risk aur planning ka balance kaise rakhte hain?'
PROMPTS['hinglish']['leadership'] = 'Zimmewari nibhate waqt aap team ke saath bharosa aur clarity kaise bana sakte hain?'

# 27 Nakshatra dictionary in English, Hinglish, and Hindi
NAKSHATRA_THEMES = {
    'en': [
        'quick initiative, healing vitality and fresh beginnings',
        'steadfast endurance, responsibility and transformative discipline',
        'sharp discernment, purifying focus and protective warmth',
        'creative growth, fertility of ideas and steady artistic care',
        'gentle curiosity, searching intellect and adaptable exploration',
        'deep emotional processing, analytical honesty and renewal after storms',
        'return to balance, resilience, renewal and hospitable wisdom',
        'patient nourishment, ethical steadiness and supportive service',
        'penetrating insight, psychological depth and cautious boundaries',
        'dignified heritage, leadership responsibility and respect for roots',
        'warmth, creative rest, affection and generous companionship',
        'dependable agreements, service-minded partnership and steady loyalty',
        'skilled craftsmanship, practical dexterity and hands-on clarity',
        'structural design, aesthetic precision and well-crafted expression',
        'independent movement, diplomatic flexibility and self-reliant learning',
        'single-pointed determination, purposeful alliances and patient milestone building',
        'devoted friendship, cooperative bridge-building and steady resilience',
        'protective seniority, crisis composure and seasoned responsibility',
        'getting to root causes, investigative courage and letting go of non-essentials',
        'invigorating conviction, emotional candor and rejuvenating enthusiasm',
        'enduring integrity, universal principles and patient completion',
        'attentive listening, learning through dialogue and thoughtful synthesis',
        'rhythmic coordination, resourcefulness and collaborative timing',
        'systems thinking, independent research and restorative boundaries',
        'intense conviction, philosophical depth and dedicated reform',
        'deep stability, compassionate endurance and grounded wisdom',
        'safe guidance, empathetic completion and imaginative synthesis',
    ],
    'hinglish': [
        'fast initiative, fresh beginnings aur active energy',
        'discipline, zimmewari aur steady endurance',
        'clear focus, sachai aur protective warmth',
        'creative growth, stability aur artistic care',
        'curiosity, nayi khoj aur flexible learning',
        'gehra analysis, emotional honesty aur fresh start',
        'wapas balance paana, optimism aur supportive nature',
        'patient care, discipline aur helpful guidance',
        'deep observation, sharp intuition aur careful boundaries',
        'apni roots ki respect, leadership aur dignity',
        'warmth, creativity, joy aur supportive companionship',
        'bharosemand commitments, partnership aur steady help',
        'practical skill, haathon ka hunar aur clear execution',
        'design sense, balance aur sunder planning',
        'independent soch, flexibility aur polite diplomacy',
        'lamba focus, strong goals aur step-by-step mehnat',
        'pakki dosti, teamwork aur mushkil mein balance rakhna',
        'zimmewari lena, maturity aur protective guidance',
        'har baat ki jad (root) tak jaana aur sachai samajhna',
        'utsah, honest feelings aur nayi energy',
        'strong values, patience aur kaam ko poora karna',
        'dhyan se sunna, seekhna aur samajhdari se jodna',
        'sahi timing, teamwork aur practical resourcefulness',
        'deep research, independent soch aur healthy boundaries',
        'gehra vishwas, reform aur dedicated focus',
        'shant stability, patience aur grounded samajh',
        'empathy, safe guidance aur creative completion',
    ],
    'hi': [
        'त्वरित पहल, नई शुरुआत और सक्रिय ऊर्जा',
        'धैर्य, जिम्मेदारी और अनुशासित प्रयास',
        'स्पष्ट विवेक, एकाग्रता और संरक्षण की भावना',
        'रचनात्मक विकास, स्थिरता और सृजनशीलता',
        'जिज्ञासा, अन्वेषण और लचीली अध्ययन-वृत्ति',
        'गहन विश्लेषण, भावनात्मक ईमानदारी और नया आरंभ',
        'संतुलन की वापसी, आशावाद और सहयोगी स्वभाव',
        'पोषण, धैर्य, कर्तव्यनिष्ठा और शांत सेवा',
        'सूक्ष्म अवलोकन, मनोवैज्ञानिक गहराई और स्पष्ट सीमाएँ',
        'परंपरा का सम्मान, नेतृत्व और आत्म-गरिमा',
        'स्नेह, रचनात्मक उत्साह और सहृदयता',
        'विश्वसनीय वचनबद्धता, सहयोग और स्थिर साझेदारी',
        'व्यावहारिक कौशल, दक्षता और स्पष्ट कार्यशैली',
        'संतुलित संरचना, कला-बोध और सुघड़ अभिव्यक्ति',
        'स्वतंत्र विचार, लचीलापन और विनम्र संवाद',
        'लक्ष्य के प्रति एकाग्रता, धैर्य और निरंतर प्रयास',
        'मैत्री, समन्वय और कठिन समय में संतुलन',
        'परिपक्व जिम्मेदारी, संरक्षण और गंभीर समझ',
        'मूल कारणों की खोज, साहस और अनावश्यक को छोड़ना',
        'उत्साह, आत्मविश्वास और भावनात्मक स्पष्टता',
        'स्थायी सिद्धांत, धैर्य और कार्य को पूर्णता तक ले जाना',
        'ध्यानपूर्वक सुनना, सीखना और विचारों का समन्वय',
        'लयबद्ध समन्वय, व्यवहारकुशलता और सामूहिक तालमेल',
        'स्वतंत्र शोध, व्यवस्थागत समझ और स्वस्थ एकांत',
        'गंभीर निष्ठा, वैचारिक गहराई और सुधार की भावना',
        'शांत स्थिरता, करुणा और परिपक्व धैर्य',
        'सहानुभूति, सुरक्षित मार्गदर्शन और कल्पनाशील पूर्णता',
    ],
}

GLOSSARY = {
    'en': [
        {'term': 'Lagna (Ascendant)', 'short': 'The zodiac sign rising on the eastern horizon at your exact birth time and place; it marks House 1.'},
        {'term': 'Rashi (Zodiac Sign)', 'short': 'One of the 12 equal 30° sidereal zodiac segments (Aries to Pisces) calculated with Lahiri ayanamsa.'},
        {'term': 'Bhava (House)', 'short': 'One of the 12 life areas (self, resources, work, relationships, etc.). In Whole Sign houses, each sign equals one house.'},
        {'term': 'Graha (Planet / Node)', 'short': 'The 9 celestial markers in Jyotish: Sun, Moon, Mars, Mercury, Jupiter, Venus, Saturn, plus the lunar nodes Rahu and Ketu.'},
        {'term': 'Nakshatra & Pada', 'short': 'One of the 27 equal lunar constellations (13°20′ each), divided into 4 quarters (padas) of 3°20′.'},
        {'term': 'Mahadasha', 'short': 'Traditional Vimshottari planetary time cycles started from the Moon’s birth Nakshatra position.'},
        {'term': 'Drishti (Aspect)', 'short': 'Traditional Parashari directional sight cast by a graha onto other houses (all 7 planets aspect the 7th house from themselves; Mars, Jupiter, and Saturn have special aspects).'},
        {'term': 'Vakri (Retrograde)', 'short': 'When a planet appears to move backward along the zodiac from Earth’s perspective; Sun and Moon are never retrograde.'},
    ],
    'hinglish': [
        {'term': 'Lagna (Ascendant)', 'short': 'Aapke exact birth time aur place par eastern horizon par udit hone wali rashi; yahi House 1 banti hai.'},
        {'term': 'Rashi (Zodiac Sign)', 'short': 'Sidereal zodiac ke 12 barabar (30°) hisse — Mesh se Meen tak (Lahiri ayanamsa ke saath).'},
        {'term': 'Bhav (House)', 'short': 'Kundali ke 12 life areas (jaise self, paisa, career, rishte). Whole-sign system mein ek rashi poora ek bhav hoti hai.'},
        {'term': 'Graha (9 Bodies)', 'short': 'Jyotish ke 9 graha: Surya, Chandra, Mangal, Budh, Guru, Shukra, Shani aur do lunar nodes Rahu-Ketu.'},
        {'term': 'Nakshatra aur Pada', 'short': 'Zodiac ke 27 barabar nakshatra (har ek 13°20′), aur har nakshatra ke 4 charan (pada, 3°20′).'},
        {'term': 'Mahadasha', 'short': 'Chandra ke birth nakshatra se shuru hone wale traditional Vimshottari time periods.'},
        {'term': 'Drishti (Aspect)', 'short': 'Parashari parampara mein graha ki doosre bhavon par drishti (sabhi 7 graha apne se 7th bhav ko dekhte hain; Mangal, Guru, Shani ki vishesh drishti bhi hoti hai).'},
        {'term': 'Vakri (Retrograde)', 'short': 'Jab Prithvi se dekhne par koi graha peeche chalta hua dikhta hai; Surya aur Chandra kabhi vakri nahi hote.'},
    ],
    'hi': [
        {'term': 'लग्न (Ascendant)', 'short': 'आपके जन्म के सटीक समय और स्थान पर पूर्वी क्षितिज पर उदित होने वाली राशि; यही प्रथम भाव (H1) होती है।'},
        {'term': 'राशि (Zodiac Sign)', 'short': 'निरयन राशिचक्र के 12 बराबर (30°) भाग — मेष से मीन तक (लाहिड़ी अयनांश के अनुसार)।'},
        {'term': 'भाव (House)', 'short': 'कुंडली के 12 जीवन-क्षेत्र (स्वयं, धन, करियर, संबंध आदि)। पूर्ण-राशि पद्धति में एक राशि पूरा एक भाव होती है।'},
        {'term': 'ग्रह (9 Grahas)', 'short': 'ज्योतिष के 9 ग्रह: सूर्य, चंद्र, मंगल, बुध, गुरु, शुक्र, शनि तथा दो छाया ग्रह (चंद्र पात) राहु और केतु।'},
        {'term': 'नक्षत्र और चरण (Pada)', 'short': 'राशिचक्र के 27 समान नक्षत्र (प्रत्येक 13°20′) और प्रत्येक नक्षत्र के 4 चरण (प्रत्येक 3°20′)।'},
        {'term': 'महादशा (Mahadasha)', 'short': 'जन्म के चंद्र नक्षत्र से प्रारंभ होने वाले पारंपरिक विंशोत्तरी समय-चक्र।'},
        {'term': 'दृष्टि (Aspect)', 'short': 'पाराशरी परंपरा के अनुसार ग्रह की अन्य भावों पर दृष्टि (सभी 7 ग्रह अपने से सप्तम भाव को देखते हैं; मंगल, गुरु और शनि की विशेष दृष्टियाँ भी होती हैं)।'},
        {'term': 'वक्री (Retrograde)', 'short': 'जब पृथ्वी से देखने पर कोई ग्रह राशिचक्र में पीछे की ओर गति करता प्रतीत होता है; सूर्य और चंद्र कभी वक्री नहीं होते।'},
    ],
}


def _build_house_guide(chart, lang):
    out = []
    for h in chart['houses']:
        idx = h['sign_index']
        n = h['number']
        heading = HOUSE_HEADINGS[lang][n - 1]
        theme = HOUSE_THEMES[lang][n - 1]
        occ = h['planets']
        asp = h.get('aspected_by', [])
        if lang == 'hi':
            occ_text = (
                f'इस भाव में {", ".join(p["name"] + " (" + p["dms"] + ")" for p in occ)} स्थित हैं।'
                if occ else
                'इस भाव में कोई ग्रह स्थित नहीं है (खाली भाव अशुभ नहीं होता; इसका अर्थ भाव के स्वामी से समझा जाता है)।'
            )
            asp_text = (
                f'पाराशरी दृष्टि: {", ".join(a["name"] + " (भाव " + str(a["from_house"]) + " से)" for a in asp)}।'
                if asp else
                'इस भाव पर किसी सप्त-ग्रह की सीधी पूर्ण-राशि दृष्टि नहीं है।'
            )
            summary = (
                f'भाव {n} ({heading}) में {h["sign"]} राशि है। '
                f'इसके स्वामी {h["lord"]} भाव {h["lord_house"]} ({h["lord_sign"]}) में स्थित हैं।'
            )
        elif lang == 'hinglish':
            occ_text = (
                f'Is bhav mein {", ".join(p["name"] + " (" + p["dms"] + ")" for p in occ)} baithe hain.'
                if occ else
                'Is bhav mein koi graha nahi hai (empty house ka matlab bad result nahi hota; iska context house lord se dekha jaata hai).'
            )
            asp_text = (
                f'Parashari drishti: {", ".join(a["name"] + " (House " + str(a["from_house"]) + " se)" for a in asp)}.'
                if asp else
                'Is bhav par kisi 7-graha ki direct whole-sign drishti nahi hai.'
            )
            summary = (
                f'House {n} ({heading}) mein {h["sign"]} rashi hai. '
                f'Iske lord {h["lord"]} House {h["lord_house"]} ({h["lord_sign"]}) mein hain.'
            )
        else:
            occ_text = (
                f'Occupied by {", ".join(p["name"] + " (" + p["dms"] + ")" for p in occ)}.'
                if occ else
                'No planets occupy this house (an empty house is normal and not negative; readers look to the house ruler instead).'
            )
            asp_text = (
                f'Parashari whole-sign aspects from: {", ".join(a["name"] + " (from H" + str(a["from_house"]) + ")" for a in asp)}.'
                if asp else
                'No direct classical Parashari whole-sign aspect on this house.'
            )
            summary = (
                f'House {n} ({heading}) contains {h["sign"]}. '
                f'Its ruler {h["lord"]} is placed in House {h["lord_house"]} ({h["lord_sign"]}).'
            )
        out.append({
            'number': n,
            'heading': heading,
            'theme': theme,
            'sign': h['sign'],
            'rashi_number': h['rashi_number'],
            'lord': h['lord'],
            'lord_house': h['lord_house'],
            'lord_sign': h['lord_sign'],
            'summary': summary,
            'occupants_text': occ_text,
            'aspects_text': asp_text,
            'planets': occ,
        })
    return out


def _build_planet_guide(chart, lang):
    out = []
    for p in chart['planets']:
        k = p['key']
        meaning = PLANET_MEANINGS[lang][k]
        house_heading = HOUSE_HEADINGS[lang][p['house'] - 1]
        if lang == 'hi':
            node_note = 'राहु और केतु भौतिक पिंड नहीं, बल्कि चंद्रमा की कक्षा के दो गणितीय बिंदु (छाया ग्रह) हैं।' if p['is_node'] else 'यह सौरमंडल का एक प्रत्यक्ष खगोलीय पिंड है।'
            retro_note = 'यह जन्म समय पर वक्री (प्रतीत होने वाली उल्टी गति में) था।' if p['retrograde'] else ''
            desc = (
                f'{p["name"]} आपकी कुंडली में {p["sign"]} राशि ({p["dms"]}) और भाव {p["house"]} ({house_heading}) में है, '
                f'तथा {p["nakshatra"]} नक्षत्र (चरण {p["pada"]}, स्वामी {p["nakshatra_lord"]}) में स्थित है। '
                f'पारंपरिक ज्योतिष में {p["name"]} को {meaning} से जोड़ा जाता है।'
            )
        elif lang == 'hinglish':
            node_note = 'Rahu aur Ketu physical planets nahi hain, balki Moon ke orbit ke mathematical lunar nodes (Chhaya Graha) hain.' if p['is_node'] else 'Yeh ek astronomical celestial body hai.'
            retro_note = 'Janam ke waqt yeh Vakri (retrograde motion mein) tha.' if p['retrograde'] else ''
            desc = (
                f'{p["name"]} aapki chart mein {p["sign"]} rashi ({p["dms"]}) aur House {p["house"]} ({house_heading}) mein hai, '
                f'aur {p["nakshatra"]} nakshatra (Pada {p["pada"]}, lord {p["nakshatra_lord"]}) mein aata hai. '
                f'Traditional Jyotish mein {p["name"]} ko {meaning} ka karaka maana jaata hai.'
            )
        else:
            node_note = 'Rahu and Ketu are mathematical lunar nodes (ecliptic intersection points), not physical planets.' if p['is_node'] else 'Astronomical solar-system body.'
            retro_note = 'Retrograde (apparent backward motion) at birth.' if p['retrograde'] else ''
            desc = (
                f'{p["name"]} is placed in {p["sign"]} ({p["dms"]}) in House {p["house"]} ({house_heading}), '
                f'within {p["nakshatra"]} Nakshatra (Pada {p["pada"]}, ruled by {p["nakshatra_lord"]}). '
                f'Traditionally, {p["name"]} symbolizes {meaning}.'
            )
        out.append({
            'key': k,
            'name': p['name'],
            'name_en': p['name_en'],
            'name_hinglish': p['name_hinglish'],
            'name_hi': p['name_hi'],
            'sign': p['sign'],
            'house': p['house'],
            'house_heading': house_heading,
            'degrees': p['degrees'],
            'dms': p['dms'],
            'nakshatra': p['nakshatra'],
            'pada': p['pada'],
            'nakshatra_lord': p['nakshatra_lord'],
            'retrograde': p['retrograde'],
            'is_node': p['is_node'],
            'dignity': p['dignity'],
            'meaning': meaning,
            'description': desc,
            'node_note': node_note,
            'retro_note': retro_note,
        })
    return out


def reading(chart, lang='en'):
    if lang not in ('en', 'hi', 'hinglish'):
        lang = 'en'
    by_key = {p['key']: p for p in chart['planets']}
    time_uncertain = chart.get('birth', {}).get('time_uncertain', False)

    sections = []
    for key, cat_key, primary, secondary, karaka_key, rule_id, en, hg, hi in TOPICS:
        h = chart['houses'][primary - 1]
        s = chart['houses'][secondary - 1]
        karaka = by_key[karaka_key]
        occupants = h['planets']
        second_occupants = s['planets']
        cat_title = CATEGORIES[lang][cat_key]

        if lang == 'hi':
            label = hi
            why_factors = (
                f'नियम {rule_id}: पारंपरिक पाराशरी पद्धति में "{hi}" के लिए मुख्य भाव {primary} ({HOUSE_HEADINGS["hi"][primary - 1]}), '
                f'सहायक भाव {secondary} ({HOUSE_HEADINGS["hi"][secondary - 1]}), उनके भावेश ({h["lord"]}, {s["lord"]}) और कारक ग्रह {karaka["name"]} का अध्ययन किया जाता है।'
            )
            f1 = f'मुख्य {primary}वें भाव ({HOUSE_HEADINGS["hi"][primary - 1]}) में {h["sign"]} राशि है। इसके स्वामी {h["lord"]} {h["lord_house"]}वें भाव ({h["lord_sign"]}) में हैं।'
            f2 = f'सहायक {secondary}वें भाव ({HOUSE_HEADINGS["hi"][secondary - 1]}) में {s["sign"]} राशि है; इसके स्वामी {s["lord"]} {s["lord_house"]}वें भाव ({s["lord_sign"]}) में हैं।'
            if occupants:
                f3 = f'मुख्य भाव {primary} में {", ".join(p["name"] + " (" + p["dms"] + ")" for p in occupants)} स्थित हैं।'
                interp = (
                    f'पारंपरिक ज्योतिष में भाव {primary} में {occupants[0]["name"]} की उपस्थिति को {PLANET_MEANINGS["hi"][occupants[0]["key"]]} '
                    f'के विषयों से जोड़ा जाता है, विशेषकर {h["sign"]} राशि के {SIGN_QUALITIES["hi"][h["sign_index"]]} के संदर्भ में।'
                )
            else:
                f3 = f'मुख्य भाव {primary} में कोई ग्रह स्थित नहीं है। खाली भाव का अर्थ नकारात्मक परिणाम नहीं होता; इसका संकेत भावेश {h["lord"]} से देखा जाता है।'
                interp = (
                    f'{h["sign"]} राशि के प्रभाव से इस क्षेत्र में {SIGN_QUALITIES["hi"][h["sign_index"]]} की भूमिका महत्वपूर्ण मानी जाती है।'
                )
            f4 = f'इस विषय के कारक ग्रह {karaka["name"]} भाव {karaka["house"]} ({karaka["sign"]}, {karaka["dms"]}, {karaka["dignity"]}) में स्थित हैं।'
            bridge = (
                f'भावेश {h["lord"]} के {h["lord_house"]}वें भाव में होने से यह क्षेत्र {HOUSE_THEMES["hi"][h["lord_house"] - 1]} से जुड़ता है, '
                f'और {karaka["name"]} ({PLANET_MEANINGS["hi"][karaka_key]}) इसे अतिरिक्त दिशा देता है।'
            )
            strength = f'संभावित सबल पक्ष: {h["sign"]} और {h["lord"]} के मेल से {SIGN_QUALITIES["hi"][h["sign_index"]]} तथा {PLANET_MEANINGS["hi"][h["lord_key"]]} को व्यवहार में लाने की क्षमता।'
            challenge = f'संतुलन बिंदु: {SIGN_CHALLENGES["hi"][h["sign_index"]]} के प्रति सजग रहना उपयोगी रहेगा।'
            note = 'ये ज्योतिष की पारंपरिक व्याख्याएँ हैं, निश्चित भविष्यवाणियाँ या वैज्ञानिक निष्कर्ष नहीं।'
            if time_uncertain:
                note += ' चूँकि जन्म समय अनुमानित है, इसलिए लग्न और भाव संख्या बदलने की संभावना रहती है।'

        elif lang == 'hinglish':
            label = hg
            why_factors = (
                f'Rule {rule_id}: Traditional Parashari Jyotish mein "{hg}" ko samajhne ke liye main House {primary} ({HOUSE_HEADINGS["hinglish"][primary - 1]}), '
                f'supporting House {secondary} ({HOUSE_HEADINGS["hinglish"][secondary - 1]}), unke lords ({h["lord"]}, {s["lord"]}) aur karaka graha {karaka["name"]} ko dekha jaata hai.'
            )
            f1 = f'Main {primary}th bhav ({HOUSE_HEADINGS["hinglish"][primary - 1]}) mein {h["sign"]} rashi hai. Iske lord {h["lord"]} {h["lord_house"]}th bhav ({h["lord_sign"]}) mein hain.'
            f2 = f'Supporting {secondary}th bhav ({HOUSE_HEADINGS["hinglish"][secondary - 1]}) mein {s["sign"]} rashi hai; iske lord {s["lord"]} {s["lord_house"]}th bhav ({s["lord_sign"]}) mein hain.'
            if occupants:
                f3 = f'Main House {primary} mein {", ".join(p["name"] + " (" + p["dms"] + ")" for p in occupants)} baithe hain.'
                interp = (
                    f'Traditional Jyotish mein House {primary} mein {occupants[0]["name"]} ko {PLANET_MEANINGS["hinglish"][occupants[0]["key"]]} '
                    f'aur {h["sign"]} rashi ke {SIGN_QUALITIES["hinglish"][h["sign_index"]]} se jodkar dekha jaata hai.'
                )
            else:
                f3 = f'Main House {primary} mein koi listed graha nahi hai. Empty house ka matlab bad result bilkul nahi hota; iska meaning lord {h["lord"]} se dekhte hain.'
                interp = (
                    f'{h["sign"]} rashi ki wajah se is area mein {SIGN_QUALITIES["hinglish"][h["sign_index"]]} ka natural role dekha jaata hai.'
                )
            f4 = f'Is topic ke karaka graha {karaka["name"]} House {karaka["house"]} ({karaka["sign"]}, {karaka["dms"]}, {karaka["dignity"]}) mein placed hain.'
            bridge = (
                f'Kyunki lord {h["lord"]} {h["lord_house"]}th bhav mein hain, yeh area {HOUSE_THEMES["hinglish"][h["lord_house"] - 1]} se connect hota hai, '
                f'aur {karaka["name"]} ({PLANET_MEANINGS["hinglish"][karaka_key]}) ismein apna context jodta hai.'
            )
            strength = f'Possible strength: {h["sign"]} aur {h["lord"]} ke combination se {SIGN_QUALITIES["hinglish"][h["sign_index"]]} aur {PLANET_MEANINGS["hinglish"][h["lord_key"]]} ko develop karne ka scope.'
            challenge = f'Dhyan rakhne wali baat: {SIGN_CHALLENGES["hinglish"][h["sign_index"]]}.'
            note = 'Yeh traditional interpretations hain, guaranteed future predictions ya scientific facts nahi.'
            if time_uncertain:
                note += ' Kyunki birth time approximate hai, Lagna aur house numbers shift ho sakte hain.'

        else:
            label = en
            why_factors = (
                f'Rule {rule_id}: In traditional Parashari Jyotish, "{en}" is examined through primary House {primary} ({HOUSE_HEADINGS["en"][primary - 1]}), '
                f'supporting House {secondary} ({HOUSE_HEADINGS["en"][secondary - 1]}), their rulers ({h["lord"]}, {s["lord"]}), and significator (karaka) {karaka["name"]}.'
            )
            f1 = f'Primary House {primary} ({HOUSE_HEADINGS["en"][primary - 1]}) falls in {h["sign"]}. Its ruler {h["lord"]} is placed in House {h["lord_house"]} ({h["lord_sign"]}).'
            f2 = f'Supporting House {secondary} ({HOUSE_HEADINGS["en"][secondary - 1]}) is in {s["sign"]}; its ruler {s["lord"]} is in House {s["lord_house"]} ({s["lord_sign"]}).'
            if occupants:
                f3 = f'{", ".join(p["name"] + " (" + p["dms"] + ")" for p in occupants)} {"occupies" if len(occupants) == 1 else "occupy"} primary House {primary}.'
                interp = (
                    f'Traditional Jyotish links {occupants[0]["name"]} in House {primary} with themes of {PLANET_MEANINGS["en"][occupants[0]["key"]]}, '
                    f'colored by {h["sign"]} qualities of {SIGN_QUALITIES["en"][h["sign_index"]]}.'
                )
            else:
                f3 = f'No planets occupy primary House {primary}. An empty house is completely normal and not negative; readers follow its ruler {h["lord"]} instead.'
                interp = (
                    f'With {h["sign"]} on House {primary}, traditional interpretation highlights themes of {SIGN_QUALITIES["en"][h["sign_index"]]}.'
                )
            f4 = f'Significator (karaka) {karaka["name"]} is in House {karaka["house"]} ({karaka["sign"]}, {karaka["dms"]}, {karaka["dignity"]}).'
            bridge = (
                f'Because house ruler {h["lord"]} sits in House {h["lord_house"]}, this life area connects symbolically with {HOUSE_THEMES["en"][h["lord_house"] - 1]}, '
                f'while {karaka["name"]} adds themes of {PLANET_MEANINGS["en"][karaka_key]}.'
            )
            strength = f'Potential strength: leaning into {h["sign"]} qualities of {SIGN_QUALITIES["en"][h["sign_index"]]} alongside {h["lord"]} themes of {PLANET_MEANINGS["en"][h["lord_key"]]}.'
            challenge = f'Potential challenge to balance: {SIGN_CHALLENGES["en"][h["sign_index"]]}.'
            note = 'These are traditional cultural interpretations for self-reflection, not guaranteed outcomes or scientific findings.'
            if time_uncertain:
                note += ' Because birth time is marked uncertain, Ascendant and house numbers may change if the actual birth time differs.'

        sections.append({
            'key': key,
            'category': cat_key,
            'category_title': cat_title,
            'title': label,
            'rule_id': rule_id,
            'primary_house': primary,
            'secondary_house': secondary,
            'karaka_key': karaka_key,
            'karaka': karaka['name'],
            'why_factors': why_factors,
            'facts': [f1, f2, f3, f4],
            'interpretation': [interp, bridge],
            'possible_strengths': strength,
            'possible_challenges': challenge,
            'reflection': PROMPTS[lang][key],
            'note': note,
        })

    lagna = chart['lagna']['sign']
    idx = chart['lagna']['sign_index']
    nak_idx = chart['nakshatra']['index']
    nak_theme = NAKSHATRA_THEMES[lang][nak_idx]

    if lang == 'hi':
        summary = (
            f'आपका लग्न {lagna} ({chart["lagna"]["dms"]}), चंद्र राशि {chart["moon_sign"]}, सूर्य राशि {chart["sun_sign"]} '
            f'और जन्म नक्षत्र {chart["nakshatra"]["name"]} (चरण {chart["nakshatra"]["pada"]}, स्वामी {chart["nakshatra"]["lord"]}) है।'
        )
        intro = (
            f'पारंपरिक ज्योतिष में {lagna} लग्न को {SIGN_QUALITIES["hi"][idx]} तथा {chart["nakshatra"]["name"]} नक्षत्र को '
            f'{nak_theme} के विषयों से जोड़ा जाता है। इसे आत्मचिंतन की भाषा की तरह लें, तय भविष्यवाणी नहीं।'
        )
        uncertainty_banner = (
            'जन्म समय अनिश्चित के रूप में चिह्नित है: लग्न (Ascendant) लगभग हर 2 घंटे में बदलता है, इसलिए जन्म समय में अंतर होने पर लग्न और 12 भाव बदल सकते हैं। चंद्र राशि और नक्षत्र तुलनात्मक रूप से अधिक स्थिर रहते हैं।'
            if time_uncertain else ''
        )
    elif lang == 'hinglish':
        summary = (
            f'Aapka Lagna {lagna} ({chart["lagna"]["dms"]}), Chandra Rashi {chart["moon_sign"]}, Surya Rashi {chart["sun_sign"]} '
            f'aur Janam Nakshatra {chart["nakshatra"]["name"]} (Pada {chart["nakshatra"]["pada"]}, lord {chart["nakshatra"]["lord"]}) hai.'
        )
        intro = (
            f'Traditional Jyotish mein {lagna} Lagna ko {SIGN_QUALITIES["hinglish"][idx]} aur {chart["nakshatra"]["name"]} Nakshatra ko '
            f'{nak_theme} se connect karte hain. Yeh self-reflection ka tool hai, fixed prediction nahi.'
        )
        uncertainty_banner = (
            'Birth time uncertain mark kiya gaya hai: Lagna lagbhag har 2 ghante mein badalta hai, isliye agar birth time exact nahi hai toh Lagna aur 12 houses shift ho sakte hain. Chandra Rashi aur Nakshatra zyada stable rehte hain.'
            if time_uncertain else ''
        )
    else:
        summary = (
            f'Your Ascendant (Lagna) is {lagna} ({chart["lagna"]["dms"]}), Moon sign is {chart["moon_sign"]}, Sun sign is {chart["sun_sign"]}, '
            f'and birth Nakshatra is {chart["nakshatra"]["name"]} (Pada {chart["nakshatra"]["pada"]}, ruled by {chart["nakshatra"]["lord"]}).'
        )
        intro = (
            f'Traditional Jyotish associates {lagna} Ascendant with {SIGN_QUALITIES["en"][idx]}, and {chart["nakshatra"]["name"]} Nakshatra with '
            f'{nak_theme}. Use these themes as prompts for reflection rather than fixed labels.'
        )
        uncertainty_banner = (
            'Birth time is marked uncertain: because the Ascendant (Lagna) shifts roughly every two hours, house placements may change if the exact birth time differs. Moon sign and Nakshatra are much less sensitive to small time differences.'
            if time_uncertain else ''
        )

    return {
        'summary': summary,
        'intro': intro,
        'uncertainty_banner': uncertainty_banner,
        'categories': [{'key': k, 'title': v} for k, v in CATEGORIES[lang].items()],
        'sections': sections,
        'house_guide': _build_house_guide(chart, lang),
        'planet_guide': _build_planet_guide(chart, lang),
        'nakshatra_guide': {
            'index': nak_idx,
            'name': chart['nakshatra']['name'],
            'pada': chart['nakshatra']['pada'],
            'lord': chart['nakshatra']['lord'],
            'theme': nak_theme,
        },
        'glossary': GLOSSARY[lang],
    }
