#!/usr/bin/env python
"""reducer.py for question 2.2
For each source-destination pair X-Y, rank the top-10 carriers 
in decreasing order of on-time arrival performance at Y from X.
"""

import sys

def reducer():

	curr_origin = None
	curr_dest = None
	curr_carrier = None
	total_delay = 0
	count = 0

	for line in sys.stdin:
		origin, dest, carrier, delay = line.strip().split("\t")

		try:
			delay = float(delay)
		except ValueError:
			continue
		# same origin, dest and carrier
		if curr_origin == origin and curr_dest == dest and curr_carrier == carrier:
			total_delay += delay 
			count += 1
		# different origin, dest or carrier
		else:
			if curr_origin and curr_dest and curr_carrier:
				print("%s\t%s\t%s\t%.2f" % (
				      curr_origin, curr_dest, curr_carrier, total_delay * 1.0/ count)) 
			curr_origin = origin
			curr_dest = dest
			curr_carrier = carrier
			total_delay = delay 
			count = 1
	# last OD
	if curr_origin == origin and curr_dest == dest and curr_carrier == carrier:
		print("%s\t%s\t%s\t%.2f" % (
			  curr_origin, curr_dest, curr_carrier, total_delay * 1.0/ count)) 

if __name__ == "__main__":
	reducer()
		