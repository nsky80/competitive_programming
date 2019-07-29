#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import date, timedelta


# Complete the dayOfProgrammer function below.
# def dayOfProgrammer(year):
#
#     d0 = date(year, 1, 1)
#     # d1 = date(year, 2, 4)
#     # delta = d1 - d0
#     # print(type(delta))
#     # print(delta.days+1)
#     timestamp = 255
#     if year < 1918:
#         timestamp = timestamp-32
#     a = str(d0 + timedelta(timestamp)).split("-")
#     a.reverse()
#     return ".".join(a)


def dayOfProgrammer(year):
    if year < 1918:
        if year % 4 == 0:
            date1 = 256-244
        else:
            date1 = 256 - 243
        a = str(date(year, 9, date1)).split("-")
    else:
        d0 = date(year, 1, 1)
        a = str(d0 + timedelta(255)).split("-") # 255 because started from jan 1
    a.reverse()
    return ".".join(a)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result)

    # fptr.close()
