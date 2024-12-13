'''
Grading Students
https://www.hackerrank.com/challenges/three-month-preparation-kit-grading/problem
  

Problem:
  HackerLand University has the following grading policy:
    * Every student receives a 'grade' in the inclusive range from 0 to 100.
    * Any 'grade' less than 40 is a failing 'grade'.

  Sam is a professor at the university and likes to round each student's 'grade' according to these rules:
    * If the difference between the 'grade' and the next multiple of 5 is less than 3, round 'grade' up to the next multiple of 5.
    * If the value of 'grade' is less than 38, no rounding occurs as the result will still be a failing grade.
  
  EXAMPLES:
    * 'grade' = 84 round to 85 (85 - 84 is less than 3)
    * 'grade' = 29 do not round (29 is less than 38, so rounding would still be failing)
    * 'grade' = 57 do not round (60 - 57 is not less than 3)
  
  Given the initial value of 'grade' for each of Sam's 'n' students, write code to automate the rounding process.

Function Description:
  * Complete the function gradingStudents in the editor below.
  * gradingStudents has the following parameter(s):
    * int grades[n]: the grades before rounding
  * Returns
    * int[n]: the grades after rounding as appropriate

Constraints:
  * 1 <= n <= 60
  * 0 <= grades[i] <= 100

Sample Input:
  4
  73
  67
  38
  33

Sample Output
  75
  67
  40
  33

'''

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    finalgrades = []
    for item in grades:
        if item < 38 or item % 5 < 3:
            finalgrades.append(item)
            continue
        finalgrades.append(int(round(item / 5,0) * 5))
    return finalgrades
