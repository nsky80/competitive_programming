# 2
# abcdef
# fghi
# f f
# 9





def res(n, string):
    result = 0
    length = 0
    m = 1
    for i in string[:n-1]:
        # print(i)
        for j in string[m:]:
            # print(j)
            cnt = 0
            for k in range(min(len(i), len(j))-1):
                if i[len(i)-k-1:] == j[:k+1]:
                    # print(i[len(i)-k-1:], j[:k+1])
                    cnt = k+1
                else:
                    break
            length += cnt
        m += 1
    length1 = 0
    for i in range(n-1):

        length1 += len(string[i])
    length1 += len(string[n-1])
    return length1-length

if __name__=="__main__":
    n = int(input())
    string = []
    for _ in range(n):
        string.append(input())
    print("%s"%res(n, string))