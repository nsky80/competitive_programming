"""
https://codeforces.com/contest/1204/problem/B

inputCopy
4 2 2
outputCopy
5 7
inputCopy
5 1 5
outputCopy
5 31
"""


def min_max(n, l, r):
    """
    Valid but long solution execution time O(1)
    s = 0
    lt = l
    s += (n - (lt - 1))
    s_m = (n - (r - 1)) * (2 ** (r - 1))
    lt -= 1
    r -= 1
    s += (2 * (2 ** lt - 1))
    s_m += (1 * (2 ** r - 1))
    return s, s_m"""
    return n - l + 2 ** l - 1, (n - r) * 2 ** (r - 1) + 2 ** r - 1


if __name__ == '__main__':
    print(*min_max(*map(int, input().strip().split())))
