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
#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
  # Write your code here
  row_cost = []
  col_cost = []
  
  for i in range(3):
    row_cost.append(15-sum(s[i]))
    col_cost.append(15-sum([s[0][i],s[1][i],s[2][i]]))
  
  return sum(row_cost)+sum(col_cost)

'''
Current issues:
  Cannot track the changes properly
  Double counting if there is a change in the row and column

Need a way to track the changes as they are made.
Maybe make the row changes first, then the columns.
  Then, check the changes compared to the original array

'''
