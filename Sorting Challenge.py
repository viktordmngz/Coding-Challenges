n = input()
n = n.split(" ")
n = [eval(i) for i in n]
n.sort()

print(n[0], n[1], n[2])
