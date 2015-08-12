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

def get_least_occurence(l):
	ascii_a = ord('a')              #ascii value of 'a'
	max_index = 0
	for i in range(len(l)):
		if l[i] > l[max_index]:
			max_index = i
	return max_index
	
def least_forbidden_letters():
	ascii_a = ord('a')              #ascii value of 'a'
	list_avoids = []
	for i in range(26):             #This loop will find the number of occurences for each letter
		list_avoids.append(0)
		with open("words.txt","r") as fin:
			for line in fin:
				word = line.strip()
				word = word.lower()
				if avoids(word,chr(i+ascii_a)):
					list_avoids[i] += 1
	for i in range(5):              #This loop will find the letter with minimum number of occurence
		max_index = get_least_occurence(list_avoids)
		print "Letter %s has count %d" %(chr(max_index+ascii_a), list_avoids[max_index])
		del list_avoids[max_index]


##############################################################################
def main():
	least_forbidden_letters()
	

if __name__ == '__main__':
    main()
