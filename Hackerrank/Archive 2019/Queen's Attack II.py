# Optimization needed..................................................
# Sample Input 1
# 5 3
# 4 3
# 5 5
# 4 2
# 2 3
# Sample Output 1
# 10

# sample for 8x8 No obstacles
# 8 0
# 4 4

# sample for 8x8 with obstacles
# 8 1
# 4 4
# 3 5

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    up = [[i, c_q] for i in range(r_q+1, n+1)]  # (+1(max), c_q)
    down = [[i, c_q] for i in range(r_q-1, 0, -1)]   # (-1(min), c_q)
    left = [[r_q, i] for i in range(c_q-1, 0, -1)]    # (r_q, -1(min))
    right = [[r_q, i] for i in range(c_q+1, n+1)]     # (r_q, +1(max))
    up_right = [[i, j] for i, j in zip(range(r_q+1, n+1), range(c_q+1, n+1))]   # (+1(max), +1(max))
    down_left = [[i, j] for i, j in zip(range(r_q-1, 0, -1), range(c_q-1, 0, -1))]    # (-1(min), -1(min))
    up_left = [[i, j] for i, j in zip(range(r_q+1, n+1), range(c_q-1, 0, -1))]    # (+1(max), -1(min))
    down_right = [[i, j] for i, j in zip(range(r_q-1, 0, -1), range(c_q+1, n+1))]   # (-1(min), +1(max))
    # res = 0
    for obst in obstacles:
        if obst in up:
            up = up[:up.index(obst)]
        elif obst in down:
            down = down[:down.index(obst)]
        elif obst in left:
            left = left[:left.index(obst)]
        elif obst in right:
            right = right[:right.index(obst)]
        elif obst in up_right:
            up_right = up_right[:up_right.index(obst)]
        elif obst in down_left:
            down_left = down_left[:down_left.index(obst)]
        elif obst in up_left:
            up_left = up_left[:up_left.index(obst)]
        elif obst in down_right:
            down_right = down_right[:down_right.index(obst)]
    res = len(up + down + left + right + up_right + down_left + up_left + down_right)
    return res

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(str(result) + '\n')
    #
    # fptr.close()
