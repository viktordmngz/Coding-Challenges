'''
Create a function named calculateLumberProbability that receives total_logs, defected_logs, and logs_needed as its parameters.

This function aims to simulate a decision-making scenario in a spruceness sawmaker's workshop.
The sawmaker has a total of total_logs wood logs, out of which defected_logs are defective.
The sawmaker needs to randomly pick logs_needed logs for an order.
The function should calculate the probability that all the picked logs will be non-defective.

To solve this problem, you need to:

* Check if defected_logs is not greater than total_logs. If it is, return 0 as the probability.
* Check if logs_needed is greater than total_logs. If it is, return 0 as the probability.
* Calculate the number of ways to choose logs_needed non-defective logs from the total non-defective logs.
* Calculate the total number of ways to choose logs_needed logs from total_logs.
* Divide the number of ways to choose non-defective logs by the total number of ways to choose logs to get the probability.

To calculate the number of ways to choose r items from n items, you can use the combination formula:

* C(n, r) = n! / (r! * (n - r)!)
where n! represents the factorial of n.

Parameters:
* total_logs (int): The total number of wood logs in the sawmaker's workshop.
* defected_logs (int): The number of defective logs in the workshop.
* logs_needed (int): The number of logs the sawmaker needs to randomly pick for an order.
* The function returns a float representing the probability that all the picked logs will be non-defective.


INPUT
10
2
3

OUTPUT
0.46666666666667

Out of 10 logs, there is roughly a 47% chance to choose a group of 3 logs without defects.
'''

def calculateLumberProbability(total_logs, defected_logs, logs_needed):
    # Write code here
    if total_logs < logs_needed or total_logs < defected_logs:
      return 0

    numerator = 1
    denominator = 1

    for i in range(logs_needed):
        numerator *= total_logs-defected_logs-i
        denominator *= total_logs-i
    
    return numerator/denominator



