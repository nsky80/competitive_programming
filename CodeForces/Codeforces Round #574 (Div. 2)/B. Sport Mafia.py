"""
https://codeforces.com/contest/1195/problem/B
inputCopy
1 1
outputCopy
0
inputCopy
9 11
outputCopy
4
inputCopy
5 0
outputCopy
3
inputCopy
3 2
outputCopy
1
"""
import math


def root_(num):
    r1 = (-1 + (1 + 8 * num) ** 0.5)/2
    r2 = (-1 - (1 + 8 * num) ** 0.5)/2
    r1, r2 = math.ceil(r1), math.ceil(r2)
    # if not r1:
    #     return abs(r2)
    return max(r1, r2)
    # if n == 1:
    #     return 0
    #
    # # n -= 2
    # res = 2
    # temp = root_(k)
    # push_req = temp - 2 if temp - 2 > 0 else 3
    # res = (n - push_req)
    # return res

def candy_eaten(n, k):

    choco = 1
    last = 1
    eat = 0
    # for i in range(n - 1):
    i = n - 1
    while i > 0:
        if choco > k:
            temp = choco - k
            choco -= temp
            eat += temp
            i -= temp
        else:
            last += 1
            choco += last
            i -= 1
    return eat


if __name__ == '__main__':
    n, k = map(int, input().strip().split())
    print(candy_eaten(n, k))
