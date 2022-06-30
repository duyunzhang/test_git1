'''
@file :  test_api.py
@author : 张福卫
@date : 2022/6/21 12:09
'''





import requests
import json
from test_data import *

url = 'http://www.kuaidi100.com/query'
params = {'type': 中通,
          'postid': '75527538262087'

          }
res = requests.get(url=url, params=params)
m = json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': '))
print(m)
