# # import datetime as dt
# #
# #
# # print(dt.date.today())
# # print(dt.datetime.now().time())
#
#
# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
# from collections import OrderedDict
#
#
# def find_logo(arr):
#     ord_dict = OrderedDict()
#     for i in arr:
#         ord_dict[i] = ord_dict.get(i, 0) + 1
#     value = list(ord_dict.values())
#     value.sort(reverse = True)
#     value = value[0 : 3]
#     cnt = 0
#     res = []
#     for i, j in zip(ord_dict.keys(), ord_dict.values()):
#         if j in value:
#             res.append([i, j])
#             cnt += 1
#         if cnt == 3:
#             break
#     res.sort(key=lambda x: x[1], reverse = True)
#     return res
#
#
# if __name__ == '__main__':
#     s = sorted(input())
#     res = find_logo(s)
#     for i in res:
#         print(*i)
#
#

#
# class Node:
#     def __init__(self, cargo=None, next=None):
#         self.car = cargo
#         self.cdr = next
#
#     def __str__(self):
#         return str(self.car)
#
#
# def display(lst):
#     if lst:
#         print("%s " % lst)
#         display(lst.cdr)
#     else:
#         print("nil\n")
#
#
# head = Node()
# first = Node(23, head)
# second = Node(21, head)
# display(head)




# 1 2 3
# 4 5 6
# 7 8 9
#
# t = 3
# case = []
# for _ in range(2):
#     arr = []
#     for _ in range(t):
#         arr.extend(list(map(int, input().rstrip().split())))
#     case.append(arr)
# print(case)

# import datetime
#
# a = datetime.datetime(2015, 5, 2, 19, 54, 36)
# b = datetime.datetime(2015, 5, 1, 13, 54, 36)
# print(a)
# print(b)
# print("a-b: ", a-b)
# # c = datetime.datetime(2015, 5, 2, 19, 54, 36)
# # print(c)
# d = datetime.datetime(2015, 5, 10, 13, 54, 36)
# e = datetime.datetime(2015, 5, 10, 13, 54, 36)
# print("d: ", d)
# print("e: ", e)
# print("d-e: ", d-e)

import re


for i in range(100000, 100100):
    if re.match(r'\b\d{6}\b', str(i)):
        print(i, ": Match")
    else:
        print("Not Matched")