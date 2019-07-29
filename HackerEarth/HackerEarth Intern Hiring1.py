def prefix_sum_array(n):
    sqr = [ i * i for i in range(1, n + 1)]
    pre = [sqr[0]]
    for i in range(1, n):
        pre.append(sqr[i] - sqr[i - 1])
    pre = [str(i) for i in pre]
    return pre


if __name__ == "__main__":
    n = int(input())
    res = prefix_sum_array(n)
    print(" ".join(res))
