"""
https://www.codechef.com/COOK108B/problems/PLAYSTR
Example Input
2
5
11000
01001
3
110
001
Example Output
YES
NO
"""

# s = list(s)
# t = list(t)
# i = 0
# j = n - 1
# while s != t and i < (n + 1)//2 <= j:
#     if s[i] != t[i] and s[j] != t[j] and s[i] != s[j]:
#         s[i] = t[i]
#         s[j] = t[j]
#         i += 1
#         j -= 1
#     elif s[i] != t[i] and s[j] == t[j]:
#         j -= 1
#     elif s[i] == t[i] and s[j] != t[j]:
#         i += 1

from collections import Counter


def is_equalize(n, s, t):
    sc = Counter(s)
    tc = Counter(t)

    if sc != tc:
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':
    for _ in range(int(input())):
        turn = int(input().strip())
        s = input().strip()
        t = input().strip()
        print(is_equalize(turn, s, t))
