#!/bin/python3
"""
Sample Input

11
middle-Outz
2
Sample Output

okffng-Qwvb
"""
import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k): #64, 96
    p = re.compile(r'[A-Za-z]')
    encryption = ''
    for idx, i in enumerate(s):
        if re.match(p,i):
            temp = ord(i)
            if temp < 97:
                temp = (temp + k) % 64
            else:
                temp = (temp + k) % 96
            encryption += chr(temp)
        else:
            encryption += i
    return encryption
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())


    result = caesarCipher(s, k)

    print(result + '\n')
