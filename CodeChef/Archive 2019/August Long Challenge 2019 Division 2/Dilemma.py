"""
Contest Code:AUG19B  Problem Code:CHEFDIL

Initially, N cards are placed in a row on a table. Each card is placed either face up or face down.
The goal of the game is to remove all cards from the table, one by one.
A card may be removed only if it is currently facing up.
When a card is removed, its adjacent cards (the cards directly to its left and right, if they exist) are flipped,
i.e. a card that was facing up will be facing down and vice versa.
There is an empty space left behind each removed card, i.e. the remaining cards are not moved to create a contiguous
row of cards again. Therefore, if the game starts with three cards and the middle card is removed, then the cards on
the sides are flipped, but removing one of these cards afterwards does not cause the other card to be flipped, since
it is only adjacent to the empty space created by removing the middle card.
"""
# if arr[cr] == 1:
#     arr[cr] = -1
#     if cr > 0 and arr[cr - 1] != -1:
#         if arr[cr - 1] == 0:
#             arr[cr - 1] = 1
#             f(arr, n, cr - 1)  # call with previous element
#         else:
#             arr[cr - 1] = 0
#
#     if cr < n - 1 and arr[cr + 1] != -1:
#         if arr[cr + 1] == 1:
#             arr[cr + 1] = 0
#         else:
#             arr[cr + 1] = 1
#         f(arr, n, cr + 1)  # call to next element
#     return


def f(arr, n):
    for cr in range(n):
        if arr[cr] == 1:
            arr[cr] = -1
            if cr > 0 and arr[cr-1] != -1:
                arr[cr-1] ^= 1
            if cr < n-1:
                arr[cr+1] ^= 1
        temp = cr - 1
        while temp >= 0 and arr[temp] == 1:
            arr[temp] = -1
            if temp > 0 and arr[temp-1] != -1:
                arr[temp-1] ^= 1
            temp -= 1
    return


if __name__ == '__main__':
    for _ in range(int(input())):
        s = list(map(int, input().strip()))
        f(s, len(s))
        flag = False
        for i in s:
            if i != -1:
                flag = True
                break
        if not flag:
            print("WIN")
        else:
            print("LOSE")