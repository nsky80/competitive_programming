"""
Example Input
3
2
2 8
3
8 2 8
3
9 10 11
Example Output
7
10
18

"""


# def sumOfDigits(a):
#     sm = 0
#     while (a != 0):
#         sm = sm + a % 10
#         a = a // 10
#
#     return sm
#
#
# def find_max(n, arr):
#     old = sumOfDigits(arr[0] * arr[1])
#     for i, num in enumerate(arr):
#         for j in arr[i+1:]:
#             old = max(sumOfDigits(num * j), old)
#     return old
#
#
# if __name__ == "__main__":
#     for _ in range(int(input())):
#         n = int(input())
#         a = list(map(int, input().strip().split()))
#         print(find_max(n, a))
def max_sum(n, arr):

    for i, num in enumerate(arr):
        if i < n - 2:
            cur = arr[i] * (i + 1)
            next = arr[i + 1] * (i + 2)
            n_next = arr[i + 2] * (i + 3)
            if cur * (i + 2) >= next * (i + 2):
                if next * (i + 3) >= n_next * (i + 3):


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    print(max_sum(n, a))