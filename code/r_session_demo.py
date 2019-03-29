# -*- coding: utf-8 -*-
# @Time : 2019-03-29 17:10
# @Author : cxa
# @File : r_session_demo.py
# @Software: PyCharm
from requests_html import HTMLSession
session = HTMLSession()
r = session.get("http://www.baidu.com")
print(r.status_code)
