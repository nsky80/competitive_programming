import math
# a = 10
# b = 15
# print(math.gcd(10, 15))

# !/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#


def check_multiple(i, a, cond):
    flag = False
    for j in a:
        if cond == 1 and j % i == 0:
            flag = True
        elif cond == 0 and i%j == 0:
            flag = True
        else:
            flag = False
            break
    if flag:
        print("i from flag:", i)
    return flag


def getTotalX(a, b):
    #
    # Write your code here.
    #
    mi1 = max(a)
    mi2 = min(b)
    print("max a and min b", mi1, mi2)
    count = 0
    l1 = []
    for i in range(mi1, mi2+1):
        print("i is :", i)
        if check_multiple(i, a, 0):
            if check_multiple(i, b, 1):
                count += 1
    return count


# def getTotalY(a, b):    # Second approach from editor
#     factor = a[0]
#     for i in a:
#         factor = lcm(factor, i)
#     gcb = math.gcd()
#     for i in range(len(b)-1):
#         gcb = math.gcd(b[i])
#     print(gcb)
#     print(factor)


def lcm(a, b):
    return (a // math.gcd(a, b)) * b


if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    # total = getTotalX(a, b)
    # getTotalY(a, b)

    # print(str(total) + '\n')
