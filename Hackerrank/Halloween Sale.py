"""
Sample Input 1

20 3 6 85
Sample Output 1

7
"""


def howManyGames(p, d, m, s):
    games = 0
    remain = s
    while p >= m and remain > 0:
        remain -= p
        print(remain)
        p -= d
        games += 1
    games += (remain // m)
    return games


if __name__ == '__main__':
    # fptr = open(os.environ[ 'OUTPUT_PATH' ], 'w')

    pdms = input().split()

    p = int(pdms[ 0 ])

    d = int(pdms[ 1 ])

    m = int(pdms[ 2 ])

    s = int(pdms[ 3 ])

    answer = howManyGames(p, d, m, s)

    print(str(answer) + '\n')
