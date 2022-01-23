"""6
7 1 3 4 1 7
Sample Output

3"""
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
from itertools import combinations


def check_diff(value):
    res = 999999
    cmb = combinations(value, 2)
    for i in cmb:
        if abs(i[0]-i[1]) < res:
            res = abs(i[0] - i[1])
    return res

# Complete the minimumDistances function below.
def minimumDistances(a):
    minimum = 999999
    temp = defaultdict(list)
    for idx, num in enumerate(a):
        temp[num].append(idx)
    for num in temp.values():
        if len(num) >= 2:
            res = check_diff(num)
            if res < minimum:
                minimum = res
    return minimum if minimum != 999999 else -1


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    print(str(result) + '\n')
