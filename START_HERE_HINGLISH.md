> **Naya Antigravity upgrade kit:** Detailed steps ke liye `START_HERE_ANTIGRAVITY.md` aur full build instruction ke liye `ANTIGRAVITY_PROMPT.md` padhein. Abhi existing Hinglish mode mein Hindi-script planet names hain; upgrade prompt unhe consistent Roman Hinglish mein convert karne ko kahega.

# Antigravity mein Kundali Saral kaise kholein

**Aapka project bana hua hai.** Is ZIP mein website, backend calculation, English/Hinglish/Hindi content, design, 9 alag readings, testing code aur Antigravity ko dene wala detailed prompt hai.

1. `kundali-saral.zip` **download** karke **Extract All / Unzip** karein.
2. Google Antigravity app kholein, **New Project → Add Folder** mein `kundali-saral` folder select karein.
3. Project ke andar `ANTIGRAVITY_PROMPT.md` kholein, poora prompt copy karke Antigravity agent mein paste karein. Agent ko boliye: **"Existing project ko check karke improvements karo, existing calculations aur 3 languages mat hatana."**
4. Local preview ke liye Python 3.11+ install hona chahiye. Antigravity terminal mein ye run karein:

   ```bash
   python -m pip install -r requirements.txt
   uvicorn main:app --reload
   ```

5. Browser mein `http://127.0.0.1:8000` kholein. **Try a sample chart** button se app test karein.
6. Project ko **public website** banane ke liye hosting/domain set karna hoga. Antigravity mein folder kholne se website automatic internet par live **nahi** hoti.

## Kya-kya bana hai?

- English, Hinglish aur Hindi mode
- Hinglish/Hindi mein grah ke naam Hindi mein: सूर्य, चंद्र, मंगल, बुध, गुरु, शुक्र, शनि, राहु, केतु
- Birthday date, time, city ke hisaab se actual planetary placements
- Lagna, rashi, nakshatra, 12 houses, 9 grahas
- Career, love, marriage, money, education, family, health/routine, personality, self-growth sections
- Dasha list, print/PDF, JSON export, sample report

## Important

Ye **MVP** hai: shuruat ka working app. Professional public launch se pehle Swiss Ephemeris ki **AGPL/commercial license** conditions check karni hain. Astrology readings traditional reflections hain, guaranteed predictions nahi. Mobile, translations aur chart ko aur audit/improve kar sakte hain.
