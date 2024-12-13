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