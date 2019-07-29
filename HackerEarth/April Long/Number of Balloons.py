"""
SAMPLE INPUT
5 2 3
1 2 1 3 3
0 4
0 3
2 0
SAMPLE OUTPUT
2
1
0

"""

from collections import Counter


# Write your code here
def find_count_k(c, k):
    ans = list(Counter(c).values())
    return ans.count(k)


def find_range(ans, l, r, n):
    first = (l + ans) % n
    second = (r + ans) % n
    return min(first, second), max(first, second)


def input_query(n, k, q, c):
    ans = 0
    for i in range(q):
        l, r = map(int, input().rstrip().split())
        r1, r2 = find_range(ans, l, r, n)
        if r1 > r2:
            ans = find_count_k(c[r2:r1+1], k)
        else:
            ans = find_count_k(c[r1:r2+1], k)
        print(ans)


if __name__ == "__main__":
    n, k, q = map(int, input().rstrip().split())
    c = list(map(int, input().rstrip().split()))
    input_query(n, k, q, c)
