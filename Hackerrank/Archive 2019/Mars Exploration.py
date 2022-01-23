#!/bin/python3

import math
import os
import random
import re
import sys
"""
Sample Input 1

SOSSOT
Sample Output 1

1
Explanation 1

 = SOSSOT, and signal length . Sami sent  SOS messages (i.e.: ).

Expected Signal: SOSSOS     
Received Signal: SOSSOT
Difference:           X
We print the number of changed letters, which is .

Sample Input 2

SOSSOSSOS
Sample Output 2

0
"""
# Complete the marsExploration function below.
def marsExploration(s):
    message = s[0:3]
    count = 0
    for i in range(0, len(s)-2, 
):
        temp = s[i:i+3]
        if temp != message:
            for i in range(3):
                if temp[i] != message[i]:
                    count += 1
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    print(str(result) + '\n')


