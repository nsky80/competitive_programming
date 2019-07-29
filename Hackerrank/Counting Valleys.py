#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    bound = 0
    count = 0
    for i in s:
        if i == 'U':
            bound += 1
        else:
            bound -= 1
        if bound == 0:
            count += 1
    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(str(result) + '\n')

    # fptr.close()
