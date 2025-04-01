'''
Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer  at position .
2. print: Print the list.
3. remove e: Delete the first occurrence of integer .
4. append e: Insert integer  at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be one of the 7 listed above.
Iterate through each command in order and perform the operation to your list.

EXAMPLE

N = 4
append 1
append 2
insert 1 3
print

append 1    --> [1]
append 2    --> [1,2]
insert 1 3  --> [1,3,2]
print       --> >>[1,3,2]


INPUT
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

OUTPUT
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''

# PROVIDED
if __name__ == '__main__':
    N = int(input())
    # CODE STARTS HERE
    a = []
    for i in range(N):
      command = input().split(' ')
      if command[0] == "print":
        print(a)
      elif command[0] == "append":
        a.append(int(command[1]))
      elif command[0] == "insert":
        a.insert(int(command[1]),int(command[2]))
      elif command[0] == "sort":
        a.sort()
      elif command[0] == "pop":
        a.pop()
      elif command[0] == "remove":
        a.remove(int(command[1]))
      elif command[0] == "reverse":
        a.reverse()
