"""Kundali Saral API + static frontend. Start: uvicorn main:app --reload."""
from pathlib import Path
import json
import os
import logging
import time
from functools import lru_cache
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import URLError

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field, field_validator

from astrology import calculate_chart
from interpretations import reading
from cities import CITIES, serialize

app = FastAPI(
    title='Kundali Saral API',
    version='1.2.0',
    docs_url='/api/docs',
    openapi_url='/api/openapi.json',
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_methods=['GET', 'POST'],
    allow_headers=['Content-Type'],
)
logger = logging.getLogger(__name__)


class BirthInput(BaseModel):
    name: str = Field(default='', max_length=80)
    birth_date: str = Field(min_length=8, max_length=16)
    birth_time: str = Field(min_length=4, max_length=16)
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    time_zone: str = Field(min_length=1, max_length=80)
    language: str = 'en'
    city: str = Field(default='', max_length=160)
    dst_fold: int | None = Field(default=None)
    time_uncertain: bool = False

    @field_validator('language')
    @classmethod
    def check_lang(cls, value):
        if value not in ('en', 'hi', 'hinglish'):
            raise ValueError('Language must be en, hi or hinglish')
        return value

    @field_validator('dst_fold')
    @classmethod
    def check_fold(cls, value):
        if value is not None and value not in (0, 1):
            raise ValueError('dst_fold must be 0 (earlier/daylight) or 1 (later/standard)')
        return value


@app.get('/api/health')
def health():
    return {'ok': True, 'service': 'Kundali Saral', 'version': '1.2.0'}


@app.get('/api/cities')
def cities():
    return {'cities': [serialize(c) for c in CITIES]}


# Basic in-memory cache; public Nominatim requires a uniquely identifying User-Agent.
@lru_cache(maxsize=256)
def _fetch_geo(query):
    url = 'https://nominatim.openstreetmap.org/search?' + urlencode({
        'q': query, 'format': 'json', 'limit': 6, 'addressdetails': 1
    })
    user_agent = os.environ.get('NOMINATIM_USER_AGENT', '').strip()
    if not user_agent:
        return []
    req = Request(url, headers={'User-Agent': user_agent, 'Accept': 'application/json'})
    with urlopen(req, timeout=6) as response:
        return json.load(response)


_last_query = 0.0


@app.get('/api/search-cities')
def search_cities(q: str = Query(min_length=2, max_length=100)):
    global _last_query
    matches = [serialize(c) for c in CITIES if q.casefold() in f'{c[0]}, {c[1]}'.casefold()]
    if len(matches) >= 3 or len(q.strip()) < 3:
        return {'cities': matches[:8], 'source': 'offline'}
    # Do not rapidly hammer the shared geocoding service.
    if time.monotonic() - _last_query < 1.1:
        return {'cities': matches, 'source': 'offline', 'warning': 'Please pause between searches.'}
    _last_query = time.monotonic()
    if not os.environ.get('NOMINATIM_USER_AGENT'):
        return {
            'cities': matches,
            'source': 'offline',
            'warning': 'Online place search is not configured. Use one of the offline cities or enter latitude, longitude and IANA timezone manually.',
        }
    try:
        results = _fetch_geo(q.strip())
    except (URLError, TimeoutError, ValueError, OSError) as exc:
        logger.warning('Geocode unavailable: %s', type(exc).__name__)
        return {'cities': matches, 'source': 'offline', 'warning': 'Online place search unavailable. Enter coordinates and timezone manually.'}
    try:
        from timezonefinder import TimezoneFinder
        tf = TimezoneFinder(in_memory=True)
    except ImportError:
        tf = None
    for item in results:
        lat = float(item['lat'])
        lon = float(item['lon'])
        tz = tf.timezone_at(lat=lat, lng=lon) if tf else None
        matches.append({
            'name': item.get('name') or item['display_name'].split(',')[0],
            'country': item.get('address', {}).get('country', ''),
            'latitude': lat,
            'longitude': lon,
            'time_zone': tz,
            'display_name': item.get('display_name', ''),
        })
    return {'cities': matches[:8], 'source': 'OpenStreetMap/Nominatim'}


@app.post('/api/chart')
def chart(body: BirthInput):
    try:
        computed = calculate_chart(
            body.birth_date.strip(),
            body.birth_time.strip(),
            body.latitude,
            body.longitude,
            body.time_zone.strip(),
            body.language,
            dst_fold=body.dst_fold,
            time_uncertain=body.time_uncertain,
        )
    except (ValueError, OverflowError) as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:
        logger.exception('Chart computation failed')
        raise HTTPException(
            status_code=422,
            detail='Unable to calculate this chart. Check date, time, coordinates and timezone.',
        ) from exc
    return {
        'name': body.name.strip(),
        'city': body.city.strip(),
        'language': body.language,
        'chart': computed,
        'reading': reading(computed, body.language),
    }


app.mount('/', StaticFiles(directory=Path(__file__).resolve().parent / 'static', html=True), name='frontend')
