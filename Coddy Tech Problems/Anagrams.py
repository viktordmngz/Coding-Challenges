'''
Given two numbers, tell if they are anagrams of each other.

First, you will receive how many different comparisons will need to be made.
Then, the numbers that need to be compared will be given, two for each input.
Last, you will output a single integer for how many anagrams were found.

Inputs:
n = 3

123 231
4567 6574
2345 2874

Output: 2
'''

# Enter your code here
n = int(input())

# # Uncomment this (and comment out the previous var n) for a printed input message
# # Good to use when you want to instruct users who don't know what the code does
# n = int(input("Input a number: "))

m = []
total = 0

# get inputs
for i in range(n):
    m.append(input())

    # # Uncomment here as you did before if you want to instruct your user
    # # Was not needed for Coddy.tech solution (and would make the answer invalid)
    # m.append(input("Input two numbers separated by a space (ex - '456 670'): "))

# store inputs in another array for comparisons
k = []
for item in m:
    k.append(item.split(" "))

del m, n

for i in range(len(k)):
    if ''.join(sorted(k[i][0])) == ''.join(sorted(k[i][1])):
        total += 1
print(total)
