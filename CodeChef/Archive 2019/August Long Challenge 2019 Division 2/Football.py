"""
Problem Code: MSNSADM1

Example Input
2
3
40 30 50
2 4 20
1
0
10
Example Output
800
0
"""

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        points = 0
        for g, f in zip(a, b):
            score = g * 20 - f * 10
            points = max(points, score)
        print(points)
