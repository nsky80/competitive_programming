import math
# Enter your code here. Read input from STDIN. Print output to STDOUT


def check_prime(num):
    if num > 1:
        if num % 2 == 0 and num != 2:
            return 'Not prime'
        elif num == 2 or num == 3 or num == 5:
            return 'Prime'
        else:
            flag = False
            for i in range(3, round(math.sqrt(num))+1, 2):
                if num % i == 0:
                    flag = True
                    break
                else:
                    flag = False
            if flag:
                return 'Not prime'
            else:
                return 'Prime'
    else:
        return 'Not prime'


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(check_prime(int(input())))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(check_prime(int(input())))