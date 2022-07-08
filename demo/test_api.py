'''
@file :  test_api.py
@author : 张福卫
@date : 2022/6/21 12:09
'''





import requests
import json
import jsonpath
from test_data import *
from keyword import *
import unittest
class test_ceshi(unittest.TestCase):
    def test_tt(self,**keyword):
        url = 'http://www.kuaidi100.com/query'
        params = {'type': 中通,
                  'postid': '75527538262087'

                  }
        res = requests.get(url=url, params=params)
        m = json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': '))
        value = requests.get_key(res.text,'com')
        print(value)
        self.assertEqual(first='zhongtong',second=value)
        print(m)
