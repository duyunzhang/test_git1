'''
@file :  test_run.py
@author : 张福卫
@date : 2022/6/27 23:45
'''


sql='select distinct(name) from a  order by id desc'
sql5='select * from a group by age  having count(age)>1'
sql1='select * from a where name in (select name from a group by name having count(name)>1)' #查询姓名相同的所有记录
sql4='select * from a where age in (select age from a group by age having count(age)>1)'  #年龄重复的所有记录
sql3='select * from a where (name,age) in (select name,age from a group by name,age having count(name)>1)'
sql2='select * from a group by name having count(name)>1'
from test_data import *
if __name__ == '__main__':
    # id_select(11)  #根据id查询
    # all_select(sql5)  #查询所有信息
    # all_select(sql4)  #查询所有信息
    test_updata()
    # for i in range(1,1000):
    #     # tom = XM1()
    #     m = random.randrange(1,10)
    #     s1 = f"UPDATE `test_1`.`a` SET `calss` = '{m}' WHERE `id` = {i} "
    #     inser_sql(s1)  #添加数据