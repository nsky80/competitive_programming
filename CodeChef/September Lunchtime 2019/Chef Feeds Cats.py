def check_fair(n, m, a):
    arr = [0] * (n + 1)
    flag = True
    for i in range(0, m - n + 1, n):
        slic = a[i:i+n]
        arr = [0] * (n + 1)
        for j in slic:
            if arr[j]:
                flag = False
                break
            else:
                arr[j] = 1

    return "YES" if flag else "NO"


if __name__ == '__main__':
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        print(check_fair(n, m, a))
