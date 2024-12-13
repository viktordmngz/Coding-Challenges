'''
PROBLEM:
If you are given a number N. Write a program that will change only one digit of the number, so that we get the largest possible number that is divisible with 3, by changing one digit from the initial number.

Given a natural number N from input. Change one digit from that number, so you get the largest number that is divisible with 3

Input
123

Output
723

Input
999
Output
996
'''
def largestNum(a1):
    '''
    1. Want to change the largest number value first
    ie: if it is a 3-digit number, we want to change the hundreds place first

    2. Want to make sure the number is not already the largest number
    ie: 999 is already the largest 3-digit number
    --> 996 is the next largest

    3. Taking an int value and changing it --> str() method?

    '''
    # Write code here
    str_num = str(a1)
    num_digits = len(str_num)

    # in case the number is already the largest divisible number
    if str_num == "9"*num_digits:
        return a1-3
    
    for i in range(num_digits):
        if str_num[i] == "9":
            continue
        for j in range(3):
            if j == 0:
                temp = str_num[:i] + "9" + str_num[i+1:]
                if int(temp) % 3 == 0 and int(temp) > a1:
                    return int(temp)
            elif j == 1:
                temp = str_num[:i] + "8" + str_num[i+1:]
                if int(temp) % 3 == 0 and int(temp) > a1:
                    return int(temp)
            else:
                temp = str_num[:i] + "7" + str_num[i+1:]
                if int(temp) % 3 == 0 and int(temp) > a1:
                    return int(temp)

largestNum(123) # Should result in 723
largestNum(999) # Should result in 996
