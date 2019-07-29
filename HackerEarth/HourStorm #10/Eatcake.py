"""
SAMPLE INPUT
4 4
10 8 7 4
11 10 7 5
2 1 2
2 2 3
2 3 4
1 4
SAMPLE OUTPUT
-1
"""


def check_hunger(n, m, q, h, priority):
    if sum(q) > sum(h):
        for idx, person in enumerate(priority):
            for pr in person:
                if q[pr-1] > 0:
                    # print("h q", h[ idx ], q[pr-1])
                    temp = q[pr-1]
                    q[pr-1] = q[pr-1] - h[idx]
                    h[idx] = 0
                    break
        res = list(filter(lambda x: x > 0, q))
        return res[0] if res else -1
    else:
        return -1


if __name__ == "__main__":
    n, m = map(int, input().rstrip().split())
    q = list(map(int, input().rstrip().split()))
    h = list(map(int, input().rstrip().split()))
    priority = []
    for i in range(m):
        priority.append(list(map(int, input().rstrip().split())))
    print(check_hunger(n, m, q, h, priority))