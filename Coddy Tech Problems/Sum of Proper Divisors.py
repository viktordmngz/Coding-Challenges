'''
Write a function sum_proper_divisors(n) that takes an integer n and returns the sum of all its proper divisors.

NOTES:
Proper divisors are positive divisors of a number that are smaller than the number itself
Example - 6 --> 1,2,3
'''

def sum_proper_divisors(n):
  # Write code here
  from math import sqrt
  total = 1
  for i in range(2,int(sqrt(n))+1):
    if n%i == 0:
      total += i
      if n/i != i:
        total += n//i
  return total

print(sum_proper_divisors(12)) # Should output 16 --> 1 + 2 + 3 + 4 + 6
