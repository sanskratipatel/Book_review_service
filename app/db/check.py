# check.py
import asyncio
import redis
# This is just for checking redis server
# is running or not this is not related to project 
async def check_redis():
    try:
        r = redis.from_url("redis://localhost", decode_responses=True)
        pong = await r.ping()
        print(" Redis running!" if pong else " No response from Redis")
        await r.aclose()  
    except Exception as e:
        print(f"Redis connection error: {e}")

asyncio.run(check_redis())
