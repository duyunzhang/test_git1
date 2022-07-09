'''
@file :  locall.py
@author : 张福卫
@date : 2022/6/30 10:22
'''

import pymysql

'''本地数据库'''

localhost = pymysql.Connect(host='192.168.28.122',
                            port=3306,  # 端口号
                            user='test',  # 用户名
                            passwd='123456',  # 密码
                            db='test_1',  # 链接数据的名称
                            charset='utf8')