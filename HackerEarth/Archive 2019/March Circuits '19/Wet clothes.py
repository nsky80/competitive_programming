def check_clothes(t, a, g):
    res = 0
    while g:

        prev = t[0]
        t.pop(0)
        try:
            cr = t[0]
        except IndexError:
            break
        x = list(filter(lambda x: x <= cr-prev, a))
        for i in x:
            a.remove(i)
        res += len(x)
        g -= 1

    return res


if __name__ == "__main__":
    n, m, g = map(int, input().rstrip().split())
    t = list(map(int, input().rstrip().split()))
    a = list(map(int, input().rstrip().split()))
    print(check_clothes(t, a, g))


    """SAMPLE INPUT 
3 3 2
3 5 8
4 1 3
SAMPLE OUTPUT 
2"""