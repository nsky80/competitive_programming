"""
Problem Code: KS1

Example Input
1
3
5 2 7
Example Output
2
Explanation
Example case 1: The triples are (1,3,3), since 5⊕2=7, and (1,2,3), since 5=2⊕7.

# Sample Data testing
1
5
3 2 5 6 4
"""


def find_triplets(n, arr):
    count = 0
    main_ = [arr[0]]
    for i in range(1, n):
        main_.append((main_[-1] ^ arr[i]))
    for m in range(n-1):
        main_cur = arr[m]
        main1 = main_.copy()
        for i in range(m, n):
            cur = main_[i]
            derived = list(map(lambda x: x ^ arr[i], main1))
            for j in range(i+1, n):
                # print(main_, main1, derived)
                if cur == derived[j]:
                    count += 1
            main1 = derived
            print()
        main_ = list(map(lambda x: x ^ main_cur, main_))
    return count


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().strip().split()))
        print(find_triplets(n, a))
