"""
inputCopy
4
ab
acxb
cax
a
aaaa
aaabbcc
a
aaaa
aabbcc
ab
baaa
aaaaa
outputCopy
YES
YES
NO
NO
"""

from collections import Counter
import array


def check_val(s, t, p):
    if s == t:
        return "YES"
    chars = [0] * 27
    for i in p:
        chars[ord(i) - 96] += 1
    temp = len(t)
    i, j = 0, 0

    while temp >= 0:
        f = s[:i]
        g = t[:i]
        if f == g:
            pass
        else:
            c = g[-1]
            if chars[ord(c) - 96] > 0:
                chars[ord(c) - 96] -= 1
                s = s[:i-1] + c + s[i-1:]
            else:
                break
        i += 1
        temp -= 1
    # print("final", s)
    if s == t:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    for _ in range(int(input())):
        s = input().strip()
        t = input().strip()
        p = input().strip()
        print(check_val(s, t, p))
