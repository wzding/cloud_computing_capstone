#!/usr/bin/env python
"""reducer.py for question 2.1
For each airport X, rank the top-10 carriers in decreasing order of on-time departure performance from X.
"""

import sys

def reducer():

	curr_origin = None
	curr_dest = None
	total_delay = 0
	count = 0

	for line in sys.stdin:
		origin, dest, delay = line.strip().split("\t")

		try:
			delay = float(delay)
		except ValueError:
			continue
		# same airport and same carrier
		if curr_origin == origin and curr_dest == dest:
			total_delay += delay 
			count += 1
		# different carrier or diff aprt
		else:
			if curr_origin and curr_dest:
				print("%s\t%s\t%.2f" % (
				      curr_origin, curr_dest, total_delay * 1.0/ count)) 
			curr_origin = origin
			curr_dest = dest
			total_delay = delay 
			count = 1
	# last aprt and carrier
	if curr_origin == origin and curr_dest == dest:
		print("%s\t%s\t%.2f" % (
			  curr_origin, curr_dest, total_delay * 1.0/ count)) 

if __name__ == "__main__":
	reducer()
		