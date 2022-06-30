'''
@file :  test_run.py
@author : 张福卫
@date : 2022/6/27 23:45
'''

sql='select * from a  order by id desc'
from test_data import *
if __name__ == '__main__':
    # id_select(11)  #根据id查询
    all_select(sql)  #查询所有信息
    # inser_sql("INSERT INTO `test_1`.`a` ( `name`, `age`) VALUES ( '张三', 18)")  #添加数据