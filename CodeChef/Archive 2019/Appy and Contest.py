# T
# N, A, B and K
""" Appy should solve the problems whose problem codes are divisible by A but not divisible by B,
and Chef should solve the problems whose problem codes are divisible by B but not divisible by A
(they decided to not solve the problems whose codes are divisible by both A and B)"""


# def check_possibility(N, A, B, K):
#     cnt = 0
#     for i in range(1, N+1):
#         if i % A == 0 and i % B == 0:
#             pass
#         else:
#             cnt += 1
#     if cnt >= K:
#         return "Win"
#     else:
#         return "Lose"


# if __name__ == "__main__":
    # T = int(input())
    # for _ in range(T):
    #     N, A, B, K = map(int, input().split())
    #     res = check_possibility(N, A, B, K)
    #     print(res)


def check_possibility(data):
    res = []
    for j in data:
        N, A, B, K = j[0], j[1], j[2], j[3]
        cnt = 0
        for i in range(1, N+1):
            if i % A == 0 and i % B == 0:
                pass
            else:
                cnt += 1
        if cnt >= K:
            res.append("Win")
        else:
            res.append("Lose")
    return res


if __name__ == "__main__":
    T = int(input())
    data = []
    for t_itr in range(T):
        data.append([i for i in map(int, input().split())])
    res = check_possibility(data)
    for i in res:
        print(i)