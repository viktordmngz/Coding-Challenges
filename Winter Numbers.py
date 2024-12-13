'''
We call a number a winter number in two cases:
* if it's a palindrome (reads the same backward or forward)
OR
* it is divisible by all of its digits

For example, 505 and 1331 are winter numbers.
They are both palindromes.

12 is also a winter number because it's divided by both 1 and 2.

Write a program that gets in the first line a number N.
In the next N rows you're given N natural numbers.
For every number, output if it's a winter number.
Output "YES" if it's a winter number, and "NO", otherwise.


Input
2
505 1331

Output
YES YES

Input
3
12 9 340

Output
YES YES NO
'''

# Enter your code here
n = int(input())
m = input()
final = ""
tests = m.split(" ")

for items in tests:
    if items[::-1] == items:
        final += "YES "
        continue
    for i in range(len(items)):
        s = 0
        if int(items[i]) == 0:
            s += 1
            break
        if int(items) % int(items[i]) != 0:
            s += 1
            break
    if s > 0:
        final += "NO "
    else:
        final += "YES "

print(final[:-1])
