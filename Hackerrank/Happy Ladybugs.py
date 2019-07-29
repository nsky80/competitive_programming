import math
import os
import random
import re
import sys
from collections import Counter

"""
Sample Input 0

4
7
RBY_YBR
6
X_Y__X
2
__
6
B_RRBR
Sample Output 0

YES
NO
YES
YES

5
1
_
4
RBRB
4
RRRR
3
BBB
4
BBB_
Expected OutputDownload
YES
NO
YES
YES
YES
"""


# Complete the happyLadybugs function below.
def happyLadybugs(b):
    a = re.match('.*_+.*', b)
    if a:
        b = b.replace('_', '')
        cnt = Counter(list(b))
        temp = cnt.values()
        if 1 in temp:
            return "NO"
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        print(result + '\n')

    # fptr.close()
