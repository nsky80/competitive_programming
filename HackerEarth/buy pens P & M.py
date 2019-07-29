#
#
# 2
# 4 2 2
# 1 2
# 3 4
# 3 2 2
# 1 2
# 1 2
# They can
# They can't


def check_possibility(n, P, M):
    p_id = [i for i in range(1, n+1)]
    # print(P in p_id,M in p_id, P, M, p_id)
    if set(P).union(set(M)) == set(p_id):
        return "They can"
    else:
        return "They can't"


if __name__ == "__main__":
    t = int(input())
    n = []
    p = []
    m = []
    P = []
    M = []
    for _ in range(t):
        npm = list(map(int, input().rstrip().split()))
        n.append(npm[0])
        p.append(npm[1])
        m.append(npm[2])
        P.append(list(map(int, input().rstrip().split())))
        M.append(list(map(int, input().rstrip().split())))
    for i in range(t):
        print("%s"%check_possibility(n[i], P[i], M[i]))