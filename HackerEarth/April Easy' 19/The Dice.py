"""
SAMPLE INPUT
3662123
SAMPLE OUTPUT
5
"""


if __name__ == "__main__":
    dice = list(map(int, list(input().rstrip())))
    girls = 0
    n = len(dice)
    idx = n
    i = 0
    flag = False

    while n >= 0 and i < idx:
        girls += 1
        if dice[i] != 6:
            n -= 1
            i += 1
        elif i+1 <= idx-1:
            count = 1
            while dice[i+1] == 6:
                count += 1
                i += 1
            else:
                i += 2
            if i+1 <= idx-1:
                n -= count
                continue
            else:
                flag = True
                break
        else:
            flag = True
            break

    print(girls if not flag else -1)