'''
https://www.hackerrank.com/challenges/picking-numbers/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.

a = [1,1,2,2,4,4,5,5,5]
  a_1 = [1,1,2,2]
  a_2 = [4,4,5,5,5]

a_2 has 5 elements and every element is separated by at most 1.
The answer returned should be 5.

EXAMPLE

INPUT
6
4 6 5 3 3 1

OUTPUT
3

Explanation:
Here are the sub-arrays you can make: [3,3,4], [4,5], [5,6]
The longest sub-array is 3 elements long, so the answer is 3.

'''

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    s = []
    for item in a:
      b = 0
      b += a.count(item) + a.count(item-1)
      s.append(b)
    
    return max(s)
