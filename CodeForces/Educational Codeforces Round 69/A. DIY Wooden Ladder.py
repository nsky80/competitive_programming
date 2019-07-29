"""
https://codeforces.com/contest/1197/problem/A

4
4
1 3 1 3
3
3 3 2
5
2 3 3 4 2
3
1 1 2


2
1
2
0

        elif f1 > f2:
            f2 += a.popleft()
        elif f1 < f2:
            f1 += a.popleft()
        else:
            if len(a) > 2:
                f1 += a.popleft()
                f2 += a.popleft()
            else:
                break
"""

from collections import deque


def find_step(n, a):
    a.sort(reverse=True)
    a = deque(a)
    f1 = a.popleft() - 1  # because 1 step used in base
    f2 = a.popleft() - 1
    k = 0
    while f1 > 0 and f2 > 0  and a:
        if a.pop() >= 1:
            f1 -= 1
            f2 -= 1
            k += 1

    return k


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input().strip())
        a = list(map(int, input().strip().split()))
        print(find_step(n, a))