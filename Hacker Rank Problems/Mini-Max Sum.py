'''
https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-week-day-one

Given 5 positive integers, find the minimum and maximum values that can be calculated by summing 4 of the 5 integers.
Then, print the respective minimum and maximum values on a single line with a space between.

INPUT
1 3 5 7 9

OUTPUT
16 24

EXPLANATION
The minimum sum is found by summing 1, 3, 5, and 7.
The maximum sum is found by summing 3, 5, 7, and 9.

'''

'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
'''

def miniMaxSum(arr):
  # Write your code here
  arr.sort(reverse=True)
  high = sum(arr[:4])
  arr.sort(reverse=False)
  low = sum(arr[:4])
  print(f"{low} {high}")

'''
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
'''
