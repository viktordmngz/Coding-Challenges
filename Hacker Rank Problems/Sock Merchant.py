'''
https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true

There is a large pile of socks that must be paired by color.
Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

n=7
ar=[1,2,1,2,1,3,2]

Answer: 2 pairs
Explanation:
There is one pair of 1s and one pair of 2s in the list.
There are three unpaired socks left (1, 2, 3).
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    pairs = set(ar)
    total = 0
    for item in pairs:
      total += ar.count(item)//2
    return int(total)
