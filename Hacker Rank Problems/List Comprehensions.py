"""
List Comprehensions
https://www.hackerrank.com/challenges/list-comprehensions/problem

SUMMARY
=======

Let's learn about list comprehensions! You are given three integers x, y, and z representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by (i, j , k) on a 3D grid where the sum of i + j + k is not equal to n.

Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z.

Please use list comprehensions rather than multiple loops, as a learning exercise.

EXAMPLE(S)
==========
x = 1
y = 1
z = 2
n = 3

The combinations of [i, j, k] not equal to n are:

[ [0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,2] ]

"""

if __name__ == '__main__':
    # Given
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # Answer Below
    print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n])

    # General Note
    # List comprehension follows the following format: [ x for x in ___ if "Conditional" ]
