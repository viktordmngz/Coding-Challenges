'''
https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true

Two friends Anna and Brian, are deciding how to split the bill at a dinner.
Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

For example, assume the bill has the following prices: bill = [2, 4, 6].
Anna declines to eat item k=bill[2] which costs 6.
If Brian calculates the bill correctly, Anna will pay (2+4)/2 = 3.
If he includes the cost of bill[2], he will calculate (2+4+6)/2 = 6.
In the second case, he should refund 3 to Anna.

Complete the bonAppetit function in the editor below. It should print Bon Appetit if the bill is fairly split. Otherwise, it should print the integer amount of money that Brian owes Anna.

bonAppetit has the following parameter(s):

* bill: an array of integers representing the cost of each item ordered
* k: an integer representing the zero-based index of the item Anna doesn't eat
* b: the amount of money that Anna contributed to the bill
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    
    b_actual = 0 #--what bill should have charged anna

    for i in range(len(bill)):
        if i == k:
            continue
        else:
            b_actual += bill[i]
    b_actual /= 2

    # if Anna paid less than what bill should have charged...
    if b <= b_actual:
        print("Bon Appetit")
    # if Anna paid what she owed or more...
    else:
        print(int(b-b_actual))

'''
If testing, you can use return statements instead of print statements.

Inputs:
bill=[3,10,2,9]
k=1
b=12

Expected Output:
5

Inputs:
bill=[3,10,2,9]
k=1
b=7

Expected Output:
Bon Appetit
'''
