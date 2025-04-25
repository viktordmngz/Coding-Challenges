'''
Write a function merge_lists(list_1, list_2) that takes two sorted lists of integers and returns a single merged and sorted list.

The function should not use any built-in Python sorting functions.
'''

def merge_lists(list_1, list_2):
    # Write code here
    a = list_1 + list_2
    merged = []
    while len(a) > 0:
        merged.append(min(a))
        a.remove(min(a))
    return merged

print(merge_lists([1, 3, 4, 6, 8],[2, 5, 7, 9])) # Should output: [1,2,3,4,5,6,7,8,9]

'''
Alternate solution probably can do this faster.
'''
