"""
You are given a rooted tree with N nodes (numbered 1 through N); node 1 is the root.
For each valid i, the i-th node has a value vi and another parameter mi.

A leaf is a node without sons. Let's denote the number of leaf nodes in the tree by L and their numbers by
l1,l2,…,lL, in increasing order. Then, for each valid i, let's define the answer for the leaf li in the following way:

Consider the path from the root to li. For each node on this path (including the root and this leaf),
choose a non-negative integer and multiply the value of this node by it.
Sum up the resulting values of all nodes on this path.
The answer ai for this leaf is defined as the maximum possible remainder of this sum modulo mli.
Find the answers for all leaves.

Input
The first line of the input contains a single integer T denoting the number of test cases.
The description of T test cases follows.
The first line of each test case contains a single integer N.
Each of the following N−1 lines contains two space-separated integers x and y denoting that nodes x and y are
connected by an edge.
The next line contains N space-separated integers v1,v2,…,vN.
The last line contains N space-separated integers m1,m2,…,mN.
Output
For each test case, print a single line containing L space-separated integers a1,a2,…,aL.

Constraints
1≤T≤8
2≤N≤105
1≤x,y≤N
1≤vi≤1018 for each valid i
1≤mi≤1018 for each valid i
the graph described on the input is a tree
Subtasks
Subtask #1 (100 points): original constraints

Example Input
1
5
1 2
2 5
1 3
3 4
2 3 4 6 7
1 2 3 2 10
Example Output
0 9
Explanation
Example case 1: There are only two leaves, l1=4 and l2=5. The answers for them are a1=0 and a2=9.
"""

