"""
Sample Input 0

hackerhappy
hackerrank
9
Sample Output 0

Yes
"""

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    match = 0
    while s[match] == t[match]:
        match += 1
    sn = len(s) - match
    tn = len(t) - match
    k = k - sn - tn
    if k >= 0:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    print(result + '\n')

