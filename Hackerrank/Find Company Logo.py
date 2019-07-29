#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def find_logo(string):
    a = Counter(string)
    li = [(i, j) for i, j in zip(a.keys(), a.values()) ]
    li.sort(key=lambda x: x[1], reverse=True)
    value = [i[1] for i in li][:3]
    i = 0
    res = [[], [], []]
    while True:
        # print('li[i]', li[i][1])
        try:
            if li[i][1] is value[0]:
                res[0].append(li[i][0])
            elif li[i][1] is value[1]:
                res[1].append(li[i][0])
            elif li[i][1] is value[2]:
                res[2].append(li[i][0])
            else:
                break
        except IndexError:
            break
        i += 1
    res = [sorted(i) for i in res]
    temp = []
    cnt = 0
    for i in range(len(res)):
        if cnt == 3:
            break
        for j in range(len(res[i])):
            temp.append((res[i][j], a[res[i][j]]))
    return temp


if __name__ == '__main__':
    s = input()
    res = find_logo(s)
    for i in res:
        print(*i)
