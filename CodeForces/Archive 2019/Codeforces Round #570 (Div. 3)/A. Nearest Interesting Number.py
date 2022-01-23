"""
Input
The only line in the input contains an integer a (1≤a≤1000).

Output
Print the nearest greater or equal interesting number for the given number a. In other words,
print the interesting number n such that n≥a and n is minimal.

Examples
inputCopy
432
outputCopy
435
inputCopy
99
outputCopy
103
inputCopy
237
outputCopy
237
inputCopy
42
outputCopy
44

"""
def sum_(num):
    res = 0
    while num != 0:
        res += (num % 10)
        num //= 10
    return res


def find_sum(num):
    s = sum_(num)
    if s % 4 == 0:
        return num
    else:
        temp = num % 10
        if temp >= 7:
            num += (10 - temp)
            s = sum_(num)

        return num + ((s // 4) + 1) * 4 - s


def debug():
    for i in range(100000000000000000):
        k = find_sum(i)
        res = True if sum_(k) % 4 == 0 else False
        if not res:
            print((i, res, k), end='\t')


if __name__ == '__main__':
    # res = True if sum_() % 4 == 0 else False
    # for i in
    # print(find_sum(int(input())))
    debug()