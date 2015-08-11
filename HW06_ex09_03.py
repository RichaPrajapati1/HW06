#!/usr/bin/env python
# HW06_ex09_03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write function(s)
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports

# Body
def avoids(word, forbidden):
	for letter in forbidden:
		if letter in word:
			return False
	return True

def prompt_forbidden_string():
	counter = 0
	forbidden = raw_input("Enter a forbidden string: ")
	with open("words.txt","r") as fin:
		for line in fin:
			word = line.strip()
			if avoids(word, forbidden):
				#print word
				counter += 1
	print ("Number of words avoiding %s are: %d") %(forbidden,counter)

def least_forbidden_letters():
	ascii_num = 97  #ascii value of 'a'
	forbidden_list = []
	while ascii < 123:


##############################################################################
def main():
	





if __name__ == '__main__':
    main()
