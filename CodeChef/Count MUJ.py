import re


def res(string):
    res = re.search(r'MUJ', string)
    return "YES" if res else "NO"


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(res(input()))

"""3
GTRGKTRGKRMUJ
MUMUUJ
MUJMUJAA"""