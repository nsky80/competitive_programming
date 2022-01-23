"""
Example Input
2
23
7
Example Output
19
7
"""
def reverse_num(n):
    return int("".join(reversed(str(n))))


def reverse_max(num):
    rem = num % 10
    if rem == 9 or num < 10:
        return num
    res = max(reverse_num(num - (rem + 1)), reverse_num(num))
    return num, reverse_num(res)


if __name__ == "__main__":
    for _ in range(3000, 3101):
        print(reverse_max(_))