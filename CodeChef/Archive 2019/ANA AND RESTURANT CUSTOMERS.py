"""
Input:
The first line will contain T, number of test cases. Then the test cases follow.
The First line of each test case contains an integer N denoting no of customers.
 -Then N lines follow containing 2 spaced integers C and D, denoting the entry time and exit time of each customer.

Sample Input:
1
4
1 10
5 15
20 20000000000
4 8
Sample Output:
3
"""


def check_time(slot):
    cnt = 1
    for i in range(len(slot)-1):
        f = slot[i]
        s = slot[i+1]
        if s[0] <= f[1]:
            cnt += 1
    return cnt


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        slot = []
        for _ in range(n):
            slot.append(list(map(int, input().rstrip().split())))
        print(check_time(slot))