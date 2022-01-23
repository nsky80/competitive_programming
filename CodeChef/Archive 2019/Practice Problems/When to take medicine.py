# URL: https://www.codechef.com/problems/MEDIC
"""
Sample Input:
1
2019:03:31
Sample Output:
1
"""
import math


def is_leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def find_days(data):    # yyyy, mm, dd
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # days in months with index
    # first check whether leap year or not
    months[2] = 29 if is_leap_year(data[0]) else 28
    count = 0
    while True:
        count += (months[data[1]] - data[2] + 2) // 2
        # print(months[data[1]] - data[2])
        # print(count, data[2])
        if (months[data[1]] - data[2]) % 2 == 0 or (months[data[1]] - data[2]) % 2 == 1:
            if data[1] == 12:
                data[0] += 1
                months[2] = 29 if is_leap_year(data[0]) else 28
                data[1] = 1
            else:
                data[1] += 1
            data[2] = 2 if not data[2] % 2 else 1
        else:
            break
    return count


if __name__ == '__main__':
    for _ in range(int(input())):
        dates = list(map(int, input().strip().split(":")))
        print(find_days(dates))
