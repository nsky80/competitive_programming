"""
Example Input
2
3
4 5 6
1 2 3
5
4 8 6 4 1
2 5 7 4 7
Example Output
10
23

"""


def check_possible(val, c_li, t_li):   # current list and target list
    scor = 0
    if t_li:
        scor = ((val + t_li.pop()) // 2)
    else:
        c_li.append(val)
    return scor

def separate(n, a, b):
    ae = []
    ao = []
    be = []
    bo = []
    score = 0
    for i, j in zip(a, b):
        if i % 2 == 0:
            score += check_possible(i, ae, be)
        else:
            score += check_possible(i, ao, bo)
        if j % 2 == 0:
            score += check_possible(j, be, ae)
        else:
            score += check_possible(j, bo, ao)
    score += (((sum(ae) + sum(ao) + sum(be) + sum(bo)) - (len(ao) + len(bo))) // 2)
    return score


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        print(separate(n, a, b))