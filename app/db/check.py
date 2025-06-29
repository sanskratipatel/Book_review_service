# check.py
import asyncio
import redis.asyncio as redis

async def check_redis():
    try:
        r = redis.from_url("redis://localhost", decode_responses=True)
        pong = await r.ping()
        print("✅ Redis running!" if pong else "❌ No response from Redis")
        await r.aclose()  # ✔ Use aclose instead of close
    except Exception as e:
        print(f"Redis connection error: {e}")

asyncio.run(check_redis())
