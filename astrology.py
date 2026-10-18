"""Deterministic Vedic birth-chart calculations. No AI-generated celestial positions."""
from datetime import datetime, timedelta, timezone
import threading
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
import swisseph as swe

CALCULATION_VERSION = '1.2.0'
_SWE_LOCK = threading.Lock()

EN_SIGNS = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
HI_SIGNS = ['मेष', 'वृषभ', 'मिथुन', 'कर्क', 'सिंह', 'कन्या', 'तुला', 'वृश्चिक', 'धनु', 'मकर', 'कुंभ', 'मीन']
HINGLISH_SIGNS = ['Mesh', 'Vrishabh', 'Mithun', 'Kark', 'Singh', 'Kanya', 'Tula', 'Vrishchik', 'Dhanu', 'Makar', 'Kumbh', 'Meen']

EN_PLANETS = {
    'sun': 'Sun', 'moon': 'Moon', 'mars': 'Mars', 'mercury': 'Mercury',
    'jupiter': 'Jupiter', 'venus': 'Venus', 'saturn': 'Saturn', 'rahu': 'Rahu', 'ketu': 'Ketu'
}
HINGLISH_PLANETS = {
    'sun': 'Surya', 'moon': 'Chandra', 'mars': 'Mangal', 'mercury': 'Budh',
    'jupiter': 'Guru', 'venus': 'Shukra', 'saturn': 'Shani', 'rahu': 'Rahu', 'ketu': 'Ketu'
}
HI_PLANETS = {
    'sun': 'सूर्य', 'moon': 'चंद्र', 'mars': 'मंगल', 'mercury': 'बुध',
    'jupiter': 'गुरु', 'venus': 'शुक्र', 'saturn': 'शनि', 'rahu': 'राहु', 'ketu': 'केतु'
}

SIGNS_RULERS = ['mars', 'venus', 'mercury', 'moon', 'sun', 'mercury', 'venus', 'mars', 'jupiter', 'saturn', 'saturn', 'jupiter']
BODY_IDS = {
    'sun': swe.SUN, 'moon': swe.MOON, 'mars': swe.MARS, 'mercury': swe.MERCURY,
    'jupiter': swe.JUPITER, 'venus': swe.VENUS, 'saturn': swe.SATURN, 'rahu': swe.MEAN_NODE
}

NAKSHATRAS = [
    'Ashwini', 'Bharani', 'Krittika', 'Rohini', 'Mrigashira', 'Ardra', 'Punarvasu', 'Pushya', 'Ashlesha',
    'Magha', 'Purva Phalguni', 'Uttara Phalguni', 'Hasta', 'Chitra', 'Swati', 'Vishakha', 'Anuradha', 'Jyeshtha',
    'Mula', 'Purva Ashadha', 'Uttara Ashadha', 'Shravana', 'Dhanishta', 'Shatabhisha', 'Purva Bhadrapada', 'Uttara Bhadrapada', 'Revati'
]
NAKSHATRAS_HINGLISH = [
    'Ashwini', 'Bharani', 'Krittika', 'Rohini', 'Mrigashira', 'Ardra', 'Punarvasu', 'Pushya', 'Ashlesha',
    'Magha', 'Purva Phalguni', 'Uttara Phalguni', 'Hasta', 'Chitra', 'Swati', 'Vishakha', 'Anuradha', 'Jyeshtha',
    'Mula', 'Purva Ashadha', 'Uttara Ashadha', 'Shravana', 'Dhanishta', 'Shatabhisha', 'Purva Bhadrapada', 'Uttara Bhadrapada', 'Revati'
]
NAKSHATRAS_HI = [
    'अश्विनी', 'भरणी', 'कृत्तिका', 'रोहिणी', 'मृगशिरा', 'आर्द्रा', 'पुनर्वसु', 'पुष्य', 'आश्लेषा',
    'मघा', 'पूर्वा फाल्गुनी', 'उत्तरा फाल्गुनी', 'हस्त', 'चित्रा', 'स्वाती', 'विशाखा', 'अनुराधा', 'ज्येष्ठा',
    'मूल', 'पूर्वाषाढ़ा', 'उत्तराषाढ़ा', 'श्रवण', 'धनिष्ठा', 'शतभिषा', 'पूर्वाभाद्रपद', 'उत्तराभाद्रपद', 'रेवती'
]

DASHA_ORDER = ['ketu', 'venus', 'sun', 'moon', 'mars', 'rahu', 'jupiter', 'saturn', 'mercury']
DASHA_YEARS = {'ketu': 7, 'venus': 20, 'sun': 6, 'moon': 10, 'mars': 7, 'rahu': 18, 'jupiter': 16, 'saturn': 19, 'mercury': 17}
YEAR_DAYS = 365.2425  # approximation; conventions differ by lineage

