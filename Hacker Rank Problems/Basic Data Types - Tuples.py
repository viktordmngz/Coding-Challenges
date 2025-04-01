'''
Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers.
Then, compute and print the result of hash(t).

Note: hash() is a built-in function, so no need to import it.

Input Format
The first line contains an integer, n, denoting the number of elements in the tuple, t.
The second line contains n space-separated integers.

Output Format
Print the result of hash(t)

'''

# PROVIDED
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    # CODE STARTS HERE
    print(hash(tuple(integer_list)))
