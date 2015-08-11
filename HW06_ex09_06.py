#!/usr/bin/env python
# HW06_ex09_05.py

# (1)
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok).
#   - write is_abecedarian
# (2)
# How many abecedarian words are there?
#   - write function(s) to assist you
#   - number of abecedarian words:
##############################################################################
# Imports

# Body
def is_abecedarian(word):
	previous = word[0]
	for letter in word:
		if letter < previous:
			return False
		previous = letter
	return True



##############################################################################
def main():
    #pass  # Call your function(s) here.
    counter = 0
    fin = open ("words.txt","r")
    for line in fin:
        word = line.strip()
    	if is_abecedarian(word):
    		counter += 1
    fin.close()
    print ("The number of abecedarian words are: %d") %(counter)


if __name__ == '__main__':
    main()
