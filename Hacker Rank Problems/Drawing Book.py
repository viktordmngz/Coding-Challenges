'''
https://www.hackerrank.com/challenges/drawing-book/problem?isFullScreen=true

A teacher asks the class to open their books to a page number.
A student can either start turning pages from the front of the book or from the back of the book.
They always turn pages one at a time. When they open the book, page 1 is always on the right side.

When they flip page 1, they see pages 2 and 3.

Each page except the last page will always be printed on both sides.
The last page may only be printed on the front, given the length of the book.
If the book is n pages long, and a student wants to turn to page p, what is the MINIMUM number of pages to turn?
They can start at the beginning or the end of the book.

The first line contains an integer, n, which is the number of pages in the book.
The second line contains an integer, p, which is the page to turn to.

Example 1:

INPUT
6
2

OUTPUT
1

EXPLANATION
It will only take one turn from the first page to get to page 2.

Example 2:

INPUT
5
4

OUTPUT
0

EXPLANATION
A 5-page book will contain page 4 on the left and page 5 on the right.
If we start at the end of the book, we won't have to turn any pages to get to page 4.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    from_front = math.ceil((p-1)/2)
    from_back = int((n-p)//2)
    
    if (n%2 == 1 and n-p == 1) or p == 1 or p == n:
      return 0
    elif n%2 == 0 and n-p == 1:
      return 1
    else:
      return min(from_back, from_front)
