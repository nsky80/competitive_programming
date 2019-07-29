"""
Sample Input
2
4
aabc
zcaa
5
pqrrs
rsptr
Sample Output
3
4
"""
from collections import defaultdict


def check_possibility(n, t1, t2):
    res = 0
    for i in t1:
        if i in t2:
            res += 1
    return res


if __name__ == "__main__":
    for _ in range(int(input().rstrip())):
        n = int(input())
        t1 = input().rstrip()
        t2 = input().rstrip()
        print(check_possibility(n, t1, t2))