"""
Problem Code: ZOMCAV

Example Input
2
5
1 2 3 4 5
1 2 3 4 5
5
1 2 3 4 5
5 4 3 4 5
Example Output
NO
YES
"""


def is_all_killed(n, c, h):
    c = [0] + c
    h = [0] + h
    r = [0] * (n + 1)
    for i in range(1, n+1):
        lb = i - c[i] if i - c[i] > 0 else 1
        ub = i + c[i] if i + c[i] < n+1 else n
        # print(lb, ub)
        r[lb] += 1
        if ub < n:
            r[ub+1] -= 1
    for j in range(1, n+1):
        r[j] += r[j-1]
    r.sort()
    h.sort()
    # print(r, h)
    return "YES" if r == h else "NO"


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        c = list(map(int, input().strip().split()))
        h = list(map(int, input().strip().split()))
        print(is_all_killed(n, c, h))