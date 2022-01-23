# 5
# 2
# 11
# 11
# 4
# 0101
# 0110
# 0110
# 0101
# 4
# 1001
# 0000
# 0000
# 1001
# 5
# 01110
# 01010
# 10001
# 01010
# 01110
# 5
# 00100
# 01010
# 10001
# 01010
# 01110


def check_solution(mat):
    resx = []
    for f in mat:
        n = len(f)
        flag1 = False
        flag2 = False
        for i in range(n//2):
            if f[i] == f[n-i-1]:
                flag1 = True
            else:
                flag1 = False
                break
        for j in f:
            n = len(j)
            if n%2 != 0:
                a = j[n//2+1:]
                b = list(reversed(a))
                b = "".join(b)
            else:
                a = j[n//2:]
                b = list(reversed(a))
                b = "".join(b)
            if j[:n//2] == b:

                flag2 = True
            else:
                flag2 = False
                break

        if flag1 and flag2:
            resx.append("YES")
        else:
            resx.append("NO")
    return resx


if __name__ == "__main__":
    t = int(input())
    mat = []
    for _ in range(t):
        n = int(input())
        n1 = []
        for _ in range(n):
            n1.append(input())
        mat.append(n1)
    res = check_solution(mat)
    print("\n".join(res))
