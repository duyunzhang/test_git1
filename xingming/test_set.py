'''
@file :  test_set.py
@author : 张福卫
@date : 2022/07/06 18:42
'''

import random

from data_xm import *


def XM():
    xing = list_x
    ming = list_m
    for i in range(1):
        x = random.randint(0, len(xing))

        m1 = random.randint(0, len(ming))

        m2 = random.randint(0, len(ming))

        name = ('' + xing[x] + ming[m1] + ming[m2])
        # print(name)
        return name


if __name__ == '__main__':
    XM()