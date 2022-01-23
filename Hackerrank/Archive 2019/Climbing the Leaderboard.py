#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the climbingLeaderboard function below.
# def climbingLeaderboard(scores, alice):
#     b = sorted(set(scores))
#     b.reverse()
#
#     l1 = []
#     for j in alice:
#         cnt = 0
#         flag = False
#         for i in b:
#             if i > j:
#                 cnt += 1
#                 flag = True
#             elif i == j:
#                 cnt += 1
#                 flag = False
#                 break
#             else:
#                 cnt += 1
#                 flag = False
#                 break
#         if flag:
#             l1.append(cnt+1)
#         else:
#             l1.append(cnt)
#     return l1
#!/bin/python3

import math
import os
import random
import re
import sys

# 7
# 100 100 50 40 40 20 10
# 4
# 5 25 50 120

# 6
# 4
# 2
# 1
# Complete the climbingLeaderboard function below.


def climbingLeaderboard(scores, alice):
    scrd = list(set(scores))
    scrd.sort(reverse = True)
    l1 = []     #contain answers or rank
    for alice_crr in alice:     # Executes first test case eg step by step each case get executed
        cnt = 0
        flag = False
        if alice_crr < scrd[-1]:
            cnt = len(scrd) + 1
        else:
            for i in scrd:
                if i > alice_crr:
                    cnt += 1
                    flag = True
                elif i == alice_crr:
                    cnt += 1
                    flag = False
                    break
                else:
                    cnt += 1
                    flag = False
                    break
        if flag:    # shows last rank so give it last
            l1.append(cnt+1)
        else:
            l1.append(cnt)
    return l1


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    print('\n'.join(map(str, result)))
    print()
    # fptr.write('\n')

    # fptr.close()