# Traditional Parashari sign dignities (BPHS standard sign-level mapping for the 7 classical grahas)
OWN_SIGNS = {
    'sun': (4,),
    'moon': (3,),
    'mars': (0, 7),
    'mercury': (2, 5),
    'jupiter': (8, 11),
    'venus': (1, 6),
    'saturn': (9, 10),
}
EXALTED_SIGN = {
    'sun': 0, 'moon': 1, 'mars': 9, 'mercury': 5, 'jupiter': 3, 'venus': 11, 'saturn': 6
}
DEBILITATED_SIGN = {
    'sun': 6, 'moon': 7, 'mars': 3, 'mercury': 11, 'jupiter': 9, 'venus': 5, 'saturn': 0
}
DIGNITY_LABELS = {
    'en': {
        'own_sign': 'Own sign (Swakshetra)',
        'exalted': 'Exalted sign (Uchcha)',
        'debilitated': 'Debilitated sign (Neecha)',
        'neutral': 'Standard sign placement',
        'lunar_node': 'Lunar node (Chhaya Graha)',
    },
    'hinglish': {
        'own_sign': 'Apni rashi (Swakshetra)',
        'exalted': 'Uchcha rashi (Exalted)',
        'debilitated': 'Neecha rashi (Debilitated)',
        'neutral': 'Normal rashi placement',
        'lunar_node': 'Lunar node (Chhaya Graha)',
    },
    'hi': {
        'own_sign': 'स्वराशि (स्वक्षेत्र)',
        'exalted': 'उच्च राशि',
        'debilitated': 'नीच राशि',
        'neutral': 'सामान्य राशि स्थिति',
        'lunar_node': 'छाया ग्रह (चंद्र पात)',
    },
}
PARASHARI_SPECIAL_ASPECT_OFFSETS = {
    'sun': (7,),
    'moon': (7,),
    'mars': (4, 7, 8),
    'mercury': (7,),
    'jupiter': (5, 7, 9),
    'venus': (7,),
    'saturn': (3, 7, 10),
}


def names_for(lang):
    if lang == 'hi':
        return HI_PLANETS, HI_SIGNS
    if lang == 'hinglish':
        return HINGLISH_PLANETS, HINGLISH_SIGNS
    return EN_PLANETS, EN_SIGNS


def nakshatras_for(lang):
    if lang == 'hi':
        return NAKSHATRAS_HI
    if lang == 'hinglish':
        return NAKSHATRAS_HINGLISH
    return NAKSHATRAS


def _format_dms(deg_in_sign):
    deg_int = int(deg_in_sign)
    minutes = int(round((deg_in_sign - deg_int) * 60))
    if minutes == 60:
        deg_int += 1
        minutes = 0
    return f'{deg_int:02d}°{minutes:02d}′'


def _dignity_for(planet_key, sign_idx, lang):
    loc = lang if lang in ('en', 'hinglish', 'hi') else 'en'
    if planet_key in ('rahu', 'ketu'):
        return 'lunar_node', DIGNITY_LABELS[loc]['lunar_node']
    if EXALTED_SIGN.get(planet_key) == sign_idx:
        return 'exalted', DIGNITY_LABELS[loc]['exalted']
    if DEBILITATED_SIGN.get(planet_key) == sign_idx:
        return 'debilitated', DIGNITY_LABELS[loc]['debilitated']
    if sign_idx in OWN_SIGNS.get(planet_key, ()):
        return 'own_sign', DIGNITY_LABELS[loc]['own_sign']
    return 'neutral', DIGNITY_LABELS[loc]['neutral']


