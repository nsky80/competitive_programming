#!/bin/python3

import math
import os
import random
import re
import sys

"""
1
10 10
7283455864
6731158619
8988242643
3830589324
2229505813
5633845374
6473530293
7053106601
0834282956
4607924137
3 4
9505
3845
3530
"""

# Complete the gridSearch function below.
def gridSearch(G, P, R, r):
    i = 0
    matched = False
    while R - 3 > 0 and matched != True:
        row = G[i]
        find_match = re.finditer(r'%s'%P[0], row)
        is_success = False
        for indices in find_match:
            st = indices.start()
            end = indices.end()
            j = r-1   # rows of pattern
            temp = 1
            while not is_success and j >0:
                if P[temp] == G[i+temp][st:end]:
                    is_success = False
                else:
                    is_success = True
                    break
                j -= 1
                temp += 1
            if not is_success and j == 0:
                matched = True
                break
            else:
                is_success = False
        i += 1
        R -= 1
    return "YES" if matched else "NO"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P, R, r)

        print(result + '\n')

    # fptr.close()
