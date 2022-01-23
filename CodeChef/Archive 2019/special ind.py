def special_ind(dishes):
    res = set(dishes[0])
    for i in range(1, len(dishes)):
        res = res.intersection(set(dishes[i]))
    return len(res)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        dishes = []
        for _ in range(n):
            dishes.append(input())
        print(special_ind(dishes))