# The winning team is the one with the largest score.
# In case of a tie between two or more teams, the one with the fewest members wins.
# If there is still a tie between two or more teams then the one with the lowest index wins.
# #
# 1
# 2 qwopwasp
# wdw
# abco


def check(n, s, team):
    s = list(s)
    win = 0
    score = 0
    n = 0
    for i in team:
        common = list(set(s).intersection(set(i)))
        for j in common:
            score += s.count(j)
        # if win < score:
    #         n = common.index(j)
    #         win = score
    #     if win == score:
    #
    # return score

if __name__ =="__main__":
    t = int(input())
    for _ in range(t):
        n, s = map(str, input().split())
        n = int(n)
        team = []
        for _ in range(n):
            team.append(input())
        print(check(n, s, team))
