'''
Write a program that will read three numbers and it will sort them in an ascending order and after that will output the sequence.

Input
2 4 3
Output
2 3 4

Input
6 1 2
Output
1 2 6

'''

n = input()
n = n.split(" ")
n = [eval(i) for i in n]
n.sort()

print(n[0], n[1], n[2])
