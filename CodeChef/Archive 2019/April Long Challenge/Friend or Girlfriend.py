"""
Shlok and Sachin are good friends. Shlok wanted to test Sachin, so he wrote down a string S with length N and one
character X. He wants Sachin to find the number of different substrings of S which contain the
character X at least once. Sachin is busy with his girlfriend, so he needs you to find the answer.

Two substrings of S are considered different if their positions in S are different.

Input
The first line of the input contains a single integer T denoting the number of test cases.
The description of T test cases follows.
The first line of each test case contains a single integer N.
The second line contains a string S with length N, followed by a space and a character X.
Output
For each test case, print a single line containing one integer — the number of substrings of S that contain X.

Constraints
1≤T≤1,000
1≤N≤106
S contains only lowercase English letters
X is a lowercase English letter
the sum of N over all test cases does not exceed 106
Subtasks
Subtask #1 (30 points): the sum of N over all test cases does not exceed 103
Subtask #2 (70 points): original constraints

Example Input
2
3
abb b
6
abcabc c
Example Output
5
15
Explanation
Example case 1: The string "abb" has six substrings: "a", "b", "b", "ab", "bb", "abb".
The substrings that contain 'b' are "b", "b", "ab", "bb", "abb".
"""
from collections import defaultdict


def generate_permutations(n, s, x):
    counter = 0
    for i in range(n):
        main_str = s[i]
        for j in range(i+1, n+1):
            if x in main_str + s[i+1:j]:
                counter += 1
    return counter


def generate_sets(length, string, x):   # TLE optimize it
    count = 0
    ss = []
    for i in range(length):
        if string[i] == x:
            count += (n - i)
            # print("from i:", n-i)
            continue
        for j in range(i, length):
            if string[j] == x:
                count += (n - j)
                # print("from j: ",string[j], n-i-1, n-j)
                break

            # temp = string[i:j + 1]
            # if x in temp:
            #     count += 1
    #         ss.append(temp)
    # print(ss)
    return count


"""abcabc c['a', 'ab', 'abb', 'b', 'bb', 'b']
5

['a', 'ab', 'abc', 'abca', 'abcab', 'abcabc', 'b', 'bc', 'bca', 'bcab', 'bcabc', 'c', 'ca', 'cab', 'cabc', 'a', 'ab', 'abc', 'b', 'bc', 'c']
15"""

def problem_setters_code(n, string, x):
    total = 0
    for i in range(n):
        if string[i] == x:
            temp = (n - (i + 1))
            total += ((i + 1) * (temp if temp else 1))
    return str(total)


def fourth_try(n, string, x):   # WA
    ds = defaultdict(int)
    count = 0
    for i in string:
        ds[i] += 1

    res = (2**ds[x] + 1) * (n//2)
    return res


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        s, x = map(str, input().rstrip().split())
        print(generate_sets(n, s, x))
