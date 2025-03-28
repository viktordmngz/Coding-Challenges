'''                 UNFINISHED - 4/5 Test Cases Passed
In one houses every neighbor copies the color of the houses painted gray.
So on the day that some houses are painted gray, every neighbor next to those houses horizontally and vertically decides to paint their house the same way.
They need one month for that.
After that the houses next to them horizontally and vertically decide to do the same thing, and they take one month as well, and so on.

0 0 0 0 X        0 0 X X X       0 X X X X        X X X X X
0 0 X 0 0        0 X X X X       X X X X X        X X X X X
0 0 0 0 0        0 0 X 0 0       0 X X X X        X X X X X
Mo.1             Mo.2            Mo.3             Mo.4

INPUT 1:
3 5
7
2
1 5
2 3

OUTPUT
1

EXPLANATION #1: 
We have the example from given in the text above.
So, the houses has a height 3 and width 5.
We need to output how many months are needed for a total of 7 houses to be painted gray.
There are 2 houses already painted gray they are on the positions [1, 5] and [2,3].
So, one month is needed for a total of 7 houses to be painted gray.


INPUT 2:
15 10
15
3
8 4
7 9
3 1

OUTPUT
2

'''

# On Coddy.tech, there is no function call and inputs should not have messages attached. Only did so for debugging.
# Write code here

# dimensions
dims = input().split(' ')
rows = int(dims[0])
cols = int(dims[1])
houses = []

# fill in array with 0s
for i in range(rows):
    a = []
    for j in range(cols):
        a.append(0)
    houses.append(a)

# incremental variables
months = 0 #--final answer--
target = int(input()) #--target total--
init_num_houses = int(input()) #--initial number of houses--
total = 0
pos = []

# fill in houses in intial positions
for i in range(init_num_houses):
    a = input().split(' ')
    houses[int(a[0])-1][int(a[1])-1] = 1
    pos.append([int(a[0])-1,int(a[1])-1])

total += init_num_houses #--checked against target--

'''         DEBUGGING CODE
def showHouses(arr):
  for i in range(len(arr)):
    print('\n')
    for j in range(len(arr[i])):
      print(arr[i][j], end=' ')
  print('\n')

showHouses(houses)
'''

while total < target:
    a = []
    for i in range(len(pos)):
        # left
        if pos[i][1] > 0:
            a.append([pos[i][0],pos[i][1]-1])
        # right
        if pos[i][1] < cols-1:
            a.append([pos[i][0],pos[i][1]+1])
        # up
        if pos[i][0] > 0:
            a.append([pos[i][0]-1,pos[i][1]])
        # down
        if pos[i][0] < rows-1:
            a.append([pos[i][0]+1,pos[i][1]])

    for j in range(len(a)):
        houses[a[j][0]][a[j][1]] = 1

    for i in range(len(a)):
        pos.append(a[i])

    z = set(tuple(sub_lists) for sub_lists in pos)
    total = len(z)

    '''     DEBUGGING CODE
    showHouses(houses)
    '''
    months += 1

print(months)
