'''
Write a function count_inversions(arr) that takes an array of integers and returns the number of inversions in the array.

An inversion is a pair of indices (i, j) such that i < j and arr[i] > arr[j].

For example, given the array [2, 4, 1, 3, 5], the function should return 3 as there are three inversions: (1, 2),(1, 3) and (0, 2).

Extra Challenge: Use time complexity of O(n*log(n)) or better
'''

def count_inversions(arr):
    # Write code here
    total = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i > j:
                continue
            elif arr[i] > arr[j]:
                total += 1
    return total


test1 = [2, 4, 1, 3, 5]
test2 = [5, 4, 3, 2, 1]
test3 = [1, 2, 3, 4, 5]
test4 = [1, 3, 5, 2, 4, 6]
test5 = [1]

print(count_inversions(test1))
print(count_inversions(test2))
print(count_inversions(test3))
print(count_inversions(test4))
print(count_inversions(test5))
