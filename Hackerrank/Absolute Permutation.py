#!/bin/python3
"""
Sample Input

3
2 1
3 0
3 2
Sample Output

2 1
1 2 3
-1
"""



import math
import os
import random
import re
import sys


# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    res = [0] * (n + 1)
    res[0] = k
    j = 0
    temp = n
    flag = False
    i = k + 1
    while n > 0:
        if abs(res[j] - j) == abs((j + 1) - i):
            res[j + 1] = i
            flag = True
        else:
            flag = False
            break
        j += 1
        i = ((i) % temp) + 1
        n -= 1
    return res[1:] if flag else [-1]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        print(' '.join(map(str, result)))
        # fptr.write('\n')

    # fptr.close()