def _valid_utc(date, time, tz, dst_fold=None):
    try:
        naive = datetime.fromisoformat(f'{date}T{time}')
    except ValueError as exc:
        raise ValueError('Enter a valid birth date (YYYY-MM-DD) and local birth time (HH:MM).') from exc
    if not 1900 <= naive.year <= 2100:
        raise ValueError('Birth year must be between 1900 and 2100.')
    try:
        z = ZoneInfo(tz)
    except (ZoneInfoNotFoundError, KeyError, ValueError) as exc:
        raise ValueError('Use a valid IANA time zone, e.g. Asia/Kolkata.') from exc

    aware_0 = naive.replace(tzinfo=z, fold=0)
    aware_1 = naive.replace(tzinfo=z, fold=1)
    roundtrip_0 = aware_0.astimezone(timezone.utc).astimezone(z).replace(tzinfo=None)
    roundtrip_1 = aware_1.astimezone(timezone.utc).astimezone(z).replace(tzinfo=None)

    # Reject nonexistent local wall-times (DST spring-forward clock jumps).
    if roundtrip_0 != naive and roundtrip_1 != naive:
        raise ValueError('This local time does not exist because of a daylight-saving clock change.')

    utc_0 = aware_0.astimezone(timezone.utc)
    utc_1 = aware_1.astimezone(timezone.utc)
    is_ambiguous = (utc_0 != utc_1) and (roundtrip_0 == naive) and (roundtrip_1 == naive)

    if is_ambiguous:
        if dst_fold not in (0, 1):
            off_0 = aware_0.strftime('%z')
            off_1 = aware_1.strftime('%z')
            raise ValueError(
                f'Ambiguous daylight-saving time: {time} occurred twice on {date} in {tz} '
                f'(first at UTC{off_0[:3]}:{off_0[3:]}, then at UTC{off_1[:3]}:{off_1[3:]}). '
                'Please choose whether birth occurred during the earlier (Daylight) or later (Standard) hour.'
            )
        chosen = utc_0 if dst_fold == 0 else utc_1
        return chosen, True, dst_fold

    return utc_0, False, 0


