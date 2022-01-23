#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations


# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    triplet = list(combinations(arr, 3))
    triplet = filter(lambda x: x[0] < x[1] < x[2], triplet)
    count = 0
    for triple in triplet:
        if triple[1] - triple[0] == triple[2] - triple[1] == d:
            count += 1
    return count


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    print(str(result) + '\n')

