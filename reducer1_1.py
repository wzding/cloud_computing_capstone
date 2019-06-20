#!/usr/bin/env python

import sys

def reducer():

	curr_aprt = None
	curr_count = 0
	aprt = None
	for line in sys.stdin:
		aprt, count = line.strip().split("\t")

		try:
			count = int(count)
		except ValueError:
			continue
		# same airport 
		if curr_aprt == aprt:
			curr_count += count
		else: # different airport
			if curr_aprt:
				print("{}\t{}".format(curr_aprt, curr_count))
			curr_count = count
			curr_aprt = aprt
	# last airport
	if curr_aprt == aprt:
		print("{}\t{}".format(curr_aprt, curr_count))


if __name__ == "__main__":
	reducer()