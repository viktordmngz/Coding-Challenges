'''
Created By: Viktor Dominguez
Date Created: 12/12/2024
Last Updated: 12/12/2024


Given a number, N, return the column heading that the number corresponds to.
The columns start at A and go to Z.
Then, the pattern will loop and start again at AA, AB, etc.


* INPUT 1:
  24

  OUTPUT
  X

* INPUT 2:
  52

  OUTPUT
  AZ

* INPUT 3:
  105

  OUTPUT
  DA

* INPUT 4:
  677

  OUTPUT
  AAA

Explanation:
677 is AAA because 676 is 26^2, or the last 2-lettered column (ZZ)
'''

def columnHeader(n):
  letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  result = ""

  # Find how many letters we will need
  power = 1 #--Storing as "power" since it will mainly be used as an exponent--

  # Run until we find the number of letters
  while True:
    if n <= 26**power and n > 26**(power-1):
      break
    else:
      power += 1
  
  # First Letters
  for i in range(power-1):
    result += letters[(n-(26**(power-1))-1)//26]

  # Last Letter
  result += letters[n%26-1]

  return result


# # Uncomment to test
# print(columnHeader(24), columnHeader(52), columnHeader(105))
# print(columnHeader(677))
