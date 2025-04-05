'''
You are given an integer, N. Your task is to print an alphabet rangoli of size N.
Rangoli is a form of Indian folk art based on creation of patterns.

Different sizes of alphabet rangoli are shown below:
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------


The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical order).


Function Description:
* int size: the size of the rangoli

Return:
* string: a single string made up of each of the lines of the rangoli separated by the newline character (\n)

Input Format:
* a single integer

Constraints:
* 0 < size < 27

'''

# PROVIDED
def print_rangoli(size):
    # your code goes here
    width = 4*size - 3
    letters = 'abcdefghijklmnopqrstuvwxyz'
    final = ''
    if size == 1:
      return 'a'

    #rows
    for i in range(1,2*size):
      if size == 1:
        final += 'a'
        break
      dashes = -2*i+int((width+3)/2)
      # top half pattern
      if i < size:
        final += '-'*dashes + '-'.join(letters[size-1:size-i-1:-1]) + '-'.join(['', *letters[size-i+1:size]]) + '-'*dashes + '\n'
      # middle row
      if i == size:
        final += '-'.join(letters[size-1:0:-1]) + '-' + letters[0] + '-' + '-'.join(letters[1:size]) + '\n'
      # bottom half
      if i > size:
        dashes = (2*i)-(2*size)
        final += '-'*dashes + '-'.join(letters[size-1:i-size-1:-1]) + '-'.join(['', *letters[i-size+1:size]]) + '-'*dashes + '\n'
    print(final)

# PROVIDED
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
