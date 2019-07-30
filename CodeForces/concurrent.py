"""
Input
The first line contains one integer n (1≤n≤2⋅105) — the length of showcase string s.

The second line contains string s, consisting of exactly n lowercase Latin letters.

The third line contains one integer m (1≤m≤5⋅104) — the number of friends.

The i-th of the next m lines contains ti (1≤|ti|≤2⋅105) — the name of the i-th friend.

It is guaranteed that ∑i=1m|ti|≤2⋅105.

Output
For each friend print the length of the shortest prefix of letters from s s/he would need to buy to be able to construct
her/his name of them. The name can be constructed if each letter is presented in the equal or greater amount.

It is guaranteed that every friend can construct her/his name using the letters from the string s.



inputCopy
9
arrayhead
5
arya
harry
ray
r
areahydra
outputCopy
5
6
5
2
9
"""

# import re
# import copy
#
# def ds(s):
#     li = [[] for i in range(27)]
#     for i, j in enumerate(s):
#         li[ord(j) - 96].append(i)
#     return li
#
#
# def position(s, name):
#     res = 0
#     for i in name:
#         ind = s[ord(i) - 96].pop(0)
#         res = max(res, ind)
#     return res + 1
#
#
# if __name__ == '__main__':
#     n = int(input())
#     s = input().strip()
#     li = ds(s)
#     for _ in range(int(input())):
#         print(position(copy.deepcopy(li), input().strip()))


def printMaxActivities(s, f):
    n = len(f)
    print("The following activities are selected")

    # The first activity is always selected
    i = 0
    print(i)

    # Consider rest of the activities
    for j in range(n):

        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if s[j] >= f[i]:
            print(j)
            i = j

        # Driver program to test above function


s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
printMaxActivities(s, f)