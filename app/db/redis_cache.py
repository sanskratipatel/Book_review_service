# app/db/redis_cache.py
import os
import redis.asyncio as redis
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost")

def get_redis():
    return redis.from_url(REDIS_URL, decode_responses=True)

# Cache key for books
BOOK_CACHE_KEY = "books"

async def get_cached_books():
    try:
        r = get_redis()
        return await r.get(BOOK_CACHE_KEY)
    except Exception as e:
        print(f"[Redis] Error on get: {e}")
        return None  # fallback

async def set_cached_books(data):
    try:
        r = get_redis()
        await r.set(BOOK_CACHE_KEY, data, ex=60)  # ex=expire time in sec
    except Exception as e:
        print(f"[Redis] Error on set: {e}")
