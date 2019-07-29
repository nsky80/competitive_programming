#!/bin/python3

import math
import os
import random
import re
import sys

"""
Sample Input 0

5 2
0 4
Sample Output 0

2
"""


def binarySearch(arr, x, low, high):
    while low < high:
        mid = (high + low) // 2
        if arr[mid] == x:
            break
        elif arr[mid] > x:
            high = mid-1
        else:
            low = mid+1
    mid = (high + low) // 2
    if x <= arr[mid]:
        return mid
    else:
        return mid+1


# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    sp = [0 if i in c else None for i in range(n)]
    c.sort()
    h = len(c)
    for i in range(n):
        if sp[i] is None:
            if i < c[0] or i > c[-1]:
                if i < c[0]:
                    sp[i] = abs(c[0] - i)
                else:
                    sp[i] = abs(c[-1]-i)
            else:
                idx = binarySearch(c, i, 0, h)
                sp[i] = min(abs(c[idx]-i), abs(c[idx-1]-i))
    return max(sp)
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    print(str(result) + '\n')
