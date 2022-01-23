"""
Distribute Apples Problem Code: DSTAPLS
Example Input
3
5 1
4 2
10 10
Example Output
NO
NO
YES

"""
# temp = n
# box1 = 0
# box2 = 0
# flag = False
# flag1 = k
# while temp - k >= 0:
#     current = temp - k
#     temp -= k
#     if not flag:
#         box1 = k
#         flag = True
#     if flag1 > 0:
#         flag1 -= 1
#         box2 += 1
# box1 = k if n >= k else n
# box2 = (n // k) if n >= k and n // k <= k else 1
# box1 = [[] * k]
# box2 = [[] * k]
# for i in range(n // k):
# return "NO" if box1 == box2 else "YES"


def fill_box(n, k):
    if n >= k:
        # for p2
        box_req = n // k
        max_occ2 = ((box_req//k) + (1 if box_req % k else 0)) * k
        min_occ2 = k * ((box_req // k) if box_req // k else 1)
        box_occ1 = k
        box_occ2 = k if box_req >= k else box_req
        # box_occ2 = (n // k) if n // k < k else k
        # for p1
        max_occ1 = min_occ1 = n // k
    else:
        max_occ2 = min_occ2 = n
        box_occ2 = 1
        max_occ1 = min_occ1 = 1
        box_occ1 = n
    # print(max_occ1, min_occ1, max_occ2, min_occ2)
    return "NO" if min_occ1 == min_occ2 and max_occ1 == max_occ2 and box_occ1 == box_occ2 else "YES"


if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = map(int, input().strip().split())
        print(fill_box(n, k))