def _as_sign(longitude):
    return int(longitude // 30) % 12


def _nakshatra_details(longitude, nak_list, planet_names):
    span = 360.0 / 27.0
    nak_index = int(longitude / span) % 27
    nak_fraction = (longitude % span) / span
    pada = min(4, int(nak_fraction * 4) + 1)
    lord_key = DASHA_ORDER[nak_index % 9]
    return {
        'index': nak_index,
        'name': nak_list[nak_index],
        'pada': pada,
        'fraction': nak_fraction,
        'lord_key': lord_key,
        'lord': planet_names[lord_key],
    }


def calculate_chart(date, time, latitude, longitude, time_zone, lang='en', dst_fold=None, time_uncertain=False):
    if not (-90.0 <= float(latitude) <= 90.0 and -180.0 <= float(longitude) <= 180.0):
        raise ValueError('Latitude must be between -90 and 90 and longitude between -180 and 180.')
    birth_utc, dst_ambiguous, resolved_fold = _valid_utc(date, time, time_zone, dst_fold=dst_fold)
    hour = birth_utc.hour + birth_utc.minute / 60.0 + birth_utc.second / 3600.0

    with _SWE_LOCK:
        jd = swe.julday(birth_utc.year, birth_utc.month, birth_utc.day, hour)
        swe.set_sid_mode(swe.SIDM_LAHIRI)
        # Offline Moshier ephemeris avoids external ephemeris binary downloads.
        flags = swe.FLG_MOSEPH | swe.FLG_SIDEREAL | swe.FLG_SPEED
        positions = {}
        for key, body in BODY_IDS.items():
            vector, _ = swe.calc_ut(jd, body, flags)
            positions[key] = {'longitude': vector[0] % 360.0, 'speed': vector[3]}
        positions['ketu'] = {
            'longitude': (positions['rahu']['longitude'] + 180.0) % 360.0,
            'speed': positions['rahu']['speed'],
        }
        _, asc_mc = swe.houses_ex(jd, float(latitude), float(longitude), b'W', swe.FLG_SIDEREAL)

    asc_lon = asc_mc[0] % 360.0
    asc_sign = _as_sign(asc_lon)
    planet_names, sign_names = names_for(lang)
    nak_list = nakshatras_for(lang)

    planets = []
    for key, pos in positions.items():
        lon_val = pos['longitude']
        sign_idx = _as_sign(lon_val)
        house_num = (sign_idx - asc_sign) % 12 + 1
        deg_in_sign = lon_val % 30.0
        p_nak = _nakshatra_details(lon_val, nak_list, planet_names)
        dignity_key, dignity_label = _dignity_for(key, sign_idx, lang)
        aspect_offsets = PARASHARI_SPECIAL_ASPECT_OFFSETS.get(key, ())
        aspects_houses = [((house_num + off - 2) % 12) + 1 for off in aspect_offsets]
        planets.append({
            'key': key,
            'name': planet_names[key],
            'name_en': EN_PLANETS[key],
            'name_hinglish': HINGLISH_PLANETS[key],
            'name_hi': HI_PLANETS[key],
            'sign_index': sign_idx,
            'rashi_number': sign_idx + 1,
            'sign': sign_names[sign_idx],
            'house': house_num,
            'degrees': round(deg_in_sign, 2),
            'dms': _format_dms(deg_in_sign),
            'longitude': round(lon_val, 6),
            'speed': round(pos['speed'], 6),
            'retrograde': pos['speed'] < 0 if key not in ('sun', 'moon') else False,
            'is_node': key in ('rahu', 'ketu'),
            'nakshatra_index': p_nak['index'],
            'nakshatra': p_nak['name'],
            'pada': p_nak['pada'],
            'nakshatra_lord_key': p_nak['lord_key'],
            'nakshatra_lord': p_nak['lord'],
            'dignity_key': dignity_key,
            'dignity': dignity_label,
            'aspects_houses': aspects_houses,
        })

    houses = []
    for n in range(1, 13):
        sign_idx = (asc_sign + n - 1) % 12
        lord = SIGNS_RULERS[sign_idx]
        occupants = [p for p in planets if p['house'] == n]
        lord_planet = next(p for p in planets if p['key'] == lord)
        aspected_by = [
            {'key': p['key'], 'name': p['name'], 'from_house': p['house']}
            for p in planets
            if n in p['aspects_houses']
        ]
        houses.append({
            'number': n,
            'sign_index': sign_idx,
            'rashi_number': sign_idx + 1,
            'sign': sign_names[sign_idx],
            'lord_key': lord,
            'lord': planet_names[lord],
            'lord_house': lord_planet['house'],
            'lord_sign': lord_planet['sign'],
            'planets': [{'key': p['key'], 'name': p['name'], 'degrees': p['degrees'], 'dms': p['dms'], 'retrograde': p['retrograde']} for p in occupants],
            'aspected_by': aspected_by,
        })

    moon_longitude = positions['moon']['longitude']
    moon_nak = _nakshatra_details(moon_longitude, nak_list, planet_names)
    asc_nak = _nakshatra_details(asc_lon, nak_list, planet_names)
    asc_lord_key = SIGNS_RULERS[asc_sign]
    dashas = _calculate_dashas(birth_utc, moon_nak['index'], moon_nak['fraction'], planet_names)

    return {
        'system': {
            'calculation_version': CALCULATION_VERSION,
            'zodiac': 'Sidereal (Lahiri ayanamsa)',
            'houses': 'Whole sign',
            'node': 'Mean Rahu / opposite Ketu',
            'ephemeris': 'Swiss Ephemeris Moshier',
            'dasha': 'Approximate Vimshottari (365.2425-day year)',
            'aspects_convention': 'Parashari whole-sign Rashi/Graha Drishti (7 classical grahas)',
        },
        'birth': {
            'date': date,
            'time': time,
            'time_zone': time_zone,
            'latitude': latitude,
            'longitude': longitude,
            'utc': birth_utc.isoformat(),
            'dst_ambiguous': dst_ambiguous,
            'dst_fold': resolved_fold,
            'time_uncertain': bool(time_uncertain),
        },
        'lagna': {
            'sign_index': asc_sign,
            'rashi_number': asc_sign + 1,
            'sign': sign_names[asc_sign],
            'degree': round(asc_lon % 30.0, 2),
            'dms': _format_dms(asc_lon % 30.0),
            'longitude': round(asc_lon, 6),
            'lord_key': asc_lord_key,
            'lord': planet_names[asc_lord_key],
            'nakshatra_index': asc_nak['index'],
            'nakshatra': asc_nak['name'],
            'pada': asc_nak['pada'],
        },
        'moon_sign_index': _as_sign(moon_longitude),
        'moon_sign': sign_names[_as_sign(moon_longitude)],
        'sun_sign_index': _as_sign(positions['sun']['longitude']),
        'sun_sign': sign_names[_as_sign(positions['sun']['longitude'])],
        'nakshatra': {
            'name': moon_nak['name'],
            'pada': moon_nak['pada'],
            'index': moon_nak['index'],
            'lord_key': moon_nak['lord_key'],
            'lord': moon_nak['lord'],
        },
        'planets': planets,
        'houses': houses,
        'dashas': dashas,
    }


def _calculate_dashas(birth_utc, nak_idx, fraction, names):
    index = nak_idx % 9
    first = DASHA_ORDER[index]
    # At birth, the first Mahadasha has already partially elapsed.
    elapsed = DASHA_YEARS[first] * fraction * YEAR_DAYS
    start = birth_utc - timedelta(days=elapsed)
    now = datetime.now(timezone.utc)
    out = []
    for i in range(19):
        lord = DASHA_ORDER[(index + i) % 9]
        end = start + timedelta(days=DASHA_YEARS[lord] * YEAR_DAYS)
        if end >= birth_utc:
            out.append({
                'key': lord,
                'name': names[lord],
                'years': DASHA_YEARS[lord],
                'start': start.date().isoformat(),
                'end': end.date().isoformat(),
                'current': start <= now < end,
            })
        start = end
    return out
