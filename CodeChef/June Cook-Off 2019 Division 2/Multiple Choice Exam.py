"""
Example Input
3
6
ABCDAB
ABCDAB
8
DDCABCCA
DNCBBBBA
3
CDD
NDC
Example Output
6
3
1

"""
def find_marks(n, s, u):
    marks = 0
    i = 0
    while i < n:
        if s[i] == u[i]:
            marks += 1
            i += 1
        elif u[i] == 'N':
            i += 1
        else:
            i += 2
    return marks


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        s = list(input().rstrip())
        u = list(input().rstrip())
        print(find_marks(n, s, u))

