#!/bin/python3

import math
import os
import random
import re
import sys

# Complete t
# he cavityMap function below.

def cavityMap(grid):
    n = len(grid[0])
    for idx in range(1, len(grid)-1):
        # print(idx, square)
        i = 1
        square = grid[idx]
        while True:
            if i < n-1:
                if square[i-1] < square[i] > square[i+1]:
                    temp1 = grid[idx-1]
                    temp2 = grid[idx+1]
                    if temp1[i] < square[i] > temp2[i]:
                        square = square[:i] + 'X' + square[i+1:]
                        i += 1
                # print(idx, i, square[i])
            else:
                break
            i += 1
        grid[idx] = square
    return grid



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())

    grid = ['4241', '1112', '1912', '1892', '1234']

    # for _ in range(n):
    #     grid_item = input()
    #     grid.append(grid_item)

    result = cavityMap(grid)

    print('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()
