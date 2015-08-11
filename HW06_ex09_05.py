#!/usr/bin/env python
# HW06_ex09_05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou:
#   - # of words that use all aeiouy:
##############################################################################
# Imports

# Body
def uses_all(word,required):
	for letter in required:
		if letter not in word:
			return False
	return True

##############################################################################
def main():
	counter_aeiou = 0
	counter_aeiouy = 0
	with open("words.txt","r") as fin:
		for word in fin:
			if uses_all(word, 'aeiou'):
				counter_aeiou += 1
			if uses_all(word,'aeiouy'):
				counter_aeiouy += 1
	print ("Number of words with aeiou are: %d") %(counter_aeiou)
	print ("Number of words with aeiouy are: %d") %(counter_aeiouy)


if __name__ == '__main__':
    main()
