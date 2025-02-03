'''
https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two

Given an array of repeated numbers, find the integer that does not repeat.

INPUT
1 2 3 4 3 2 1

OUTPUT
4

'''


'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
'''

def lonelyinteger(a):
  # Write your code here
  for i in range(len(a)):
    if a.count(a[i]) < 2:
      return a[i]


'''
if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  n = int(input().strip())

  a = list(map(int, input().rstrip().split()))

  result = lonelyinteger(a)

  fptr.write(str(result) + '\n')

  fptr.close()
'''
