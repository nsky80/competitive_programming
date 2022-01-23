"""
Example Input
2
3 6
5 7
1 9
2 5
3 7
5 8
2 5
5 10
Example Output
16
15

"""


def eat_twice(dv, n, m):
    # res = [[0, 0], [0, 0]]
    # i = 0
    # for d, v in dv:
    #     first = res[0]
    #     second = res[1]
    #
    #     if v > second[0] or v > second[1]:
    #         if d in first and v > second[first.index(d)]:
    #             second[first.index(d)] = v
    #         elif second[0] > second[1]:
    #             first[1] = d
    #             second[1] = v
    #         else:
    #             first[0] = d
    #             second[0] = v
    # return sum(res[1])
    dv.sort(key=lambda x: x[1], reverse=True)
    res = dv[0][1]
    i = dv[0][0]
    j = 1
    while dv[j][0] == i:
        j += 1
    res += dv[j][1]
    return res

if __name__ == '__main__':
    for _ in range(int(input())):
        n, m = map(int,input().rstrip().split())
        dv = []
        for _ in range(n):
            dv.append(list(map(int, input().rstrip().split())))
        print(eat_twice(dv, n, m))
