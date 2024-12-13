'''
In the games of football, the winner is awarded 3 points, the loser is not awarded any points and if the match is a draw, both teams get 1 point each. 

Write a program that gets a natural number N from input. In the next N lines there are three numbers W, D, L representing the wins, draws and loses of the specific team respectively.
Output the number of points that the team with most has.

Input
3
4 0 1
2 0 2
0 1 4

Output
12
'''

# Enter your code here
n = int(input())
records = []
totals = []

for i in range(n):
    records.append(input())
    totals.append(records[i].split(' '))
    
del n, records

for i in range(len(totals)):
    totals[i] = int(totals[i][0]) * 3 + int(totals[i][1])

print(max(totals))
