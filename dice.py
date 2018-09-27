#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Rolling one, two or three dices.

# Author: __ekarlsson66@gmail.com__
# Date: __2018.09.27__
# Version: __001__

# Rolls one, two or three dices. User input "n" starts 30 sec countdown then
# throws one dice. 

import time
from random import randint

min = 1
max = 6


def count_down(secs=30):
	"""Count down 30 sec. Then throws one dice."""
	while (secs > 0):
		print secs
		secs = secs - 1
		time.sleep(1)
		if secs == 0:
			print "Dice: %d" % randint(min, max)

def one_crap():
	"""Roll just one dice."""
	print "Ready to roll? y/n"
	roll = raw_input()
	if roll == "y":
		print "Dice: %d" % randint(min, max)
	else:
		count_down()

def two_craps():
	"""Rolls two "dices"."""
	print "Ready to roll? yes/no"
	roll = raw_input()
	if roll == "y":
		print "You got:"
		print "Dice one: %d" % randint(min, max)
		print "Dice two: %d" % randint(min, max)
	else:
		count_down()	

def three_craps():
	"""Three dices."""
	print "Ready to roll? yes/no"
	roll = raw_input()
	if roll == "y":
		print "Dice one: %d" % randint(min, max)
		print "Dice two: %d" % randint(min, max)
		print "Dice three: %d" % randint(min, max)
	else:
		count_down()	

