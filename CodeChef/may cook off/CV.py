# Example Input
# 3
# 6
# bazeci
# 3
# abu
# 1
# o
# Example Output
# 3
# 1
# 0
import re


def check_possibility(n, s):
    count = re.findall(r'[b-df-hj-np-tv-z][aeiou]', s)
    return len(count)


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        s = input()
        print(check_possibility(n, s))