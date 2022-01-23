#!/bin/python3

import math
import os
import random
import re
import sys


def quadrants(p, queries):
    for q in queries:
        q = q.split(" ")
        q[1] = int(q[1])
        q[2] = int(q[2])

        if q[0] == 'X':
            for i in range(q[1]-1, q[2]):
                p[i][1] = -1 * (p[i][1])
        elif q[0] == 'Y':
            for i in range(q[1]-1, q[2]):
                p[i][0] = -1 * (p[i][0])
        # Case 3: c
        else:
            first = 0
            second = 0
            third = 0
            forth = 0
            for i in range(q[1]-1, q[2]):
                x = p[i][0]
                y = p[i][1]
                if x>0 and y>0:
                    first += 1
                elif x < 0 < y:
                    second += 1
                elif x<0 and y<0:
                    third += 1
                elif y < 0 < x:
                    forth += 1
            print(first, second, third, forth)


if __name__ == '__main__':
    n = int(input().strip())

    p = []

    for _ in range(n):
        p.append(list(map(int, input().rstrip().split())))

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries_item = input()
        queries.append(queries_item)

    quadrants(p, queries)
