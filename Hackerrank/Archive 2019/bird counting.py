# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
# from collections import Counter
#
# import operator
#
#
# # Complete the migratoryBirds function below.
# def migratoryBirds(arr):
#     b = dict(Counter(arr))
#     sorted_x = sorted(b.items(), key=operator.itemgetter(0))
#     data = max(b.values())
#     for i in sorted_x:
#         if i[1] == data:
#             data = i[0]
#             break
#     return data
#
#
# if __name__ == '__main__':
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     arr_count = int(input().strip())
#
#     arr = list(map(int, input().rstrip().split()))
#
#     result = migratoryBirds(arr)
#
#     print(str(result) + '\n')
#

from collections import Counter
n = input()
arr = Counter(map(int, input().split()))
print(arr.most_common(1)[0][0])
