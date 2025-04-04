'''
In Python, a string of text can be aligned left, right and center.

.ljust(width)
- This method returns a left aligned string of length width.

>>> width = 20
>>> print 'HackerRank'.ljust(width,'-')
HackerRank----------


.center(width)
- This method returns a centered string of length width.

>>> width = 20
>>> print 'HackerRank'.center(width,'-')
-----HackerRank-----


.rjust(width)
- This method returns a right aligned string of length width.

>>> width = 20
>>> print 'HackerRank'.rjust(width,'-')
----------HackerRank


TASK

You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.

INPUT FORMAT

A single line containing the thickness value for the logo.

CONSTRAINTS

0 < thickness < 50; Thickness must be an odd integer

INPUT
5

OUTPUT
    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H 
'''

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
  #print((c*i).______(thickness-1)+c+(c*i).______(thickness-1))
  print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
  # first iteration - c*i = ''; 'H'; c*i = ''
  # second iteration - 'H'; 'H'; 'H' ==> want them in the middle ==> right, left
  # etc.

#Top Pillars
for i in range(thickness+1):
  #print((c*thickness).______(thickness*2)+(c*thickness).______(thickness*6))
  print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
  # 'H'*5 with 10 spaces; 'H'*5 with 30 spaces
  # '--HHHHH---'; '------------HHHHH-------------'

#Middle Belt
for i in range((thickness+1)//2):
  #print((c*thickness*5).______(thickness*6))
  print((c*thickness*5).center(thickness*6))
  # 'H'*25 centered with 30 spaces
  # '--HHHHHHHHHHHHHHHHHHHHHHHHH---'

#Bottom Pillars
for i in range(thickness+1):
  #print((c*thickness).______(thickness*2)+(c*thickness).______(thickness*6))
  print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
  # 'H'*5 centered with 10 spaces, 'H'*5 centered with 30 spaces
  # Same as top pillars

#Bottom Cone
for i in range(thickness):
  #print(((c*(thickness-i-1)).______(thickness)+c+(c*(thickness-i-1)).______(thickness)).______(thickness*6))
  print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
  # 'H' from 4->0; right; -- 'H' --; 'H' from 4->0; left; ===> All of this moved to the right; 30 spaces total
