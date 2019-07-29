""""
Ari and Rich are playing a pretty confusing game. Here are the rules of the game:

The game is played with two piles of matches. Initially, the first pile contains N matches and the second one
contains M matches.
The players alternate turns; Ari plays first.
On each turn, the current player must choose one pile and remove a positive number of matches
(not exceeding the current number of matches on that pile) from it.
It is only allowed to remove X matches from a pile if the number of matches in the other pile divides X.
The player that takes the last match from any pile wins.
It can be proved that as long as both piles are non-empty, there is always at least one valid move,
so the game must end by emptying some pile. Both Ari and Rich play optimally. Determine the winner of the game.

Input
The first line of the input contains a single integer T denoting the number of test cases.
The description of T test cases follows.
The first and only line of each test case contains two space-separated integers N and M.
Output
For each test case, print a single line containing the string "Ari" (without quotes)
if Ari wins or "Rich" (without quotes) if Rich wins.

Constraints
1≤T≤105
1≤N,M≤1018
Subtasks
Subtask #1 (30 points): 1≤N,M≤1,000
Subtask #2 (70 points): original constraints

Example Input
5
1 1
2 2
1 3
155 47
6 4
Example Output
Ari
Ari
Ari
Ari
Rich
"""


def remove_match(n, m):
    if n >= m:
        div = n // m
        n -= (m * div)
    else:
        div = m // n
        m -= (n * div)
    return n, m


def game_result(n, m):
    turn = 0
    while n != 0 and m != 0:
        n, m = remove_match(n, m)
        if turn == 0 and n != 0 and m != 0:    # Ari's turn
            turn = 1
        elif n != 0 and m != 0:   # Rich's Turn
            turn = 0
    return "Ari" if turn == 0 else "Rich"


if __name__ == "__main__":
    for _ in range(int(input().rstrip())):
        print(game_result(*map(int, input().rstrip().split())))
