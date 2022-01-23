"""
Codeforces Round #580

inputCopy
1
20
2
10 20
outputCopy
20 20

inputCopy
3
3 2 2
5
1 5 7 7 9
outputCopy
3 1

inputCopy
4
1 3 5 7
4
7 5 3 1

outputCopy
1 1
"""

# Greedy approach
def find_pair(a, b):
    return max(a), max(b)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    m = int(input())
    b = list(map(int, input().strip().split()))
    print(*find_pair(a, b))