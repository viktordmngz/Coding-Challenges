'''
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, 'alison heck' should be capitalised correctly as 'Alison Heck'.

Given a full name, your task is to capitalize the name appropriately.

Note: in a word only the first character is capitalized.
* 12abc when capitalized remains 12abc.

INPUT
chris alan

OUTPUT
Chris Alan
'''
# PROVIDED
def solve(s):
  # DEBUGGING CODE - CAN BE COMMENTED OUT
  print(f"Old String: {s}")
  # CODE STARTS HERE
  names = s.split(' ')
  final = []
  for item in names:
    if len(item)>0:
      final.append(item[0].upper() + item[1:])
    else:
      final.append(item)

  # DEBUGGING CODE - CAN BE COMMENTED OUT
  print(f"New String: {' '.join(final)}\n")
  return ' '.join(final)

# DEBUGGING CODE - CAN BE COMMENTED OUT
solve('hello world')

# DEBUGGING CODE - CAN BE COMMENTED OUT
solve('hello   world  lol')

'''
# PROVIDED
if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  s = input()

  result = solve(s)

  fptr.write(result + '\n')

  fptr.close()
'''
