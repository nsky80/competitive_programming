#!/bin/python3

import math
import os
import random
import re
import sys


def second(grid):
    for i, s in enumerate(grid):
        temp = s.replace('O', '1')
        grid[ i ] = temp.replace('.', 'O')
    return grid


def flip_bit(grid):
    for i, s in enumerate(grid):
        grid[ i ] = s.replace('1', 'O')
    return grid


def blast(grid, r, c):
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '1':
                if i > 0:
                    upper = grid[i - 1]
                    upper = upper[:j] + '.' + upper[j + 1:]
                    grid[ i - 1 ] = upper
                if i < r - 1 and grid[ i + 1 ][ j ] != '1':
                    down = grid[ i + 1 ]
                    down = down[ :j ] + '.' + down[ j + 1: ]
                    grid[ i + 1 ] = down
                if j > 0 and grid[ i ][ j - 1 ] != '1':
                    left = grid[ i ]
                    left = left[:j - 1] + '.' + left[j: ]
                    grid[ i ] = left
                if j < c - 1 and grid[i][j + 1] != '1':
                    right = grid[i]
                    right = right[:j+1] + '.' + right[j + 2: ]
                    grid[ i ] = right
                main = grid[ i ]
                main = main[ :j ] + '.' + main[ j + 1: ]
                grid[i] = main
    return grid


# Complete the bomberMan function below.
def bomberMan(n, grid, r, c):
    need_to = False
    for i in range(n-1):
        temp = i % 2
        if temp == 0:
            grid = second(grid)
            need_to = True
        elif temp == 1:
            grid = blast(grid, r, c)
            need_to = False
    if need_to:
        grid = flip_bit(grid)
    return grid


if __name__ == '__main__':
    # fptr = open(os.environ[ 'OUTPUT_PATH' ], 'w')

    rcn = input().split()

    r = int(rcn[ 0 ])

    c = int(rcn[ 1 ])

    n = int(rcn[ 2 ])

    grid = [ ]

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid, r, c)

    print(result)

