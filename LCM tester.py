'''
Write a function named lcm that given two natural numbers a and b from input.
Return their LCM in the code block.

The Least Common Multiple (LCM) for two integers a and b is the smallest positive integer that is evenly divisible by both a and b.

In these examples, "Input" refers to the arguments used in the function.

Input
2 3 
Output
6

Input
4 8 
Output 
8
'''
def lcm(a, b):
    # Write code here
    if a%b == 0 or b%a == 0:
        return max(a,b)
    for i in range(1, 1000):
        if a*i%b == 0:
            return a*i

print(lcm(2, 3), lcm(4, 8))
