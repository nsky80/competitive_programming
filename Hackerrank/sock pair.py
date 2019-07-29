from itertools import groupby
n = int(input())
c = map(int, input().split())

ans = 0
print([len(list(group)) for key, group in groupby(sorted(c))])
for val in [len(list(group)) for key, group in groupby(sorted(c))]:
    ans = ans + val//2
print(ans)