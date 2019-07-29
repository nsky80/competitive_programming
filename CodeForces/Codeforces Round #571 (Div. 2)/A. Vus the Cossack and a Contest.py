"""
Input
The first line contains three integers n, m, and k (1≤n,m,k≤100) — the number of participants, the number of pens, and the number of notebooks respectively.

Output
Print "Yes" if it possible to reward all the participants. Otherwise, print "No".

You can print each letter in any case (upper or lower).

Examples
inputCopy
5 8 6
outputCopy
Yes
inputCopy
3 9 3
outputCopy
Yes
inputCopy
8 5 20
outputCopy
No

"""
if __name__ == '__main__':
    n, m, k = map(int, input().rstrip().split())
    if n <= m and n <= k:
        print("Yes")
    else:
        print("No")