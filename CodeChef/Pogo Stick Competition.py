# cook your dish here
def count_points(k, a, n):
    res = []
    for i in range(n):
        points = a[i]
        position = i
        while True:
            position += k
            if position < n:
                points += a[position]
                pass
            else:
                res.append(points)
                break

    return max(res)


if __name__ == "__main__":
    for _ in range(int(input())):
        n, k = map(int, input().rstrip().split())
        a = list(map(int, input().rstrip().split()))
        print(count_points(k, a, n))


"""
2
5 2
3 6 4 7 2
5 3
3 -5 6 3 10

13 10
"""