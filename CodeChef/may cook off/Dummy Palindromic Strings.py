""""
Example Input
4
code
xyxyxy
sad
baab
Example Output
!DPS
DPS
DPS
!DPS
"""
from collections import Counter


def is_palindrome(s):
    return s == "".join(reversed(s))


def canFormPalindrome(st):
    if is_palindrome(st):
        return "!DPS"
    n = len(st)
    if n == 3:
        return "DPS"
    count = Counter(st)
    odd = 0
    for i in count.values():
        if i % 2 != 0:
            odd += 1

    if n % 2 == 0 and odd == 2:
        res = True
    elif n % 2 != 0 and odd == 3:
        res= True
    else:
        res = False
    return "DPS" if res else "!DPS"


if __name__ == "__main__":
    for _ in range(int(input())):
        print(canFormPalindrome(input()))
