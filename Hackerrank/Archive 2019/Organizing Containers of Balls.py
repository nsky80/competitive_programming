#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the organizingContainers function below.
"""Sample Input 1

2
3
1 3 1
2 1 2
3 3 3
3
0 2 1
1 1 1
2 0 0
Sample Output 1

Impossible
Possible"""


def sum_of_dim(containter, n, m):
    cols = []
    rows = []
    for i in range(m):
        temp = 0
        for j in range(n):
            temp += container[j][i]
        cols.append(temp)
        rows.append(sum(container[i]))
    return rows, cols


def organizingContainers(container):
    m = len(container)
    n = len(container[0])
    sum_of_rows, sum_of_cols = sum_of_dim(container, n, m)
    if sum_of_cols == sum_of_rows:
        return "Possible"
    else:
        return "Impossible"
    # print(sum_of_rows)
    # print(sum_of_cols)
    # a = Counter(sum_of_rows)
    # set_of_rows = list(a.keys())
    # n = len(set_of_rows)

    # if n == 1:
    #     return "Possible"
    # max_c = (0, 0)
    # min_c = (0, 9999999)
    # for i in a.items():
    #     if i[1] > max_c[1]:
    #         max_c = i
    #     if i[1] < min_c[1]:
    #         min_c = i
    # if max_c[0] > min_c[0] and max_c[1] >= min_c[1]:
    #     return "Possible"
    # else:
    return "Impossible"



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)
        # result = sum_of_columns(container, 3, 3)
        print(result)
