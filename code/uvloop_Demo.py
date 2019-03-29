# -*- coding: utf-8 -*-
# @Time : 2019-03-29 16:38
# @Author : cxa
# @File : uvloop_Demo.py
# @Software: PyCharm
import asyncio
import aiohttp
import time
import async_timeout
try:
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass


async def fetch(url: str):
    with async_timeout.timeout(10):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as req:
                code = req.status
                print(code)


if __name__ == '__main__':
    url = "https://wwww.baidu.com"

    tasks = [asyncio.ensure_future(fetch(url)) for i in range(500)]
    start = time.time()
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))
    finally:
        loop.close()
    print("use time", time.time() - start)
