#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
"""
Sample Input

3
3
3 1 2
4
1 3 4 2
5
1 2 3 5 4
Sample Output

YES
YES
NO
1
5
1 6 5 2 4 3

A		rotate 
[1,6,5,2,4,3]	[6,5,2]
[1,5,2,6,4,3]	[5,2,6]
[1,2,6,5,4,3]	[5,4,3]
[1,2,6,3,5,4]	[6,3,5]
[1,2,3,5,6,4]	[5,6,4]
[1,2,3,4,5,6]
"""


def array_rotate(a, s, e, check):
    slic = deque(a[s:e])
    if check:
        slic.rotate(1)
    else:
        slic.rotate(-1)
    return a[:s] + list(slic) + a[e:]


def is_sorted(s):
    return sorted(s) == s


def larrysArray(arr):
    n = len(arr)
    # first calculate suffix which is sorted from starting position
    flag = False
    attempt = 1
    count = 8
    while count > 0:
        i = 0
        print(arr, end="\t")
        while i < n-1 and arr[i] <= arr[i+1]:
            i += 1
        print("i:", i, end=",  ")
        if i+3 <= n:
            if i + 4 <= n and sorted(arr[i+1:i+4], reverse=True) == arr[i+1:i+4]:
                st = i+1
                end = i + 4
                check = True
            else:   # left rotate
                st = i
                end = i + 3
                check = False
            arr = array_rotate(arr, st, end, check)
            print(st, end)
        else:
            # once try left
            temp = arr[n-i+1:n]
            temp1 = array_rotate(temp, 0, 3, False)
            if is_sorted(temp1) and arr[i-1] <= temp1[0]:
                flag = False
                break
            # once try right
            temp1 = array_rotate(temp, 0, 3, True)

            if is_sorted(temp1) and arr[n-i] <= temp1[0]:
                flag = False
                break
            flag = True
            print("In whole else")
            break
        count -= 1
    return "YES" if not flag else "NO"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        print(result, '\n')
    #
    # fptr.close()
