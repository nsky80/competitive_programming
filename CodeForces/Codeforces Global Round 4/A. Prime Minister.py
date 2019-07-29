""""
inputCopy
3
100 50 50
outputCopy
2
1 2
inputCopy
3
80 60 60
outputCopy
0
inputCopy
2
6 5
outputCopy
1
1
inputCopy
4
51 25 99 25
outputCopy
3
1 2 4
"""


def is_win(n, a):
    # total_seats = sum(a)
    to_win = sum(a) // 2 + 1
    eligible = a[0] // 2
    k = 1
    alice = a[0]
    i = 0
    ind = [str(1)]
    while alice < to_win and i < n:
        current = a[i]
        if current <= eligible:
            alice += current
            k += 1
            ind.append(str(i + 1))
        i += 1
    if alice >= to_win:
        print(k)
        print(" ".join(ind))
    else:
        print(0)



if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    is_win(n, a)
