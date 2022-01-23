#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
# Complete the nonDivisibleSubset function below.

"""15 7
278 576 496 727 410 124 338 149 209 702 282 718 771 575 436
Your Output (stdout)
15
Expected OutputDownload
11"""


def nonDivisibleSubset(k, S):
    """ with K of 5, remainder pairs are 1+4 & 2+3. Given the numbers with a remainder of 1,
    they can't be paired with ANY of the numbers with remainder 4 (and vice versa).
    Using Complement, 0 always be in the result"""
    data = {i: [] for i in range(k)}
    res = []
    key = []
    for i in S:
        data[i % k].append(i)

    count = 0

    if len(data[0]) > 0:
        count = 1
        res.extend(data[0])
        key.append(0)
    # Creating a set for all sum of 7
    S = set([(x, k - x) for x in range(1, k // 2 + 1)])
    for i, j in S:
        if i != j:
            if len(data[i]) > len(data[j]):
                count += len(data[i])
                res.extend(data[i])
                key.append(i)
            else:
                count += len(data[j])
                res.extend(data[j])
                key.append(j)
        else:
            if len(data[i]) > 0:
                count += 1
                res.extend(data[i])
                key.append(j)
    print("Data: ", data)
    print("S:  ", S)
    print("res: ", res)
    print("key: ", key)
    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    S = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, S)

    print(str(result) + '\n')

    # fptr.close()
