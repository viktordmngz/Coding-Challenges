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
#    print(a1, '\t', a2, '\t', temp)

print(terms)
