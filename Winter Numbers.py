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
