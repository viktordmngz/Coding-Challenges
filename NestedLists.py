"""
Nested Lists Problem:
https://www.hackerrank.com/challenges/nested-list/problem


SUMMARY
========
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

EXAMPLE(S)
==========
records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]]

When the list of scores is ordered, it will look like this: [20.0, 50.0].
Therefore, 50.0 is the second-lowest score.

The result will be the names "alpha" and "beta" printed in alphabetical order.

"""

"""
							# ORIGINAL SOLUTION #
if __name__ == '__main__':
	# Added
	scores = {}
	# Given
    for _ in range(int(input())):
        name = input()
        score = float(input())
    # Answer here
		if score in scores.keys():
          scores[score].append(name)
        else:
          scores[score] = [name]
    
    keys = list(scores.keys())
    keys.sort()
    sortedScores = {k: scores[k] for k in sorted(scores)}
    for item in sorted(sortedScores[keys[1]]):
      print(item)

    # Notes: Need a way to do this with less lines/no dictionaries.
    """


    						# SECONDARY SOLUTION #
if __name__ == '__main__':	
	# Added
	records = []
	# Given
	for _ in range(int(input())):
		name = input()
		score = float(input())
	# Answer Here
		records.append([name, score])

	# Use a lambda function to sort first by score, then by names
	records.sort(key=lambda x: (x[1],x[0]))

	grades = sorted(set([grade for name,grade in records]))
	studentsSecond = [name for name,grade in records if grade == grades[1]]
	sorted(studentsSecond)
	for item in studentsSecond:
		print(item)