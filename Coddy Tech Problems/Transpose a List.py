'''
Transpose a List

To access a certain element in a list, we use indices:
```lst = ['a', 'b', 'c']
print(lst[0])```

This will output 'a' because this is the element at index 0.


But things can be more complicated. Each element in a list can also be a list:
```lst = [[1, 2, 3], [4, 5, 6]]```

To access the number 2 we need to access the first list and then the second element (index 1) in that list:

```print(lst[0][1])```

This will output 2.

Challenge

Create a function named 'transpose' that receives one argument, a list that contains lists, and returns a modified list.

Your task is to swap the rows and columns of the list. This is usually referred to as transpose in mathematics.

For example, assume this is the list:

lst = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

After transposing this list we'll get:

[
	[1, 4, 7],
	[2, 5, 8],
	[3, 6, 9]
]


Another example:

lst = [
	[1, 2],
	[4, 5],
	[7, 8]
]

Transpose:

[
	[1, 4, 7],
	[2, 5, 8]
]
'''
def transpose(lst):
  # Code Starts Here
  rows = len(lst)

  # Would like to find a different way to treat the empty case
  if rows == 0:
    return lst
  #
  
  cols = len(lst[0])
  final = []
  for i in range(cols):
    a = []
    for j in range(rows):
      a.append(lst[j][i])
    final.append(a)
  return final

if __name__ == '__main__':
  test = [[1]]
  print(f"Test #1: {test}\t\t{print(transpose(test))}\n")
  test = []
  print(f"Test #2: {test}\t\t{print(transpose(test))}\n")
  test = [[1,2]]
  print(f"Test #3: {test}\t\t{print(transpose(test))}\n")
  test = [[1,2],[3,4]]
  print(f"Test #4: {test}\t\t{print(transpose(test))}\n")
  test = [[1,2,3],[4,5,6],[7,8,9]]
  print(f"Test #5: {test}\t\t{print(transpose(test))}\n")
