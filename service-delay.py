import redis
import asyncio
import time

r = redis.Redis(
    host='127.0.0.1',
    port=6379,)


async def service(number):
    await asyncio.sleep(3)
    r.rpush("Gateway",number)
    print("pushed into gateway", number, time.time())



async def main():
    while True:
        if r.llen("ServiceQueue") > 0 :
            number = r.lpop("ServiceQueue")
            print("poped from serviceQ", number, time.time())
            await service(number)
        pass

loop = asyncio.get_event_loop()
loop.run_until_complete(main())