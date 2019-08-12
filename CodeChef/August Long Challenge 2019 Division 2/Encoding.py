"""
Encoding Problem Code: ENCODING

Example Input
3
1 9
2 97
1 8
2 12
1 1
1 8
Example Output
4681
49
36

"""


def f(num):
    num = str(num)
    current = num[0]
    res = num[0]
    for d in num[1:]:
        if d == current:
            res += '0'
        else:
            res += d
            current = d
    return int(res)


def find_num(l, nl, r, nr):
    password = 0
    for i in range(l, r+1):
        password += f(i)
    return password % (10 ** 9 + 7)


if __name__ == '__main__':
    # for _ in range(int(input())):
    #     nl, l = map(int, input().strip().split())
    #     nr, r = map(int, input().strip().split())
    #     print(find_num(l, nl, r, nr))
    print(f(1120))
