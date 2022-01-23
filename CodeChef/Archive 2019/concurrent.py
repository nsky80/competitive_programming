# def largest_digit(num):
#     larges = num % 10
#     while num:
#         rem = num%10
#         if rem > larges:
#             larges = rem
#         num //= 10
#     return larges

#
# def largest_digit(num):
#     return max([int(i) for i in list(str(num))])
#
#
# def sum_of_digit(num):
#     return sum([int(i) for i in list(str(num))])
#
#
# print(largest_digit(12354))
# print(sum_of_digit(1235498))
print("Largest Digit is: ", max([int(i) for i in list(str(int(input("Enter Number:"))))]))
