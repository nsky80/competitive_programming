# 4 4
# 1 2
# 2 3
# 3 1
# 1 4
#
# 1


def check_root(root):
    closures = [ ]
    j = 0
    while j < len(root):
        city = [root[j][0]]
        a = root[j][0]
        for i in range(j, len(root)-1):
            if root[i][1] == root[i+1][0]:
                city.append(root[i][1])
            if root[i][1] == a:
                closures.append(city)
                j = i + 1
                break
        else:
            closures.append(root[j])
            j += 1
            print("citY j", city, j)
        print("closure", closures)
    return len(closures) - 1


if __name__ == "__main__":
    nm = list(map(int, input().rstrip().split()))
    n = nm[0]
    m = nm[1]
    root = []
    for i in range(m):
        root.append(list(map(int, input().rstrip().split())))
    print("%s" % str(check_root(root)))
