
def set_dfb(d, f, b, c):
    try:
        ind = c.index(d)
        print("try: ", ind, d, c)
    except ValueError:
        ind = c.index(max(c))
        print("except: ", ind, d, c)
    if c[ind] > 0:
        c[ind] -= 1
        return f, ind + 1
    else:
        c[ind] -= 1
        return b, ind + 1


if __name__ == '__main__':
    dfb = []
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        c = list(map(int, input().rstrip().split()))
        profit = 0
        res = []
        for _ in range(n):
            d, f, b = map(int, input().rstrip().split())
            p, i = set_dfb(d, f, b, c)
            profit += p
            res.append(i)
        print(profit, res, sep="\n")
