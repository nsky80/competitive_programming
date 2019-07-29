"""
SAMPLE INPUT
3
5
23 22 919 1441 1
6
5 565 151 52 34543 595
3
79 88 12332
SAMPLE OUTPUT
2
5
0
"""


def check_num(arr):
    count = 0
    for i in arr:
        if i % 2 != 0:
            if str(i) == "".join(reversed(str(i))):
                print("i", i)
                count += 1
    return count

# Write your code here
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().rstrip().split()))
        print(check_num(arr))