As you know, in Python, lists can have elements that are themselves list whose elements are themselves lists whose …

For example, x= [1,2, [3, [4, 5, [6], 7, [8,9, [ [ [11,12] ] ] ] ] ]

We would like to “free” all the elements so that we end up with a list:

[1, 2, 3, 4 ,5, 6, 7, 8, 9, 10, 11, 12].

Write a recursive function

freeThem(z)

which take a list like x above and return a list with all the elements from z in a single list, in the order in which they are encountered in z. You may assume that all the non-list elements of z are integers.

Hint:

You can tell if an element i is an integer by asking if type(i) == type(1). If it's not an integer then it must be a list.
The list methods extend and append should be helpful here
