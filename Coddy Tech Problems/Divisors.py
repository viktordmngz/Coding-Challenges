'''
Write a program that will calculate how many t a number has, so that in a given range you output the number with most t.
If there are more numbers with the same amount of t, output the smallest of the more numbers.

INPUT
1 10

OUTPUT
6 4

Explanation:
There are two numbers from 1-10 that have 4 t: 6 and 10.
6 is the smallest, so that is what is output.

6 - 1, 2, 3, 6
10 - 1, 2, 5, 10


INPUT
10 20

OUTPUT
12 6

Explanation:
Similar to the previous example, there are two numbers with 6 t: 12 and 20.
12 is smallest, so it is output.

12 - 1, 2, 3, 4, 6, 12
20 - 1, 2, 4, 5, 10, 20
'''

# Write code here
from math import sqrt as sqrt

nums = input().split(' ')
min_num = int(nums[0])
max_num = int(nums[1])+1

divisors = []

for i in range(min_num,max_num):
    t = 0
    for j in range(1, int(sqrt(i)+1)):
        if i%j == 0:
            if i/j == j:
                t += 1
            else:
                t += 2
    divisors.append((i, t))

a = sorted(divisors, key=lambda x: x[1], reverse=True)
# print(a)

print(str(a[0][0])+" "+str(a[0][1]))
