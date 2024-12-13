'''
You are given a sequence which begins with 1 and after every element the added sequence increases. 
But, it starts over as follows: 112123123412345123456

Given a natural number N from input. Return the N-th digit of the given sequence.

Input
10
Output
4

Input
17
Output
2

'''

def digit(n):
    # Write code here
    a = 1
    numbers = ""
    while len(numbers) < n:
        for i in range(1,a+1):
            numbers += str(i)
        a += 1
    return int(numbers[n-1])
