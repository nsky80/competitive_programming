#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the separateNumbers function below.
def separateNumbers(s):
    flag = False
    n = chance= len(s) - 1
    start = 1
    end = 2
    attempt = 1
    first = int(s[0:1])
    while n and chance:
        prev = int(s[start:end])
        if prev - first == 1:
            first = prev
            start = end
            end = end + attempt
            n -= attempt
            flag = True
        else:
            end += attempt
            attempt += 1
            flag = False

    if flag and n == 0:
        print("YES", s[0:1])
    else:
        print("NO")


if __name__ == '__main__':
        separateNumbers('99100')
