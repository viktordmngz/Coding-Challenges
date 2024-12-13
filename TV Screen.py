# Enter your code here
rows = 0
cols = 0

while True:
    m = input()
    m = m.replace(' ', '')
    cols = len(m)
    rows += 1
    if m[-1] == '3':
        break

print(f"{rows} {cols}")
