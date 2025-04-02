'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

* Mat size must be NxM. ( is an odd natural number, and M is 3 times N.)
* The design should have 'WELCOME' written in the center.
* The design pattern should only use |, . and - characters.

Sample Designs
Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------



INPUT
9 27

OUTPUT
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

'''

# CODE STARTS HERE

dims = input().split(' ')
n = int(dims[0])
m = int(dims[1])

b = '-'
c = ".|."
d = "WELCOME"

for i in range(1, n+1):
  if i < n/2:
    print(b*int((m-3*(2*i-1))/2) + c*(2*i-1) + b*int((m-3*(2*i-1))/2))
  elif i == n//2+1:
    print(b*int((m-7)/2) + d + b*int((m-7)/2))
  else:
    print(b*int((m-3*(-2*i+(2*n+1)))/2) + c*(-2*i+(2*n+1)) + b*int((m-3*(-2*i+(2*n+1)))/2))
  
