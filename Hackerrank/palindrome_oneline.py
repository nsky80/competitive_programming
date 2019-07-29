
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    # l1 = [j for j in range(1, i + 1)]
    # temp = l1.copy()
    # temp.reverse()
    # l1.extend(temp[ 1: ])
    # print(l1, sep="")
    # # for j in range(1, i+1):
    # #     print(j, sep="", end="")
    # # print()
    print(*range(1, i+1), *range(i-1, 0, -1), sep="")
    # print(pow(((pow(10, i)) // 9), 2))
