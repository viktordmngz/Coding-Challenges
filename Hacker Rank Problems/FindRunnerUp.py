"""
Find The Runner-Up Score!
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

SUMMARY
========
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

INPUT FORMAT
============
The first line contains n. The second line contains an array A[] of n integers each separated by a space.

CONSTRAINTS
============
* 2 <= n <= 10
* -100 <= A[i] <= 100

OUTPUT FORMAT
=============
Print the runner-up score.


EXAMPLE(S)
==========

5
2 3 6 6 5

Answer: 5
"""

if __name__ == '__main__':
    # Given
    n = int(input())
    arr = map(int, input().split())
    # Answer Below Here
    arr = list(set(arr))
    arr.sort()
    print(arr[-2])