# from datetime import date
# import calendar
# my_date = input().split()
# my_date = "-".join(my_date)
# print(my_date)
# my_date = date(my_date)
# # my_date = date.today()
# print(my_date)
# print(calendar.day_name[date.weekday(my_date)])

import datetime
from Hackerrank import calendar1

day, month, year = map(int, input().split())
my_date = datetime.date(year, month, day)
# print(my_date)
print(calendar1.day_name[my_date.weekday() ])
# print(calendar.day_name)
# print(datetime.date.today())
# d = datetime.date(year, month, day)
# d = dplanted.strftime('%m/%d/%Y')
# d = datetime.date(d)+timedelta(days=30)
# print(d)
