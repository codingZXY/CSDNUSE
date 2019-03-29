# -*- coding: utf-8 -*-
# @Time : 2019-03-29 16:57
# @Author : cxa
# @File : request.py
# @Software: PyCharm
import requests
r = requests.get('https://www.baidu.com')
print(r.status_code)
