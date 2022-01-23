"""Let's learn some new Python concepts! You have to generate a list of the first  fibonacci numbers,
  being the first number. Then, apply the map fun and a lambda expn to cube each fibonacci number and print the list.

Concept

The map() function applies a function to every member of an iterable and returns the result.
It takes two parameters: first, the function that is to be applied and secondly, the iterables.
Let's say you are given a list of names, and you have to print a list that contains the length of each name.

>> print (list(map(len, ['Tina', 'Raj', 'Tom'])))
[4, 3, 3]
Lambda is a single expression anonymous function often used as an inline function.
In simple words, it is a fun that has only one line in its body. It proves very handy in functional and GUI programming.

>> sum = lambda a, b, c: a + b + c
>> sum(1, 2, 3)
6
Note:

Lambda functions cannot use the return statement and can only have a single expression.
 Unlike def, which creates a function and assigns it a name, lambda creates a function and returns the function itself.
Lambda can be used inside lists and dictionaries.

Input Format

One line of input: an integer .

Constraints


Output Format

A list on a single line containing the cubes of the first  fibonacci numbers.

Sample Input

5
Sample Output

[0, 1, 1, 8, 27]
>>> b = [[3, 2, 1], [43, 22, 12], [53, 12, 75]]
>>> b
[[3, 2, 1], [43, 22, 12], [53, 12, 75]]
>>> list(map(list.sort, b))
[None, None, None]
>>> b
[[1, 2, 3], [12, 22, 43], [12, 53, 75]]
>>>
"""

#
# cube = lambda x: x**3 # complete the lambda function
#
# def fibonacci(n):
#     # return a list of fibonacci numbers
#     a = 0
#     b = 1
#     li = []
#     if n>=2:
#         li.append(a)
#         li.append(b)
#         while n-2:
#             li.append(a+b)
#             temp = a
#             a = b
#             b = temp + b
#             n -= 1
#     elif n==1:
#         li.append(a)
#     else:
#         li = []
#     return li



# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
A = [0, 1]
for i in range(2,N): A.append(A[i-1]+A[i-2])
print(map(lambda a: a*a*a, A)[:N])


# if __name__ == '__main__':
# n = int(input())
# print(list(map(cube, fibonacci(n))))
