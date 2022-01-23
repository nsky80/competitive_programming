"""
We say that some number y is reachable from x if we can apply function f to x some (possibly zero) times so that
we get y as a result. For example, 102 is reachable from 10098 because f(f(f(10098)))=f(f(10099))=f(101)=102;
and any number is reachable from itself.
"""


def check_number(num):
    count = 1
    while num > 10:
        num += 1
        while num % 10 == 0:
            num /= 10
            count += 1
        count += 1
    return count


if __name__ == "__main__":
    print(check_number(int(input())))