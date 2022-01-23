"""
Input
The first line contains two integers n and q (2≤n≤105, 0≤q≤3⋅105) — the number of elements in the deque
and the number of queries. The second line contains n integers a1, a2, ..., an, where ai (0≤ai≤109) —
the deque element in i-th position. The next q lines contain one number each, meaning mj (1≤mj≤1018).

Output
For each teacher's query, output two numbers A and B — the numbers that Valeriy pulls out of the deque for
the mj-th operation.

inputCopy
5 3
1 2 3 4 5
1
2
10
outputCopy
1 2
2 3
5 2
inputCopy
2 0
0 0
outputCopy

"""

from collections import deque


def find_element(arr, rotate):
    a, b = arr[0], arr[1]
    for i in range(rotate):
        a = arr.popleft()
        b = arr.popleft()
        if a > b:
            arr.appendleft(a)
            arr.append(b)
        else:
            arr.appendleft(b)
            arr.append(a)
    return str(a), str(b)



if __name__ == '__main__':
    n, q = map(int, input().rstrip().split())
    a = deque(map(int, input().rstrip().split()))
    for _ in range(q):
        print(" ".join(find_element(a.copy(), int(input().rstrip()))))
