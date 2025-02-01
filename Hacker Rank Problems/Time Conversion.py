"""
https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one

Given a time in a 12-hour AM/PM format, convert it to military (24-hour) time.

Example:
s = '12:01:00PM'
  Return '12:01:00'

s = '12:01:00AM'
  Return '00:01:00'

INPUT
07:05:45PM

OUTPUT
19:05:45

EXPLANATION
07:05:45 PM in military time is 19:05:45.
Because military time uses the full 24 hours, there's no need to have the AM/PM designation.
However, there is always 2 digits for each position.
So, 01:15:15 AM would be 01:15:15 in military time.

"""

"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
# 
"""

def timeConversion(s):
  # Write your code here
  if s.upper().find('PM') != -1:
    a = int(s[:2])%12 + 12
    s = s.replace(s[:2],str(a))
  elif s.upper().find('AM') != -1:
    a = int(s[:2])%12
    if a < 10:
      a = '0'+str(a)
    s = s.replace(s[:2],str(a))
  return s[:-2]

"""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
"""
