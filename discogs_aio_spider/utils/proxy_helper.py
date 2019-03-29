# -*- coding: utf-8 -*-
# @Time : 2018/12/28 11:03 AM
# @Author : cxa
# @File : proxy_helper.py
# @Software: PyCharm
import os
import aiohttp
import asyncio

environment = os.environ.get('APP_ENVIRONMENT', 'development')
if environment == "development":
    host = 'http://47.96.170.1:15003'
elif environment == "production":
    # host = 'http://10.10.4.3:15003'
    host = 'http://10.10.4.87:15003'
elif environment == "test":
    host = 'http://127.0.0.1:15003'
else:
    raise Exception("不正确的environment")
FAIL_SLEEP_TIME = 0
# host = 'http://47.96.170.1:15003'
# host = 'http://10.10.4.3:15003'
# host = 'http://127.0.0.1:15003'
token = '4cc5fbe69e2a93d48bef68319b763541'
TIMEOUT = 0.5


async def get_proxy(isown, protocol, site):
    async with aiohttp.connector.TCPConnector(limit=300, force_close=True, enable_cleanup_closed=True) as tc:
        async with aiohttp.ClientSession(connector=tc) as session:
            ps=await _get_proxy(session, isown, protocol, site)
            return ps


async def _get_proxy(session, isown, protocol, site, count=1, logger=None):
    try_times = 0
    while try_times < 2:
        try_times += 1
        try:
            url = '%s/select?isown=%s&protocol=%s&site=%s&token=%s&count=%s' % (
                host, isown, protocol, site, token, count)
            async with session.get(url, timeout=TIMEOUT) as res:
                r_json = await res.json()
                ps = r_json['data']
            return ps
        except Exception as e:
            if logger:
                logger.error(str(e))
            else:
                print(str(e))
    return []


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_proxy(isown=1, protocol=0, site='dianping'))
