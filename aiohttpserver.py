from aiohttp import web
import asyncio
import time
import redis


r = redis.Redis(
    host='127.0.0.1',
    port=6379,)


async def handle(request):
    number = request.match_info.get('name')
    print("handler run for number", number, time.time())
    r.rpush("ServiceQueue",number)
    answer =await ans(number)
    print("answer back to handler for number", number, time.time())
    return web.Response(text=str(answer))


async def ans(number):
    print("ans run for number", number, time.time())
    answer = ""
    while r.llen("Gateway") < 1:
        await asyncio.sleep(0)
    answer = int(r.lpop("Gateway"))
    print("ans find for number", number, time.time())
    return int(answer)*3


app = web.Application()
app.add_routes([web.get('/{name}', handle)])

web.run_app(app)