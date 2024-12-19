'''
https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true

An avid hiker keeps meticulous records of their hikes.
During the last hike that took exactly "steps" steps.
For every step it was noted if it was an uphill, U, or a downhill, D, step.

Hikes always start and end at sea level, and each step up or down represents a 1 unit change in altitude.

* A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
* A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.

Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

EXAMPLE:
steps = 8
path = "DDUUUDD"

The hiker first enters a valley 2 units deep.
Finally, the hiker returns to sea level and ends the hike.

EXAMPLE 2:

INPUT
8
UDDDUDUU

OUTPUT
1

EXPLANATION
The hiker only goes below sea level once before returning to sea level and ending the hike.

_/\      _  This is a visual representation of this hike.
   \    /   Notice that there is only one valley between the two "_" points
    \/\/
'''


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
