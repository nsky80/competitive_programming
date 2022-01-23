"""
Input
The first line of the input contains one integer q (1≤q≤100) — the number of queries. Each query is presented by two lines.

The first line of the query contains two integers n and k (1≤n≤100,1≤k≤108) — the number of products and the value k. The second line of the query contains n integers a1,a2,…,an (1≤ai≤108), where ai is the price of the i-th product.

Output
Print q integers, where the i-th integer is the answer B on the i-th query.

If it is impossible to equalize prices of all given products with restriction that for all products the condition |ai−B|≤k should be satisfied (where ai is the old price of the product and B is the new equal price of all products), print -1. Otherwise print the maximum possible equal price of all products.

Example
inputCopy
4
5 1
1 1 2 3 1
4 2
6 4 8 5
2 2
1 6
3 5
5 2 5
outputCopy
2
6
-1
7

"""
def find_extremes(a):
    max_ = 0
    min_ = 10 ** 8 + 1
    for i in a:
        min_ = min(i, min_)
        max_ = max(i, max_)
    return min_, max_


def find_num(n, k, a):
    min_, max_ = find_extremes(a)
    d = min_ + k
    if abs(max_ - d) > k:
        return -1
    else:
        return d

if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = map(int, input().rstrip().split())
        a = list(map(int, input().rstrip().split()))
        print(find_num(n, k, a))