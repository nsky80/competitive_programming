# Sample Input
#
# Sorting1234
# Sample Output
#
# ginortS1324

import re

if __name__ == "__main__":
    b = input()
    n = list(map(int, re.findall(r'[0-9]', b)))
    even_lst = []
    odd_lst = []
    for j in n:
        if j % 2 == 0:
            even_lst.append(j)
        else:
            odd_lst.append(j)
    s = re.findall(r'[a-z]', b)
    u = re.findall(r'[A-Z]', b)
    s.sort()
    u.sort()
    even_lst.sort()
    odd_lst.sort()
    res = "".join(["".join(s), "".join(u), "".join(list(map(str, sum([odd_lst, even_lst], []))))])
    print(res)
