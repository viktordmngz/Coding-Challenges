'''
https://www.hackerrank.com/challenges/electronics-shop/problem?isFullScreen=true

A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a given budget.
Given price lists for keyboards and USB drives and a budget, find the cost to buy them.
If it is not possible to buy both items, return -1.

Example:
b = 60   --Budget
keyboards = [40,50,60]
drives = [5,8,12]

The person can by a keyboard worth 40 and a USB worth 12.
Or, they can buy a keyboard worth 50 and a USB worth 8.

Since the latter option is more expensive, go with that.

Complete the getMoneySpent function in the editor below.

getMoneySpent has the following parameter(s):
* int keyboards[n]: keyboard prices
* int drives[m]: USB prices
* int b: the budget

Returns:
* int: maximum spent or -1 if not possible.


EXAMPLE:

INPUT
10 2 3  -- b, n, m
3 1     -- keyboards[]
5 2 8   -- drives[]

OUTPUT
9

EXPLANATION
You can buy the last keyboard and last USB for 1 and 8 respectively. This gives you 1 + 8 = 9.


'''

#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
  #
  # Write your code here.
  total = []
  for k_price in keyboards:
    for d_price in drives:
      if k_price + d_price <= b:
        total.append(k_price + d_price)
  if not total:
    return -1
  else:
    return max(total)
