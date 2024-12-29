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


Currently working on an alternate solution on HackerRank:

def formingMagicSquare(s):
  # # Write your code here
  values = {'coords':[], 'available': [1,2,3,4,5,6,7,8,9], 'safe_values':[]}
  cost = 0
  
  def rowSum(row):
    total = 0
    for item in row:
      total += item
    return total
  
  def colSum(matrix,index):
    total = 0
    for i in range(len(matrix)):
      total += matrix[i][index]
    return total
  
  def diagDownRightSum(matrix):
    total = 0
    for i in range(len(matrix)):
      for j in range(len(matrix[i])):
        if i == j:
          total += matrix[i][j]
    return total
  
  def diagUpRightSum(matrix):
    total = 0
    for i in range(len(matrix)):
      for j in range(len(matrix[i])):
        if i + j == 2:
          total += matrix[i][j]
    return total
  
  # Initial matrix row, column, and diagonals checks
  for i in range(len(s)):
    if rowSum(s[i]) == 15:
      for j in range(len(s[i])):
        if [i,j] not in values['coords']:
          values['coords'].append([i,j])
          values['safe_values'].append(s[i][j])
          values['available'].remove(s[i][j])
    if colSum(s,i) == 15:
      for j in range(len(s[i])):
        if [j,i] not in values['coords']:
          values['coords'].append([j,i])
          values['safe_values'].append(s[j][i])
          values['available'].remove(s[j][i])
    if diagDownRightSum(s) == 15:
      for j in range(len(s[i])):
        if i == j:
          if [i,j] not in values['coords']:
            values['coords'].append([i,j])
            values['safe_values'].append(s[i][j])
            values['available'].remove(s[i][j])
    if diagUpRightSum(s) == 15:
      for j in range(len(s[i])):
        if i + j == 2:
          if [i,j] not in values['coords']:
            values['coords'].append([i,j])
            values['safe_values'].append(s[i][j])
            values['available'].remove(s[i][j])
'''
