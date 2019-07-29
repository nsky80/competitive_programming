"""
SAMPLE INPUT
4 1
2 5 1 4
SAMPLE OUTPUT
2

"""


def check_min_cost(n, x, a):
    cost = 0
    idx = n
    for i in range(n):
        temp = a.index(max(a))
        if x < idx-temp-1:
            cost += x
            a.remove(min(a))
        else:
            a.pop(temp)
            cost += idx-temp-1
        idx -= 1
    return cost


if __name__ == "__main__":
    n, x = map(int, input().rstrip().split())
    a = list(map(int, input().rstrip().split()))
    print(check_min_cost(n, x, a))