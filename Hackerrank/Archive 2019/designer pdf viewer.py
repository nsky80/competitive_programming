#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    wlist = list(set(list(word)))
    height = []
    for i in wlist:
        height.append(h[(abs(97-ord(i)))])
    return max(height)*len(word)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(str(result) + '\n')

    # fptr.close()
