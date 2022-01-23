"""SAMPLE INPUT
2
1 2 3
4 5 6
7 8 9
578 460 457
165 301 351
721 437 109
SAMPLE OUTPUT
15
1112
"""


def check_mat(mat):
    sum1 = mat[0][1] + mat[1][0] + mat[1][2] + mat[2][1]
    return sum1 - mat[1][1]


if __name__ == "__main__":
    for _ in range(int(input())):
        mat = []
        for _ in range(3):
            mat.append(list(map(int, input().rstrip().split())))
        print(check_mat(mat))