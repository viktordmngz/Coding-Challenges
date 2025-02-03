'''
https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two

Given a square matrix, find the absolute difference between the diagonals.

INPUT
1 2 3
4 5 6
9 8 9

OUTPUT
2

EXPLANATION
d1 = 1 + 5 + 9
d2 = 9 + 5 + 3

|d1-d2| = 2

'''

'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
'''


def diagonalDifference(arr):
  # Write your code here
  n = len(arr)
  d1 = 0
  d2 = 0
  for i in range(n):
    for j in range(n):
      if i == j:
        d1 += arr[i][j]
      if i+j == n-1:
        d2 += arr[i][j]
  return abs(d1-d2)

'''
if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  n = int(input().strip())

  arr = []

  for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

  result = diagonalDifference(arr)

  fptr.write(str(result) + '\n')

  fptr.close()
'''
