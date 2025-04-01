'''
You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa.

Example
Www.HackerRank.com --> wWW.hACKERrANK.COM

Pythonist 2 --> pYTHONIST 2

'''

# PROVIDED
def swap_case(s):
  # CODE STARTS HERE
  a = ''
  for i in range(len(s)):
    if s[i] == s[i].upper():
      a += s[i].lower()
    else:
      a += s[i].upper()
  return a

# PROVIDED
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
