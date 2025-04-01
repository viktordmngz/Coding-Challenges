'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.


Input Format
The first line of input contains the original string.
The next line contains the substring.

Constraints
* 1 <= len(string) <= 200
* Each character in the string is an ASCII character

Output Format
Output the integer number indicating the total number of occurrences of the substring in the original string.

INPUT
ABCDCDC
CDC

OUTPUT
2
'''

# PROVIDED
def count_substring(string, sub_string):
  # CODE STARTS HERE
  n = len(sub_string)
  total = 0
  for i in range(len(string)-n+1):
    if string[i:i+n] == sub_string:
      total += 1
  return total


# PROVIDED
if __name__ == '__main__':
  string = input().strip()
  sub_string = input().strip()
  
  count = count_substring(string, sub_string)
  print(count)
