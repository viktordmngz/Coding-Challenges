'''
In the game of chess, the knight is a piece shaped like a horse and it has an L-shaped movement.
If the knight is on e4, it's currently attacking d2, f2, c3, g3, c5, g5, d6 and f6.

In the first row, you are given a character, C, and a number, R, representing the column and row where your knight is placed.
In the next line is a number, N, that represents the number of chess pieces your opponent has on the table.
In the next N lines are the characters C and numbers R representing the columns and rows of the specific chess pieces.

Output the number of your opponent's chess pieces that are currently in range to be attacked by your knight.

Input
e 4
10
c 5
d 6
f 6
g 5
g 3
f 2
d 2
c 3
e 5
a 1

Output
8

Explanation
The positions currently attacked by the knight are: d2, f2, c3, g3, c5, g5, d6 and f6.
8 of your opponent's pieces are currently placed on those positions

'''

# Enter your code here
player = input()
letters = "abcdefgh"
cindex = letters.find(player[0])
rindex = int(player[-1])
total = 0

n = int(input())



pieces = []
moves = []
for i in range(n):
    pieces.append(input())

for i in range(1,3):
    for j in range(1,3):
        if i == j:
            continue
        if rindex + j < 9:
            try:
                moves.append(letters[cindex+i] + " " + str(rindex + j))
            except:
                moves.append("")
            try:
                moves.append(letters[cindex-i] + " " + str(rindex + j))
            except:
                moves.append("")
        else:
                moves.append("")
        if rindex - j > 0:
            try:
                moves.append(letters[cindex+i] + " " + str(rindex - j))
            except:
                moves.append("")
            try:
                moves.append(letters[cindex-i] + " " + str(rindex - j))
            except:
                moves.append("")
        else:
                moves.append("")

"""
UP L VERT = letter-1, row+2; letter+1, row+2
UP L HORI = letter-2, row+1; letter+2, row+1
DOWN L VERT = letter-1, row-2; letter+1, row-2
DOWN L HORI = letter-2, row-1; letter+2, row-1
"""

for item in pieces:
    if item in moves:
        total += 1

print(total)
