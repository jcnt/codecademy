#!/usr/bin/python

# import modules used here -- sys is a very standard one
import sys
import random

# Gather our code in a main() function
def main():
	for i in xrange(6):
		yield random.randint(1, 4000)

for random_number in main():
	print "the next random number is %d" % random_number



# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()


