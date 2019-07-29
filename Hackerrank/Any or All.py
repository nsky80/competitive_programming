"""any()
This expression returns True if any element of the iterable is true.
If the iterable is empty, it will return False.

Code

>>> any([1>0,1==0,1<0])
True
>>> any([1<0,2<1,3<2])
False
>>>
# all()
# This expression returns True if all of the elements of the iterable are true. If the iterable is empty,
# it will return True.
#
# Code

>>> all(['a'<'b','b'<'c'])
True
>>> all(['a'<'b','c'<'b'])
False
>>>
"""
print("hello world!")
n = int(input())
li = list(map(int, input().rstrip().split()))
if all([0 if i<0 else i for i in li]):
    if any([1 if str(i) == "".join(reversed(str(i))) else 0 for i in li]):
        print(True)
    else:
        print(False)
else:
    print(False)

# 5
# 12 9 61 5 14
