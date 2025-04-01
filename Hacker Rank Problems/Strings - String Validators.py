'''
Python has built-in string validation methods for basic data.
It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

1. str.isalnum()
- This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
>>> print 'ab123'.isalnum()
True
>>> print 'ab123#'.isalnum()
False

2. str.isalpha()
- This method checks if all the characters of a string are alphabetical (a-z and A-Z).
>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False

3. str.isdigit()
- This method checks if all the characters of a string are digits (0-9).
>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False

4. str.islower()
This method checks if all the characters of a string are lowercase characters (a-z).
>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False

5. str.isupper()
This method checks if all the characters of a string are uppercase characters (A-Z).
>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False


TASK
You are given a string S.
Your task is to find out if the string S contains:
* alphanumeric characters
* alphabetical characters
* digits
* lowercase characters
* uppercase characters


INPUT
qA2

OUTPUT
True
True
True
True
True
'''

# PROVIDED
if __name__ == '__main__':
    s = input()
    # CODE STARTS HERE
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    
    for i in range(len(s)):  
      if s[i].isalnum() == True:
        alnum = True
      if s[i].isalpha() == True:
        alpha = True
      if s[i].isdigit() == True:
        digit = True
      if s[i].islower() == True:
        lower = True
      if s[i].isupper() == True:
        upper = True
    print(alnum,alpha,digit,lower,upper,sep='\n')
