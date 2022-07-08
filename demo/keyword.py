'''
@file :  keyword.py
@author : 张福卫
@date : 2022/07/08 15:39
'''


import json
import  jsonpath
def get_key(res,key):
    '''断言_获取字段值'''
    if res != '':
        try:
            res = res.json()  # 将返回值转会成json格式
            value = jsonpath.jsonpath(res, '$..{0}'.format(key))  # '$..{0}'从返回值的根目录开始遍历  key:要遍历的字段
            if len(value) == 1:
                print(value)
                return value
            elif len(value) > 1:
                for i in value:
                    print(i)
                    return i
        except Exception as e:
            return e
    else:
        return f'没有当前{key}字段值'


def get_key1(res,key):
    '''参数化_获取字段的值'''
    if res != '':
        try:
            res = res.json()  # 将返回值转会成json格式
            value = jsonpath.jsonpath(res, '$..{0}'.format(key))  # '$..{0}'从返回值的根目录开始遍历  key:要遍历的字段
            if len(value) == 1:
                print(value)
                return value
            elif len(value) > 1:
                for i in value:
                    print(i)
                    return i
        except Exception as e:
            return e
    else:
        return f'没有当前{key}字段值'



        # if value :
        #     if len(value) == 1:
        #         return value[0]
        #     else:
        #         return value
        # else:
        #     return value
