'''
Create a program that will output every Fibonacci number that is less than or equal to a given number N.

Write a program that gets a natural number N from input and outputs every number from the Fibonacci sequence that is less than or equal to N.

Input
3
Output
1 1 2 3

Input
6
Output
1 1 2 3 5
'''

# Enter your code here
n = int(input())
terms = "1"
a1 = 1
a2 = 0
temp = a1 + a2
while temp <= n:
    terms += " " + str(temp)
    a2 = a1
    a1 = temp
    temp = a1 + a2

print(terms)
