'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def check(mat):
    path1 = False
    path2 = False
    for i in mat:
        if 1 in i:
            path1 = True
        else:
            path1 = False
            break
    temp = list(map(list, zip(*mat)))
    for i in temp:
        if 2 in i:
            path2 = True
        else:
            path2 = False
            break
    if path1 and path2:
        return 'AMBIGUOUS'
    elif path1:
        return 1
    elif path2:
        return 2
    else:
        return 0


if __name__ =='__main__':
    n = int(input())
    mat = []
    for _ in range(n):
        mat.append(list(map(int, input().rstrip().split())))
    print('%s'%check(mat))
# 4
# 0 0 0 0
# 2 0 1 0
# 0 2 1 2
# 0 1 2 0