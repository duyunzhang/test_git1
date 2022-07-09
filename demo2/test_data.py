'''
@file :  select.py
@author : 张福卫
@date : 2022/6/27 22:11
'''
from locall import *
from xingming.test_xm import *

import random

def id_select(user_id):
    '''查询'''

    # 链接数据库 [Scrm]
    conn = localhost
    # 创建游标
    cursor = conn.cursor()
    # sql语句
    cursor.execute('select * from a where id like "%{}"'
                    .format(user_id))  # 用户id查询

    # 提交
    conn.commit()
    # 打印结果
    results = cursor.fetchall()
    print("表头:\n", "  ".join([item[0] for item in cursor.description]))

    for row in results:
        print(row)
        # print(row[1])

    # print("当前上报数据表中共有数据☞【",len(results),"】条")  #打印列表数量

def all_select(sql):
    '''查询'''

    # 链接数据库 [Scrm]
    conn = localhost
    # 创建游标
    cursor = conn.cursor()
    # sql语句
    cursor.execute(sql)  # 用户id查询

    # 提交
    conn.commit()
    # 打印结果
    res = cursor.fetchall()
    print('查询返回数据共' + '【' + str(len(res)) + '】' + '条')
    print("表头:\n", "  ".join([item[0] for item in cursor.description]))


    for row in res:
        print(row)
        # print(row[1])

    # print("当前上报数据表中共有数据☞【",len(results),"】条")  #打印列表数量

def inser_sql(sql):
    '''查询'''

    # 链接数据库 [Scrm]
    conn = localhost
    # 创建游标
    cursor = conn.cursor()
    # sql语句
    cursor.execute(sql)  # 用户id查询

    # 提交
    conn.commit()
    print('插入语句:\n   '+sql)

    s2='select * from a  order by id desc limit 3'
    cursor.execute(s2)

    #打印返回结果
    res=cursor.fetchall()
    print('查询返回数据共'+'【'+str(len(res))+'】'+'条')
    print("表头:\n", "  ".join([item[0] for item in cursor.description]))
    for i in res:
        print('数据展示:\n' + str(i))
    # 打印结果
    results = cursor.fetchall()
    print("表头:\n", "  ".join([item[0] for item in cursor.description]))

    for row in results:
        print(row)
        # print(row[1])

    # print("当前上报数据表中共有数据☞【",len(results),"】条")  #打印列表数量

def test_updata():
    '''批量操作数据库 '''

    conn = localhost
    # 创建游标
    cursor = conn.cursor()
    for i in range(1,1000):
        m=random.randrange(18,22)
        # tom = XM1()
        # print(tom)
        # s1 = f"UPDATE `test_1`.`a` SET `name` = '{tom}', `age` = 18 WHERE `id` = {i} " #修改姓名
        s1 = f"UPDATE `test_1`.`a` SET `age` = '{str(m)}' WHERE `id` = {i} "  #修改年龄
        # s1 = f"UPDATE finance_order SET order_status = 3  where username = '赵峰' and product_id = 2022032410164444233"
        # s1 = "UPDATE finance_order SET buy_time = '%s' where username = '杨晓宇' and product_id = 2022032410164444233"%(today)
        print(s1)
        cursor.execute(s1)#提交
        conn.commit()  # 执行sql

        s2 = 'select * from a  order by id desc limit 3'
        cursor.execute(s2)

    #打印返回结果
    res=cursor.fetchall()
    print('查询返回数据共'+'【'+str(len(res))+'】'+'条')
    print("表头:\n", "  ".join([item[0] for item in cursor.description]))
    for i in res:
        print('数据展示:\n' + str(i))

if __name__ == '__main__':
    # id_select(10)
    test_updata()