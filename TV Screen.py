'''
A TV is drawn using numbers like below:

    1 1 1 1 1 1 1 1 1
    1 2 2 2 2 2 2 2 1
    1 2 2 2 2 2 2 2 1
    1 2 2 2 2 2 2 2 1
    1 1 1 1 1 1 1 1 3

1s - the border of the TV
2s - the actual screen
3  - the power button

You are given a sequence of numbers from input until a 3 is entered.
Calculate the width and height of the TV and output it to the screen.

Input
1 1 1 1 1 1 1 1 1
1 2 2 2 2 2 2 2 1
1 2 2 2 2 2 2 2 1
1 2 2 2 2 2 2 2 1
1 1 1 1 1 1 1 1 3

Output
5 9

Input
1 1 1
1 2 1
1 1 3

Output
3 3

'''

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
