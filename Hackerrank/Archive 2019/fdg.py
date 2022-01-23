def logic(n, flowers):
    cnt = 0
    petals = sum(flowers)
    if petals % 2:
        res = ':('
    else:
        res = 1


if __name__ == '__main__':
    n = int(input())
    flowers = list(map(int, input().rstrip().split()))
    print("%s"%logic(n, flowers))
