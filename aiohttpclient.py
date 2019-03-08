import aiohttp
import asyncio

j = {"a" : 1}


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main(number):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://localhost:8080/'+number)
        print(html)

loop = asyncio.get_event_loop()
number = input("number:")
loop.run_until_complete(main(number))