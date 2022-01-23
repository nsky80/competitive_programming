"""
Sample Input
2
7 2
2 4 5 6 15 17 20
2 19
6 2
6 2
5 9 9 16 16 19
4 5
6 19
Sample Output
7 3
2 -1
Each query contains 2 space separated integers, id and K in a single line
"""


def find_id(height, query):
    res = []
    for q in query:
        height[q[0]-1] = 0
        id_x = -1
        for i in height:
            if i > q[1]:
                id_x = height.index(i) + 1
                break
        res.append(str(id_x))
    return res


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().rstrip().split())
        height = list(map(int, input().rstrip().split()))
        query = []
        for _ in range(q):
            query.append(list(map(int, input().rstrip().split())))
        res = find_id(height, query)
        print(" ".join(res))
