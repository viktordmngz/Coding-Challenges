'''
Date Created: 12/12/2024
Last Updated: 12/13/2024

Description:

Given a number, return the column heading that the number corresponds to.
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
  703
  OUTPUT
  AAA
'''

def columnHeader(n):
  letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  result = ""

  # Initialize some variables that will be used to determine how many letters we need
  num = 1 #--used to track how many letters we need--
  lower_bound = 26**(num-1)   #--init at 1--
  upper_bound = 26**(num)     #--init at 26--

  # Test our n to determine how many letters we will need
  while n > upper_bound:
    num += 1 #--increment the number of letters by 1--
    lower_bound += 26**(num-1) #--Add the next term; for num = 2 ==> 1 + 26 = 27--
    upper_bound += 26**(num)   #--Add the next term; for num = 2 ==> 26 + 676 = 702--

  '''
              BRAINSTORMING SECTION
==========================================================================================
  703 --> 0 for the first letter
      --> 0 for the second letter
      --> 0 for the last letter

  ** 703 % 26 --> 1 ==> (n-1) % 26 = Last Letter

  ** ((703-1) - 26**(num-1)) % 26 = Second Letter
      Can check this by adding 27 to 703 to see if it returns 1; (729 - 26**2) % 26 = 1; SUCCESS
  
  ** Need to find First Letter, which changes ever 26**2 numbers after lb
      lb = 703:
      'A' --> [703, 1378]; 'B' --> [1379, 2054]; etc.
  
    ((703-1) - 26**(num-1)) // 26 ==> 702 - 676 = 26; 26//26 = 1 --> x

    ((n-lb))//(26**(num-1)) --> 0; First Letter
      Check by adding 26^2 to (n-lb) part to see if it changes to 1; SUCCESS
==========================================================================================
  
  Need to loop so that we do the same steps, no matter how long the answer should be
    If num is 1, we should use the same steps as we would if num was 3
  
  i=0 --> Last Letter:
    (n-lower_bound) // 26**0 % 26**1;
      * "// 26**0"  --> floor division by 1 returns the (n-lower_bound) part
                        Since the lower bound is inclusive, the first value we can get is 0 and the last is 26**num - 1
      * "% 26**1"   --> is needed because for higher values, (n-lower_bound) // 26**0 will exceed the indexing of letters[]
                        Won't be needed for other letters, but it won't affect the answer by including it

  i=1 --> Middle Letter:
    (n-lower_bound) // 26**1 % 26**1;
      * "// 26**1"  --> ensures that the letter does not change until (n-lower_bound) exceeds 26
  
  i=2 --> First Letter:
    (n-lower_bound) // 26**2 % 26**1;
      * "// 26**2"  --> ensures that the letter does not changed until (n-lower_bound) exceeds 676

  '''

  for i in range(num):
    result += letters[(n-lower_bound) // 26**i % 26]

  result = result[::-1]
  print(result)


# # Uncomment to test
# columnHeader(24)       #--X--
# columnHeader(52)       #--AZ--
# columnHeader(105)      #--DA--
# columnHeader(703)      #--AAA--
# columnHeader(18279)    #--AAAA--
