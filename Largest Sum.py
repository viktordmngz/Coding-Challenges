'''
Your teacher wrote three positive numbers on the board A, B, C.

Then, your teacher gives you a challenge:
Pick one of the three numbers and replace it with its square (X2).
When you sum the three numbers after the replacement, you get the largest sum possible.

Write a function named "sum" that takes three natural numbers A, B, and C from inputs.
Return the largest sum possible with replacing one number with its square.

Input
1 5 5
Output
31
--Explanation--
We replace one of the 5s with its square - 25, so we get 1 + 5 + 25 = 31

Input
0 1 10
Output
101
--Explanation--
We replace the 10 with its square - 100, we get 0 + 1 + 100 = 101
'''

def sum(a, b, c):
    # Write code here
    n = [a, b, c]
    n_max = max(a, b, c)
    n.sort()
    n.pop(-1)
    n.append(n_max**2)
    return n[0]+n[1]+n[2]
