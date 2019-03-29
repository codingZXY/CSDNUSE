# -*- coding: utf-8 -*-
# # @Time : 2019-03-29 16:23
# # @Author : cxa
# # @File : async_demo.py
# # @Software: PyCharm
import asyncio


async def c_foo():
    await asyncio.sleep(2)
    print(f"2s之后,这是一个协程")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(c_foo())
    finally:
        loop.close()
