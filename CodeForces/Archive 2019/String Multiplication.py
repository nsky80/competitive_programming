"""input
3
a
b
a
output
3
input
2
bnn
a
output
1
Note
In the first example, the product of strings is equal to "abaaaba".

In the second example, the product of strings is equal to "abanana"."""


def multiplication(s, t):
    t = list(map(lambda x: s+x, t))
    return t


if __name__ == "__main__":
    n = int(input())
    s = list(input())
    s.append('')
    t = []
    for _ in range(n-1):
        t.append(input())
    f = multiplication(s, t)
    print(f)
    # print(t)