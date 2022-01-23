"""ab
SAMPLE OUTPUT
2"""
from itertools import permutations, combinations


if __name__ == "__main__":
    string = input()
    n = len(string)

    cmb = list(filter(lambda x: len(x) == len(set(list(x))), list(permutations(string))))
    print(cmb)
