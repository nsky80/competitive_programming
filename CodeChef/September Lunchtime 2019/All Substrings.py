"""
https://www.codechef.com/LTIME76B/problems/ALLSUB/

Example Input
4
aa
ababab
aaa
ramialsadaka
said
sryhieni
code
codeisfun

Example Output
aaabbb
aaaaadiklmrs
Impossible
codefinsu
"""


from collections import Counter


def fun(x, y):
    x_c = Counter(x)
    y_c = Counter(y)
    flag = True
    for alp, cnt in x_c.items():
        cnt2 = y_c.get(alp)
        if cnt2:
            if cnt2 < cnt:
                flag = False
                break
            else:
                y_c[alp] -= (x_c[alp])
        else:
            flag = False
            break
    if flag:
        left = []
        right = []
        if x < x[0]*len(x):
            for i, j in y_c.items():
                if i < x[0]:
                    left.append(i*j)
                else:
                    right.append(i*j)
        else:
            for i, j in y_c.items():
                if i <= x[0]:
                    left.append(i*j)
                else:
                    right.append(i*j)
        left.sort()
        right.sort()
        return "".join(left) + x + "".join(right)
    else:
        return "Impossible"


if __name__ == '__main__':
    for _ in range(int(input())):
        a = input().strip()
        b = input().strip()
        print(fun(a, b))
