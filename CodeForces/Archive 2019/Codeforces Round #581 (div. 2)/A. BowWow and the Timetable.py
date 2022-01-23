"""
https://codeforces.com/contest/1204/problem/0
inputCopy
100000000
outputCopy
4
inputCopy
101
outputCopy
2
inputCopy
10100
outputCopy
3
"""


if __name__ == '__main__':
    num = int(input().strip(), 2)
    k = 0
    while num > 4 ** k:
        k += 1
    print(k)
