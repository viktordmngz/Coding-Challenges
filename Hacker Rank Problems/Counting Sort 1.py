'''
https://www.hackerrank.com/challenges/one-week-preparation-kit-countingsort1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two

Create an integer array whose index range covers the entire range of values in your array to sort.
Each time a value occurs in the original array, you increment the counter at that index.
At the end, run through your counting array, printing the value of each non-zero valued index that number of times.

INPUT
1 1 3 2 1

OUTPUT
[0, 3, 1, 1]

BREAKDOWN
All of the values are in the range [0...3], so create an array of zeros, s = [0,0,0,0]. The results of each iteration follow:

i	|   arr[i]   |	  result
0	|     1	     |  [0, 1, 0, 0]
1	|     1	     |  [0, 2, 0, 0]
2	|     3	     |  [0, 2, 0, 1]
3	|     2	     |  [0, 2, 1, 1]
4	|     1	     |  [0, 3, 1, 1]

The frequency array is [0, 3, 1, 1]. These values can be used to create the sorted array as well: result = [1,1,1,2,3].
'''


'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
'''


def countingSort(arr):
  # Write your code here
  s = [0]*100
  result = []
  for i in range(100):
    s[arr[i]] += 1
  return s

'''
if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  n = int(input().strip())

  arr = list(map(int, input().rstrip().split()))

  result = countingSort(arr)

  fptr.write(' '.join(map(str, result)))
  fptr.write('\n')

  fptr.close()
'''
