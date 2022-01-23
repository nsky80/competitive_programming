"""
>>> from functools import reduce
>>> reduce(lambda x, y: x+y, [1, 2, 3])
6
>>> a = [1, 2, 3]
>>> a
[1, 2, 3]
>>> reduce(lambda x, y: x+y, a, -6)
0
>>> reduce(lambda x, y: x+y, a, -5)
1
>>> a= [2, 4, 8]
>>> import math
>>> reduce(math.gcd, a)
2
>>> reduce(math.gcd, a, 3)
1
>>> reduce(math.gcd, a, 4)
2
>>> reduce(math.gcd, [4, 8, 12], 6)
2
>>> reduce(math.gcd, [4, 8, 12], 16)
4
>>> """

from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y: x*y, fracs)                    # complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)