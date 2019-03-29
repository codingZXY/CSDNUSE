import aiohttp
import asyncio
import sys

BASE_URL = "http://www.baidu.com"


async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL) as req:
            code = req.status
            if code in [200, 201]:
                text = await req.text()
                return text


async def start():
    text = await fetch()
    print(text)


if __name__ == '__main__':
    if sys.version_info >= (3, 7):
        asyncio.run(start())
    else:
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(start())
        finally:
            loop.close()
