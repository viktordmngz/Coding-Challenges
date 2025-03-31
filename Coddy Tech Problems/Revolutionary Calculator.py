'''
Create a function named calculate that takes an arithmetic expression as input and returns the result.
The input will be a non-empty string containing only +, -, and non-negative integers.
The function should handle an unlimited number of operands and operators.
Do not use the built-in eval function.

INPUT
1+2-3

OUTPUT
0

The input is a string, and the output is an int.

'''

def calculate(expression):
    # Write code here
    terms = ''
    symbols = ''
    for i in range(len(expression)):
      if expression[i] == '+' or expression[i] == '-':
        symbols += expression[i]
        terms += ' '
      else:
        terms += expression[i]
    terms = list(map(int,terms.split(' ')))
    
    while len(terms)>1:
      a = terms[0]
      if symbols[0] == '+':
        a += terms[1]
      else:
        a -= terms[1]
      del terms[0:2]
      symbols = symbols[1:]
      terms.insert(0,a)
    print(terms[0])
