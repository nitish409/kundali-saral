from concurrent.futures import ThreadPoolExecutor
from fastapi.testclient import TestClient
from main import app
from astrology import calculate_chart

client = TestClient(app)
SAMPLE = {
    'name': 'Sample',
    'birth_date': '1998-08-15',
    'birth_time': '08:30',
    'city': 'New Delhi, India',
    'latitude': 28.6139,
    'longitude': 77.209,
    'time_zone': 'Asia/Kolkata',
    'language': 'en',
}


def test_health():
    res = client.get('/api/health').json()
    assert res['ok'] is True


def test_chart_all_languages():
    expected_sun = {'en': 'Sun', 'hinglish': 'Surya', 'hi': 'सूर्य'}
    for lang in ('en', 'hi', 'hinglish'):
        response = client.post('/api/chart', json={**SAMPLE, 'language': lang})
        assert response.status_code == 200, response.text
        data = response.json()
        chart = data['chart']
        read = data['reading']
        assert len(chart['planets']) == 9
        assert len(chart['houses']) == 12
        assert len(read['sections']) == 17
        assert len(read['house_guide']) == 12
        assert len(read['planet_guide']) == 9
        assert len(read['glossary']) >= 8
        assert len({p['key'] for p in chart['planets']}) == 9
        assert all(1 <= p['house'] <= 12 for p in chart['planets'])
        assert all(0 <= p['degrees'] < 30 for p in chart['planets'])
        ketu_lon = next(p['longitude'] for p in chart['planets'] if p['key'] == 'ketu')
        rahu_lon = next(p['longitude'] for p in chart['planets'] if p['key'] == 'rahu')
        assert abs(((ketu_lon - rahu_lon) % 360) - 180) < 1e-3

        sun_planet = next(p for p in chart['planets'] if p['key'] == 'sun')
        assert sun_planet['name'] == expected_sun[lang]
        assert expected_sun[lang] in str(read)

        # Verify every section has structured facts, rule_id, why_factors, strengths, challenges, reflection
        for sec in read['sections']:
            assert sec['rule_id'].startswith('KS-BPHS-D1-')
            assert len(sec['facts']) >= 3
            assert sec['why_factors']
            assert sec['possible_strengths']
            assert sec['possible_challenges']
            assert sec['reflection']


def test_hinglish_has_no_unexplained_devanagari():
    response = client.post('/api/chart', json={**SAMPLE, 'language': 'hinglish'})
    assert response.status_code == 200
    data = response.json()
    # Planet display names and reading prose in Hinglish must use Roman script by default
    for p in data['chart']['planets']:
        assert all(not ('\u0900' <= ch <= '\u097f') for ch in p['name'])
    assert all(not ('\u0900' <= ch <= '\u097f') for ch in data['reading']['summary'])
    for sec in data['reading']['sections']:
        for text in sec['facts'] + sec['interpretation'] + [sec['possible_strengths'], sec['possible_challenges'], sec['reflection']]:
            assert all(not ('\u0900' <= ch <= '\u097f') for ch in text), f'Unexpected Devanagari in Hinglish text: {text}'


def test_known_places():
    data = client.get('/api/cities').json()
    assert any(c['name'] == 'New Delhi' for c in data['cities'])
    assert len(data['cities']) >= 40


def test_invalid_timezone():
    response = client.post('/api/chart', json={**SAMPLE, 'time_zone': 'Fake/Nowhere'})
    assert response.status_code == 422


def test_nonexistent_dst_time():
    response = client.post('/api/chart', json={
        **SAMPLE, 'birth_date': '2024-03-10', 'birth_time': '02:30', 'time_zone': 'America/New_York'
    })
    assert response.status_code == 422


def test_ambiguous_dst_fallback_disambiguation():
    # 2024-11-03 01:30 in America/New_York occurred twice (EDT UTC-4 and EST UTC-5)
    ambiguous_payload = {
        **SAMPLE,
        'birth_date': '2024-11-03',
        'birth_time': '01:30',
        'latitude': 40.7128,
        'longitude': -74.0060,
        'time_zone': 'America/New_York',
    }
    res_missing = client.post('/api/chart', json=ambiguous_payload)
    assert res_missing.status_code == 422
    assert 'Ambiguous daylight-saving time' in res_missing.json()['detail']

    res_fold0 = client.post('/api/chart', json={**ambiguous_payload, 'dst_fold': 0})
    res_fold1 = client.post('/api/chart', json={**ambiguous_payload, 'dst_fold': 1})
    assert res_fold0.status_code == 200
    assert res_fold1.status_code == 200
    utc0 = res_fold0.json()['chart']['birth']['utc']
    utc1 = res_fold1.json()['chart']['birth']['utc']
    assert utc0 != utc1
    assert res_fold0.json()['chart']['birth']['dst_ambiguous'] is True


def test_time_uncertain_warning():
    res = client.post('/api/chart', json={**SAMPLE, 'time_uncertain': True, 'language': 'en'})
    assert res.status_code == 200
    data = res.json()
    assert data['chart']['birth']['time_uncertain'] is True
    assert 'uncertain' in data['reading']['uncertainty_banner'].lower()


def test_chart_determinism_and_concurrency():
    a = calculate_chart('2000-01-01', '12:30', 27.4924, 77.6737, 'Asia/Kolkata')
    b = calculate_chart('2000-01-01', '12:30', 27.4924, 77.6737, 'Asia/Kolkata')
    assert a['planets'] == b['planets']

    inputs = [
        ('1998-08-15', '08:30', 28.6139, 77.2090, 'Asia/Kolkata', 'en'),
        ('1990-05-21', '18:45', 19.0760, 72.8777, 'Asia/Kolkata', 'hi'),
        ('2001-12-09', '04:15', 12.9716, 77.5946, 'Asia/Kolkata', 'hinglish'),
        ('1985-01-30', '22:10', 51.5072, -0.1276, 'Europe/London', 'en'),
    ]
    expected = [calculate_chart(*args)['planets'] for args in inputs]
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(lambda args: calculate_chart(*args)['planets'], inputs * 3))
    for i, res_planets in enumerate(results):
        assert res_planets == expected[i % len(inputs)]
