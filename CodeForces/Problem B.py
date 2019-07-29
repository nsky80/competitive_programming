from functools import reduce

n = int(input())
maximum = 0
for i in range(n+1):
    temp = list(map(int, list(str(i))))
    temp = reduce(lambda x, y: x*y, temp)
    if temp>maximum:
        maximum = temp
print(maximum)