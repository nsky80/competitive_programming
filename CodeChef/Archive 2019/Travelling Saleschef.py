"""Input
The first line of the input contains a single integer T denoting the number of test cases.
The description of T test cases follows.
The first line of each test case contains two space-separated integers N and D.
The second line contains N space-separated integers C1,C2,…,CN.
Output
For each test case, print a single line containing the string "YES" (without quotes) if Chef can visit all
cities or "NO" (without quotes) if he cannot.
"""

def check_temp(n, d, temp):

    for i in range(n):
        


if __name__ == "__main__":
    for _ in range(int(input())):
        n, d = map(int, input().split())
        temp = list(map(int, input().split()))
        print(check_temp(n, d, temp))