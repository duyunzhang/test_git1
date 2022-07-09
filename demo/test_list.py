'''
@file :  test_list.py
@author : 张福卫
@date : 2022/6/21 21:38
'''

a = [1, 2]
b = [3, 4]
c = [5, 6]
d = [[1, 2], [3, 4], [5, 6]]

d.remove(c)
d.insert(1, 6)
print(d)

list = [1, 3, 5, 7]
print(list)
list.remove(1)
list.insert(2, 1)
print(list)

a = 1
print('000' + str(a))
print('0' * 3 + str(a))

b = 'hello_world_yoyo'
b = b.split('_')
print(b)

zifu = 'axbyczdj'
print(zifu[0::2])

list1 = [2, 6,6, 5, 6, 5, 1, -5,-5, -9, -1, -2, 1, 5, 8]
list_z = []
for i in list1:
    if i < 0:
        list_z.append(i)
        # print(list_z)
print('负数个数：' + str(len(list_z)))

print('正数个数：' + str(len(list1) - len(list_z)))

# !/usr/bin/env python3
# -*- coding: utf-8 -*-


# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def demo():
    # 方法一
    a = [11, 3, 3, -9, -4, 25, 27, 0, -1, -5, -5,8, -27, 10, 2, -2]

    b = [i for i in a if i > 0]
    print("大于0的个数: %s" % len(b))

    c = [i for i in a if i < 0]
    print("小于0的个数: %s" % len(c))

# 方法二
a = [11, 3, 3, -9, -4, 25, 27, 0, -1, -5, 8, -27, 10, 2, -2]

m = 0
n = 0
for i in a:
    if i > 0:
        m += 1
    elif i < 0:
        n += 1
    else:
        pass
print("大于0的个数: %s" % m)
print("小于0的个数: %s" % n)


b = 'hello_world_yoyo'
bb=[i for i in b ]
print(bb)