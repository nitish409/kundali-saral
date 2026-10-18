"""Regression tests: localization must not silently change natal math."""
from astrology import calculate_chart


def _mathematical_snapshot(chart):
    return {
        'asc_sign': chart['lagna']['sign_index'],
        'asc_degree': chart['lagna']['degree'],
        'nakshatra_index': chart['nakshatra']['index'],
        'pada': chart['nakshatra']['pada'],
        'planets': [(p['key'], p['sign_index'], p['house'], p['longitude']) for p in chart['planets']],
        'houses': [(h['number'], h['sign_index'], h['lord_key'], h['lord_house']) for h in chart['houses']],
        'dashas': [(d['key'], d['start'], d['end']) for d in chart['dashas']],
    }


def test_locale_does_not_change_mathematics():
    args=('1998-08-15', '08:30', 28.6139, 77.2090, 'Asia/Kolkata')
    baseline=_mathematical_snapshot(calculate_chart(*args, lang='en'))
    for lang in ('hinglish', 'hi'):
        assert _mathematical_snapshot(calculate_chart(*args, lang=lang)) == baseline


def test_house_indices_follow_lagna():
    chart=calculate_chart('2000-01-01','12:30',27.4924,77.6737,'Asia/Kolkata')
    lagna=chart['lagna']['sign_index']
    assert {h['sign_index'] for h in chart['houses']} == set(range(12))
    for house in chart['houses']:
        assert house['sign_index'] == (lagna+house['number']-1) % 12
    for planet in chart['planets']:
        assert planet['house'] == (planet['sign_index']-lagna) % 12 + 1


def test_rahu_ketu_opposition():
    chart=calculate_chart('1998-08-15','08:30',28.6139,77.2090,'Asia/Kolkata')
    p={body['key']: body['longitude'] for body in chart['planets']}
    assert abs(((p['ketu'] - p['rahu']) % 360) - 180) < 0.000003


def test_all_12_lagna_rotations_across_day():
    seen_lagnas = set()
    for hour in range(24):
        for minute in (0, 30):
            t = f'{hour:02d}:{minute:02d}'
            c = calculate_chart('1998-08-15', t, 28.6139, 77.2090, 'Asia/Kolkata')
            asc = c['lagna']['sign_index']
            seen_lagnas.add(asc)
            assert c['lagna']['rashi_number'] == asc + 1
            for h in c['houses']:
                expected_sign = (asc + h['number'] - 1) % 12
                assert h['sign_index'] == expected_sign
                assert h['rashi_number'] == expected_sign + 1
    assert seen_lagnas == set(range(12))
