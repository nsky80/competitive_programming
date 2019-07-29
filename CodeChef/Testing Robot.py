"""2
6 10
RRLLLL
2 0
LL
"""


# cook your dish here
def count_points(x, cmd):
    res = []
    for command in cmd:
        if command == 'R':
            res.append(x + 1)
            x += 1
        else:
            res.append(x - 1)
            x -= 1
    return len(set(res))


if __name__ == "__main__":
    for _ in range(int(input())):
        n, x = map(int, input().rstrip().split())
        cmd = list(input().rstrip())
        print(count_points(x, cmd))