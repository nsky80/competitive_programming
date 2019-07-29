# 3
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry


# Enter your code here. Read input from STDIN. Print output to STDOUT
def check_number(data, queries):
    res = []
    for i in queries:
        number = data.get(i)
        if number:
            res.append("%s=%s"%(i, number))
        else:
            res.append("Not found")
    return res


def process_input():
    queries = []
    while True:
        try:
            p = list(map(str, input().rstrip().split("\n")))
            if p == '':
                break
        except EOFError:
            return queries
        queries.append(p[0])


if __name__ == "__main__":
    n = int(input())    # No. of test cases
    data = {}
    for _ in range(n):
        np = list(map(str, input().rstrip().split()))
        data[np[0]] = int(np[1])
    queries = process_input()
    print("\n".join(check_number(data, queries)))
