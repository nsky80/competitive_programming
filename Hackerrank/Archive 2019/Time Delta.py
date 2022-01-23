# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000

import math
import os
import random
import re
import sys
import datetime


# Complete the time_delta function below.
# def time_delta(t1, t2):
#     # Sun   10   May  2015 13: 54:36 - 0700
#     a = t1.split(' ')
#     b = t2.split(' ')
#     a.pop(0), b.pop(0)
#     mn = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5,
#           'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
#     a[1] = mn[a[1]]
#     b[1] = mn[b[1]]
#     time1 = list(map(int, (a.pop(3)).split(':')))
#     time2 = list(map(int, (b.pop(3)).split(':')))
#     tz1, tz2 = int(a.pop()), int(b.pop())
#     tz = (0-tz1) + (0-tz2)
#     a.reverse(), b.reverse()
#     a, b = list(map(int, a)), list(map(int, b))
#     t1 = datetime.datetime(*a, *time1)
#     t2 = datetime.datetime(*b, *time2)
#     diff = (t1-t2).total_seconds()
#     h, m = abs(tz)//100, abs(tz) % 100
#     h = h * 60 * 60
#     m = m * 60
#     if tz <= 0:
#         return str(abs(int(diff)-(h + m)))
#     else:
#         return str(abs(int(diff) +(h + m)))

# def time_delta(t1, t2):
#     # Sun   10   May  2015 13: 54:36 - 0700
#     a = t1.split(' ')
#     b = t2.split(' ')
#     a.pop(0), b.pop(0)
#     mn = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5,
#           'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
#     a[1] = mn[a[1]]
#     b[1] = mn[b[1]]
#     time1 = list(map(int, (a.pop(3)).split(':')))
#     time2 = list(map(int, (b.pop(3)).split(':')))
#     tz1, tz2 = int(a.pop()), int(b.pop())
#     tz = (tz1) - (tz2)
#     a.reverse(), b.reverse()
#     a, b = list(map(int, a)), list(map(int, b))
#     t1 = datetime.datetime(*a, *time1)
#     t2 = datetime.datetime(*b, *time2)
#     diff = (t1-t2).total_seconds()
#     h, m = abs(tz)//100, abs(tz) % 100
#     h = h * 60 * 60
#     m = m * 60
#     # print(tz)
#     if tz >= 0:
#         return str(abs(int(diff)-(h + m)))
#     else:
#         return str(abs(int(diff) +(h + m)))

# import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    frmt = '%a %d %b %Y %H:%M:%S %z'
    # d = 'Sun 10 May 2015 13:54:36 -0000'
    t1 = datetime.datetime.strptime(t1, frmt)
    t2 = datetime.datetime.strptime(t2, frmt)
    a = abs(t1-t2)
    a = int(a.total_seconds())
    return str(a)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print(delta)

# 25200
# 88200
#
# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000
