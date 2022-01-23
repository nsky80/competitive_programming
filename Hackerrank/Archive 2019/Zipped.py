# zip([iterable, ...])
#
# This function returns a list of tuples. The th tuple contains the th element
# from each of the argument sequences or iterables.
#
# If the argument sequences are of unequal lengths, then the returned list is truncated to the length of
# the shortest argument sequence.
#
# >>> print(zip([1, 2, 3, 4, 5, 6], 'Hacker'))
# <zip object at 0x000001AA44B6C1C8>
# >>> a = zip([1, 2, 3, 4, 5, 6], 'Hacker')
# >>> for i in a:
# 	print(i)
#
# (1, 'H')
# (2, 'a')
# (3, 'c')
# (4, 'k')
# (5, 'e')
# (6, 'r')
# >>>
# >>> b =  zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1])
# >>> for i in b:
# 	print(i)
#
# (1, 0)
# (2, 9)
# (3, 8)
# (4, 7)
# (5, 6)
# (6, 5)
# >>> print(list(b))
# []
# >>> b
# <zip object at 0x000001AA44B2AD88>
# >>> for i in b:
# 	print(b)
#
# >>> b =  zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1])
# >>> print(list(b))
# [(1, 0), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5)]
# >>> b
# <zip object at 0x000001AA44B7C388>
# >>> a = [1, 2, 4,4]
# >>> a
# [1, 2, 4, 4]
# >>> a.insert(2, 12)
# >>> a
# [1, 2, 12, 4, 4]
# >>> a.insert(213,21)
# >>> a
# [1, 2, 12, 4, 4, 21]
# >>> a = [1, 2, 3]
# >>> b = [6, 5, 3]
# >>> c = [7, 8, 9]
# >>> x  = [a] + [b] +[c]
# >>> x
# [[1, 2, 3], [6, 5, 3], [7, 8, 9]]
# >>> print(*x)
# [1, 2, 3] [6, 5, 3] [7, 8, 9]
# >>> print(zip(*x))
# <zip object at 0x000001AA44B6A948>
# >>> a = zip(*x)
# >>> print(a)
# <zip object at 0x000001AA44B67C08>
# >>> for i in a:
# 	print(i)
#
# (1, 6, 7)
# (2, 5, 8)
# (3, 3, 9)


# marks =
# [[89, 90, 78, 93, 80], [90.0, 91.0, 85.0, 88.0, 86.0], [91.0, 92.0, 83.0, 89.0, 90.5]]
#
# for i in zip(*marks):
# 	print(i)
#
# (89, 90.0, 91.0)
# (90, 91.0, 92.0)
# (78, 85.0, 83.0)
# (93, 88.0, 89.0)
# (80, 86.0, 90.5)

# Enter your code here. Read input from STDIN. Print output to STDOUT
def result(n, x, marks):
    res = []
    for i in zip(*marks):
        res.append(sum(i)/x)
    return list(map(str, res))


if __name__ == "__main__":
    n, x = map(int, input().rstrip().split())
    marks = []
    for _ in range(x):
        marks.append(list(map(float, input().rstrip().split())))
    print("\n".join(result(n, x, marks)))

