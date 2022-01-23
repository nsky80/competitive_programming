"""
SAMPLE INPUT
1
baceb
SAMPLE OUTPUT
16
"""
import re


def find_vowels(string):
    # vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    res = 0
    n = len(string)
    for i in range(n):
        for j in range(i+1, n+1):
            res += len(re.findall(r'[aeiouAEIOU]', string[i]+string[i+1:j]))
            # print(string[i]+string[i+1:j])
    return res


def problem_setters_code(string):
    n = len(string)
    total = 0
    for i in range(n):
        if string[i] in 'aeiouAEIOU':
            total += (i + 1) * (n - i)
    return str(total)


if __name__ == "__main__":
    for _ in range(int(input())):
        string = input().rstrip()
        print(problem_setters_code(string))