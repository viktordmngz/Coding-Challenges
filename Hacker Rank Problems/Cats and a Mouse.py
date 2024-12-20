'''
https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?isFullScreen=true

Two cats and a mouse are at various positions on a line. You will be given their starting positions.
Your task is to determine which cat will reach the mouse first, assuming the mouse does not move and
the cats travel at equal speed.
If the cats arrive at the same time, the mouse will be allowed to move and it will escape while they fight.

You are given q queries in the form of x, y, and z representing the respective positions for cats A and B, and for mouse C.
Complete the function  to return the appropriate answer to each query, which will be printed on a new line.
  * If cat A reaches the mouse first, print "Cat A"
  * If cat B reaches the mouse first, print "Cat B"
  * If the cats reach at the same time, print "Mouse C"

EXAMPLE:

INPUT
2        --number of trials
1 2 3    --Cat A, Cat B, Mouse C
1 3 2    --Cat A, Cat B, Mouse C

OUTPUT
Cat B
MOUSE C

EXPLANATION
In the first scenario, Cat A is at position 1, Cat B is at position 2, and the mouse is at position 3.
Cat B will reach the mouse first.
In the second scenario, Cat A is at position 1, Cat B is at position 3, and the mouse is in the middle at position 2.
The cats will reach the mouse at the same time, allowing the mouse to escape.

'''

# !/bin/python3

# import math
# import os
# import random
# import re
# import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
  # Write your code here
  cat_a_dist = (z-x)**2
  cat_b_dist = (z-y)**2
  
  if cat_a_dist == cat_b_dist:
    return "Mouse C"
  elif cat_a_dist < cat_b_dist:
    return "Cat A"
  else:
    return "Cat B"

''' ALTERNATIVE SOLUTION -- Replace the "**2" with the abs() function

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
  cat_a_dist = abs(z-x)
  cat_b_dist = abs(z-y)
  
  if cat_a_dist == cat_b_dist:
    return "Mouse C"
  elif cat_a_dist < cat_b_dist:
    return "Cat A"
  else:
    return "Cat B"

'''
