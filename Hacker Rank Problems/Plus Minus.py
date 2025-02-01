'''
https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one

Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with 6 places after the decimal.

INPUT
-4 3 -9 0 4 1

OUTPUT
0.500000
0.333333
0.166667

EXPLANATION
There are 6 numbers total in the array. There are 3 positive numbers, 2 negative numbers, and 1 zero.

3/6 = 0.500000
2/6 = 0.333333
1/6 = 0.166667

'''

def plusMinus(arr):
  # Write your code here:
  n = len(arr)
  pos = 0
  neg = 0
  for i in range(n):
    if arr[i]>0:
      pos += 1
    elif arr[i]<0:
      neg += 1
  print('{:.6f}'.format(pos/n))
  print('{:.6f}'.format(neg/n))
  print('{:.6f}'.format(arr.count(0)/n))
