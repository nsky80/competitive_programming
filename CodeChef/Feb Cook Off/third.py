def check_detail(n, ke, lr):
    h_max = max([i[1] for i in lr])
    res = []
    for i in range(n):
        c = [0 for m in range(h_max)]
        temp = lr.copy()
        temp.pop(i)
        for j in temp:
            for k in range(j[0]-1, j[1]):
                c[k] += 1
        ld = c.count(ke)
        res.append(ld)
    return max(res)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().rstrip().split())
        lr = []
        for _ in range(n):
            lr.append(list(map(int, input().rstrip().split())))
        print(check_detail(n, k, lr))