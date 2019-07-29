"""Example Input
3
1 3 3
5 7 2
38657 76322 564
Example Output
Paja
Chef
Paja
"""


def starter(x, y, n):
    if int((x+y)/n)%2==0:
        return "Chef"
    else:
        return "Paja"


if __name__ == '__main__':
    for _ in range(int(input())):
        print(starter(*map(int, input().strip().split())))