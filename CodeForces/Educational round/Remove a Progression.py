"""
inputCopy
3
3 1
4 2
69 6
outputCopy
2
4
12
"""


def find_element(n, x):
    li = list(range(n + 1))
    i = 1
    while len(li) > i:
        print(li)
        li.pop(i)
        i += 1
    print(li, i, len(li))
    return li[x]



if __name__ == '__main__':
    for _ in range(int(input())):
        n, x = map(int, input().split())
        print(find_element(n, x))