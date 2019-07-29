"""
PROXYC
Input
The first line of the input contains a single integer T denoting the number of test cases.
The description of T test cases follows.
The first line of each test case contains a single integer D.
The second line contains a single string S with length D.
Output
For each test case, print a single line containing one integer — the minimum number of times Chef needs
to be marked as present by proxy, or −1 if it is impossible to make Chef achieve 75% attendance.


Example Input
1
9
PAAPPAPPP
Example Output
1
"""
import math


def count_proxy(d, s):
    p = 0  # present day of chef
    for att in s:
        if att == 'P':
            p += 1
    current = p/d
    if current >= 0.75:
        return -1
    else:
        required = 0.75 - current
        c = 1 / d
        return math.ceil((c * 100) * required)



if __name__ == "__main__":
    for _ in range(int(input())):
        d = int(input())
        s = input().rstrip()
        print(count_proxy(d, s))
