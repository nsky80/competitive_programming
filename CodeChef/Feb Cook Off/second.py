def check_party(n, a):
    res = []
    for i in a:
        i.sort()
        cnt = 0
        for j in i:
            if j <= cnt:
                cnt += 1
        res.append(str(cnt))
    return res


if __name__ == "__main__":
    t = int(input())
    n = []
    a = []
    for _ in range(t):
        n.append(int(input()))
        a.append(list(map(int, input().rstrip().split())))
    res = check_party(n, a)
    print("\n".join(res))