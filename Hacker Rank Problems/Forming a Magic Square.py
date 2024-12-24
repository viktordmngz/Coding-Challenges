'''
https://www.hackerrank.com/challenges/magic-square-forming/problem?isFullScreen=true


We define a magic square to be an n*n matrix of distinct positive integers from 1 to n^2 where
the sum of any row, column, or diagonal of length n is always equal to the same number: the magic constant.

You will be given a 3x3 matrix s of integers in the inclusive range [1,9].
We can convert any digit a to any other digit b in the range [1,9] at cost of |a-b|.
Given s, convert it into a magic square at minimal cost. Print this cost on a new line.

Example:
s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

5 3 4
1 5 8
6 4 2

We can convert it to the following magic square:
8 3 4
1 5 9
6 7 2

This took three replacements at a cost of |5-8| + |8-9| + |4-7| = 7


INPUT
4 9 2
3 5 7
8 1 5

OUTPUT
1

EXPLANATION
If we change the bottom right value (s[2][2]) from 5 to 6, the square will be complete.
The cost of this exchange is |5-6| which is 1.

'''
