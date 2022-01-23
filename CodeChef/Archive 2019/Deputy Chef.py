# cook your dish here
def check_best_shield(n, a, b):
    power = b[ 0 ] - (a[(n - 1) % n] + a[(n + 1) % n])
    ind = 0
    for i in range(1, n):
        defence_value = b[(n + i) % n] - (a[(n + i - 1) % n] + a[(n + i + 1) % n])
        if defence_value > power:
            power = defence_value
            ind = i
    if power > 0:
        return b[ind]
    else:
        return -1


def process_input():
    queries = ''
    while True:
        try:
            p = list(map(str, input().rstrip().split("\n")))
            if p == '':
                break
        except EOFError:
            return int(queries)
        queries = (p[0])


if __name__ == '__main__':

    t = process_input()
    n = []
    a = []
    b = []
    for _ in range(t):
        n.append(int(input().strip()))
        a.append(list(map(int, input().rstrip().split())))
        b.append(list(map(int, input().rstrip().split())))
    for i in range(t):
        print(check_best_shield(n[i], a[ i ], b[ i ]))