from math import gcd
"""2 1 2
1 3
SAMPLE OUTPUT 
2"""


def check_max(n, l, r, a):
    x = 1
    final_res = 0
    for i in range(l, r+1):
        temp = [i+j for j in a]
        res = temp[0]
        for j in range(n-1):
            res = gcd(res, temp[j+1])
        final_res = max(res, final_res)
    return final_res


if __name__ == "__main__":
    n, l, r = map(int, input().rstrip().split())
    a = list(map(int, input().rstrip().split()))
    print(check_max(n, l, r, a))