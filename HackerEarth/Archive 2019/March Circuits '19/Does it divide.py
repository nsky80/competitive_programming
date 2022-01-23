import math
"""Consider a permutation of numbers 1 to N written on a paper. Let’s denote the product of its element as P
and the sum of its elements as S. Given a positive integer N, your task is to determine 
whether P is divisible by S or not. """

if __name__ == "__main__":
    for _ in range(int(input().rstrip())):
        n = int(input())
        p =  math.factorial(n)
        s = (n*(n+1)//2)
        print(s)
        if p%s  == 0:
            print("YES")
        else:
            print("NO")