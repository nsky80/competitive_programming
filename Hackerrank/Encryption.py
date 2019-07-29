
#!/bin/python3

import math
import os
import random
import re
import sys
import textwrap


# Complete the encryption function below.
def encryption(s):
    s = "".join(s.split())
    print(s)
    L = len(s)
    sq = math.sqrt(L)
    row = math.floor(sq)
    col = math.ceil(sq)
    if row * col < L:
        row = round(sq)
    slices = textwrap.wrap(s, col)

    last = list(slices.pop())
    result = []
    for i in range(col):
        encrypted_text = [j[i] for j in slices]
        if last:
            encrypted_text.append(last[0])
            last.pop(0)
        result.append("".join(encrypted_text))
    return " ".join(result)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    print(result + '\n')

    # fptr.close()
