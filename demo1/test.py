'''
@file :  test.py
@author : 张福卫
@date : 2022/6/21 15:59
'''

a = 'elsa_lucy_flora'
b = a.split('_')
print('讲字符串{}通过【b = a.split(“_”)】\n转换成列表>>>'.format(a)+str(b))

c = [2, 3, 4, 9, 6, 9, 4, 2, 6, 1]
print('列表>>>' + str(c))
c.sort()
print('升序>>>' + str(c))

c.sort(reverse=True)
print('降序>>>' + str(c))

c.reverse()
print('逆序>>>' + str(c))