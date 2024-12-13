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
