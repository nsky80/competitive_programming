# 8
# 1 2 3 1 2 3 3 3

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the equalizeArray function below.
def equalizeArray(arr):
    a = dict(Counter(arr))
    # print(a)
    b =max(a, key=a.get)    # return key with maximum value
    # print(b)
    c3 = arr.count(b)
    return len(arr)-c3

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    print(str(result) + '\n')

    # fptr.close()
