#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the cutTheSticks function below.
def cutTheSticks(arr, n):
    res = []
    arr.sort()
    i = 0
    temp = n
    while n > 0:
        res.append(n)
        current = temp-i
        minimum = arr[i]
        while current > 0 and arr[i] == minimum:
            current -= 1
            n -= 1
            i += 1
        arr = [arr[j]-minimum if j >= i else 0 for j in range(0, temp)]
    return res



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 6

    arr = list(map(int, "5 4 4 2 2 8".rstrip().split()))

    result = cutTheSticks(arr, n)

    print('\n'.join(map(str, result)))

