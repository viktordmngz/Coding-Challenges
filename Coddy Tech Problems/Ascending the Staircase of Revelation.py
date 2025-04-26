'''
Create a function named ascend_staircase that receives visibility_map and movements as its parameters.

Your task is to simulate a journey up an ancient, mystical staircase where each step reveals new levels of visibility in a complex, multi-dimensional environment.
As you ascend, you'll uncover more of the surroundings, and the function will need to process and update the visibility accordingly.

Implement the following rules:

* Each step up ("U") increases the visibility level of all currently visible cells by 1.
* Each step down ("D") decreases the visibility level of all currently visible cells by 1, but never below 1.
* Moving left or right ("L" or "R") reveals hidden cells (0) in a 3x3 area around the climber's new position, setting them to visibility level 1.
* The climber cannot move outside the bounds of the visibility map.


Parameters:

* visibility_map (list of lists of int): A 2D integer array representing the initial visibility of the environment.
  0 represents hidden areas, and positive integers represent visible areas with different levels of clarity.
* movements (list of str): A list of strings representing the climber's movements. Each string will be one of "U" (up), "D" (down), "L" (left), or "R" (right).
* The function returns a 2D integer array representing the final visibility map after all movements have been executed.

Use advanced array operations like map, filter, and reduce to process the visibility changes efficiently.
Implement complex conditional logic to handle edge cases and special visibility rules based on the climber's position and surrounding cells.

NOTE:
It is not explained in the instructions, but the user starts at the "bottom" and "center" of the map.
So, if the map is comprised of a 3x3 grid, the user starts in the final row and in the center.
When the columns are an even number, the starting column position is n/2 rounded up, or n//2 + 1
'''


def ascend_staircase(visibility_map, movements):
  # Write code here 
  starting_row = len(visibility_map) - 1
  starting_col = len(visibility_map[starting_row])//2
  #print(f"Starting Point: ({starting_row}, {starting_col})")
  for item in movements:
    if item == 'U':
      #print("Moved UP. New Visibility Map:\n")
      for i in range(len(visibility_map)):
        #print('\n')
        for j in range(len(visibility_map)):
          if visibility_map[i][j] > 0:
            visibility_map[i][j] += 1
          #print(visibility_map[i][j],end='\t')
      if starting_row > 0:
        starting_row -= 1
    if item == 'D':
      #print("Moved DOWN. New Visibility Map:\n")
      for i in range(len(visibility_map)):
        #print('\n')
        for j in range(len(visibility_map)):
          if visibility_map[i][j] > 1:
            visibility_map[i][j] -= 1
          #print(visibility_map[i][j],end='\t')
      if starting_row < len(visibility_map)-1:
        starting_row += 1
    if item == 'R' or item == 'L':
      if item == 'R':
        #print("Moved RIGHT. New Visibility Map:\n")
        if starting_col < len(visibility_map)-1:
          starting_col += 1
      else:
        #print("Moved LEFT. New Visibility Map:\n")
        if starting_col > 0:
          starting_col -= 1
      for i in range(len(visibility_map)):
        #print('\n')
        for j in range(len(visibility_map)):
          if i == starting_row and j == starting_col:
            if visibility_map[i][j] == 0:
              visibility_map[i][j] += 1
          if i == starting_row + 1 or i == starting_row - 1 or i == starting_row:
            if j == starting_col or j == starting_col - 1 or j == starting_col + 1:
              if visibility_map[i][j] == 0:
                visibility_map[i][j] += 1
          #print(visibility_map[i][j],end='\t')                    
  return visibility_map

'''
INPUT
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
[U]

OUTPUT
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]


INPUT
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
[R, R, U, U, L, D]

OUTPUT
[[0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 2, 2], [0, 0, 2, 2]]

NOTE:
I have included some print statements that will state which way the user moves and see the updated map.
They have been commented out as they are not needed for the solution.
'''
