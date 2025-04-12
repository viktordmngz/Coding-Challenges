'''
Create a function named find_occurrences that:

Takes two string arguments: text and pattern
Counts how many times pattern appears in text, including overlapping occurrences
Returns a tuple containing:
* A boolean indicating if the pattern was found (True/False)
* The number of occurrences of the pattern
* A list of starting positions where the pattern was found

For example, if text is "abababab" and pattern is "aba", your function should return (True, 3, [0, 2, 4]), since "aba" appears at positions 0, 2, and 4.

If the pattern is not found, return (False, 0, []).
'''

def find_occurrences(text, pattern):
    # Write your code here
    if pattern not in text:
        return (False,0,[])
    else:
        a = True
        b = 1
        c = [text.find(pattern)]
        while True:
            if text.find(pattern,c[-1]+1) == -1:
                break
            b += 1
            c.append(text.find(pattern, c[-1]+1))
    return (a,b,c)


text = 'hello hello hello'
pattern = 'lo'

result = find_occurrences(text, pattern)
print(result) # Should output (True, 3, [3, 9, 15])


''' PROVIDED
# Read input
text = input()
pattern = input()

# Call your function and print the result
result = find_occurrences(text, pattern)
print(result)
'''
