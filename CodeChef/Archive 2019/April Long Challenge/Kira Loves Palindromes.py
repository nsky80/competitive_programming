"""
You are given a string S. Find the number of ways to choose a pair of non-overlapping non-empty substrings of this
string (let's denote them by s1 and s2) such that their concatenation s1+s2 is a palindrome.

Two pairs (s1,s2) and (s′1,s′2) are different if s1 is chosen at a different position from s′1 or s2 is chosen
at a different position from s′2.

Input
The first and only line of the input contains a single string S.

Output
Print a single line containing one integer — the number of ways to choose a valid pair of substrings.

Constraints
1≤|S|≤1,000
S contains only lowercase English letters
Subtasks
Subtask #1 (25 points): |S|≤100
Subtask #2 (75 points): original constraints

Example Input
abba
Example Output
7
Explanation
The following pairs of substrings can be chosen: ("a", "a"), ("a", "ba"), ("a", "bba"), ("ab", "a"), ("ab", "ba"),
("abb", "a"), ("b", "b").
"""
from collections import Counter


def is_palindrome(a, b):
    temp = a + b
    if temp == temp[::-1]:
        return True
    else:
        return False


def validate(first, second):
    # print(first, second, end=" ")
    res = False
    for k in first.keys():
        if first[k] <= second[k]:
            res = True
            continue
        else:
            res = False
            break
    # print(res)
    return res


def check_pairs(string):
    n = len(string)
    count = 0
    dic = Counter(list(string))
    subsets = generate_sets(string)
    # print(subsets)
    for idx, st in enumerate(subsets):
        for j in range(idx+1, len(subsets)):
            temp = st + subsets[j]
            if len(temp) > n:
                continue
            else:
                if validate(Counter(list(temp)), dic):
                    if is_palindrome(st, subsets[j]):
                        count += 1
    return count


def generate_sets(string):
    length = len(string)
    ss = []
    for i in range(length):
        for j in range(i, length):
            ss.append(string[i:j + 1])
    return ss


"""['a', 'ab', 'abb', 'abba', 'b', 'bb', 'bba', 'b', 'ba', 'a']"""



if __name__ == "__main__":          # TLE
    print(check_pairs('abba'))

