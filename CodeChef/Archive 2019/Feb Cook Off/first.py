# cook your dish here
def check_tab(nb, whp):
    res = [ ]
    print(nb, whp)
    for i in range(len(nb)):
        area = []
        tabs = whp[i:i+nb[i][0]]
        for j in tabs:
            # print("j[2], i, nb[i][1]", j[2], i, nb[i][1], nb[i])
            if j[2] <= nb[i][1]:
                area.append(j[0] * j[1])
        if area:
            res.append(str(max(area)))
        else:
            res.append("no tablet")
        whp = whp[nb[i][0]-1:]
    return res


if __name__ == "__main__":
    t = int(input())
    nb = [ ]
    whp = [ ]
    for _ in range(t):
        nb.append(list(map(int, input().rstrip().split())))
        for _ in range(nb[ -1 ][ 0 ]):
            whp.append(list(map(int, input().rstrip().split())))
    res = check_tab(nb, whp)
    print("\n".join(res))