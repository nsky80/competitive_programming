import math


def is_smart_number(num):
    val = int(math.sqrt(num))
    print('val is :', val)
    print("num/val", num/val)
    print("num%val", num%val)

    if num / val**2 == 1:
        return True
    return False


for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")
