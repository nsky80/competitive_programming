# Complete the kaprekarNumbers function below.
"""
Sample Input

1
100
Sample Output

1 9 45 55 99
"""


def kaprekarNumbers(p, q):
    res = []
    for num in range(p, q+1):
        d = len(str(num))
        sq = str(num * num)
        temp = len(sq)
        r = sq[-d:] if sq[-d:] else '0'
        l = sq[:temp-d] if sq[:temp-d] else '0'
        if int(r) + int(l) == num:
            res.append(str(num))
    print(" ".join(res))


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)