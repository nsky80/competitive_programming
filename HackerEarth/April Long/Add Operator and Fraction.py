"""
Input format

First line: Two integers n and k (1<n<=100000 ) where n is the number of steps.
It is guaranteed that there is at least k numbers written in nth step.

Output format

Print the answer in the format (int)/(int), like 3/5.

SAMPLE INPUT
5 5
SAMPLE OUTPUT
2/5
Explanation
0/1,1/2 first step

0/1,1/2 second step

0/1,1/3,1/2 third step

0/1,1/4,1/3,1/2 fourth step

0/1,1/5,1/4,1/3,2/5,1/2 fifth step and the fifth fraction is 2/5

"""


def find_fraction(n, k):
    a = (0, 1)
    b = (1, 2)
    frc = [(0, 1), (1, 2)]
    for i in range(1, n+1):
        flag = 0
        for j in range(len(frc) - 1):
            check = frc[flag][1] + frc[flag+1][1]
            if check <= i:
                frc.insert(flag+1, (frc[flag][0] + frc[flag+1][0], check))
                flag += 1
            flag += 1
        print(frc)
    return frc[k-1]


if __name__ == "__main__":
    n, k = map(int, input().rstrip().split())
    a = find_fraction(n, k)
    print("%d/%d" %(a[0], a[1]))
