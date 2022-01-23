from itertools import groupby, count

# lst = [0, 1, 3, 5, 7, 8, 9, 10, 12, 13]
# Explanation
# Initial Power of soldiers : 5 1 2 3 2
# 1) 0 1 5 : length of longest increasing chain in range [1,5] = 3 i.e {1,2,3}
# 2) 1 5 4 : update power of 5th solder by 4 : 5 1 2 3 6
# 3) 0 1 5 : length of longest increasing chain in range [1,5] = 4 i.e {1,2,3,6}
# 4) 0 3 5 : length of longest increasing chain in range [3,5] = 3 i.e {2,3,6}
# 5) 1 3 10 : update power of 3rd solder by 10 : 5 1 12 3 6
# 6) 0 3 5 : length of longest increasing chain in range [3,5] = 2 i.e {3,6}
# 3
# 4
# 3
# 2
# 1
# 5 6
# 5 1 2 3 2
# 0 1 5
# 1 5 4
# 0 1 5
# 0 3 5
# 1 3 10
# 0 3 5



def business_logic_layer(n, p, q):
    res = []
    for i in q:
        if i[0] == 1:
            p[i[1]-1] += i[2]
        elif i[0] == 0:
            a = p[i[1]-1:i[2]]
            # c = count()
            # print("c", c)
            # val = max((list(g) for _, g in groupby(chain, lambda x: x - next(c))), key=len)
            # print(chain, val)
            seqlist = [ ]  # List of Sequences
            seq = [ ]  # Current Sequence
            last = -1

            for item in a:
                # Start a new sequence if the gap from the last item is too big
                if item - last > 1:
                    seqlist.append(seq)
                    seq = [ ]

                # only add item to the sequence if it's not the same as the last
                if item != last:
                    seq.append(item)

                last = item

            # Print longest sequence found

            res.append(len(max(seqlist)))
    res = list(map(str, res))
    return res


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        nq = list(map(int, input().rstrip().split()))
        n = nq[0]
        q = nq[1]
        p = list(map(int, input().rstrip().split()))
        z = []
        for _ in range(q):
            z.append(list(map(int, input().rstrip().split())))
        print(p, z)
        print("\n".join(business_logic_layer(n, p, z)))
