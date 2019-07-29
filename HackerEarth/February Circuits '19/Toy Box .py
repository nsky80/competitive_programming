#
# 5 6
# 3 1
# 4 2
# 1 1
# 2 3
# 1 6


def check_price(M, pb):
    a = dict()
    for i in pb:
        p = i[0]
        b = i[1]
        if a.get(b, 0) == 0:
            a[b] = p
            pass
        elif a[b] <= p:
            a[b] = p
    return sum(a.values())


if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    pb = []
    for _ in range(N):
        pb.append(list(map(int, input().rstrip().split())))
    res = check_price(M, pb)
    print("%s"%str(res))