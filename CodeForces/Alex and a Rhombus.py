"""
Input
The first and only input line contains integer n (1≤n≤100) — order of a rhombus whose numbers of cells
should be computed.

Output
Print exactly one integer — the number of cells in a n-th order rhombus.

Examples
inputCopy
1
outputCopy
1
inputCopy
2
outputCopy
5
inputCopy
3
outputCopy
13

"""


def find_rhombus(n):
    if n >= 2:
        middle = 2 * n - 1
        terms = middle // 2
        ap_sum = int(((terms / 2) * ((middle - 2) + 1)) * 2)
        return middle + ap_sum
    else:
        return 1


if __name__ == '__main__':
    n = int(input())
    print(find_rhombus(n))
