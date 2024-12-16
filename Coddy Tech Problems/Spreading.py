'''
INCOMPLETE

In one neighborhood every neighbor copies the color of the houses painted gray.
So on the day that some houses are painted gray, every neighbor next to those houses horizontally and vertically decides to paint their house the same way.
They need one month for that.
After that, the houses next to them horizontally and vertically decide to do the same thing, and they take one month as well, and so on.

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
So, the neighborhood has a height 3 and width 5.
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
def main():
  # Write code here

  # dimensions
  dims = input("Enter your dimensions ('row column' format): ").split(' ')
  rows = int(dims[0])
  cols = int(dims[1])

  # incremental variables
  months = 0 #--final answer--
  target = int(input("Enter your desired # of houses: ")) #--target total--
  total = 0 #--checked against target--
  init_num_houses = int(input("Enter how many houses are painted at the start: ")) #--initial number of houses--

  # position array for painted houses
  x_pos = []

  # get coords for initial painted houses
  for i in range(init_num_houses):
    a = input("Enter the coordinates of the painted houses ('row colum' format): ").split(' ') #--takes two numbers separated by a space and makes an array
    x_pos.append([int(a[0])-1, int(a[1])-1]) #--uses increment format for positions --> '1 5' == [0, 4]

  # count total houses
  total += init_num_houses


  # while loop until target is met
  while total < target and total > 0:
    n = len(x_pos) #--used to get correct number of loops--
    
    # add new houses
    for i in range(n):
      added_x_pos = [] #--used to only track the newly added houses--
      # UP
      if x_pos[i][0]-1 <= rows-1 and x_pos[i][0]-1 >= 0:
        x_pos.append((x_pos[i][0]-1, x_pos[i][1]))
      # DOWN
      if x_pos[i][0]+1 <= rows-1 and x_pos[i][0]+1 >= 0:
        x_pos.append((x_pos[i][0]+1, x_pos[i][1]))
      # LEFT
      if x_pos[i][1]-1 <= cols-1 and x_pos[i][1]-1 >= 0:
        x_pos.append((x_pos[i][0], x_pos[i][1]-1))
      # RIGHT
      if x_pos[i][1]+1 <= cols-1 and x_pos[i][1]+1 >= 0:
        x_pos.append((x_pos[i][0], x_pos[i][1]+1))
    
    set_xpos = set([tuple(t) for t in x_pos]) #--ensure no duplicate coords--
    if total < len(set_xpos):
      total = len(set_xpos)
      months += 1

  return months

print(f"\nFinal Answer: {main()}")
