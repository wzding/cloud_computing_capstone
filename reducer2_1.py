#!/usr/bin/env python
"""reducer.py for question 2.1
For each airport X, rank the top-10 carriers in decreasing order of on-time departure performance from X.
"""

import sys

def reducer():

	curr_aprt = None
	curr_carrier = None
	total_delay = 0
	count = 0

	for line in sys.stdin:
		aprt, carrier, delay = line.strip().split("\t")

		try:
			delay = float(delay)
		except ValueError:
			continue
		# same airport and same carrier
		if curr_aprt == aprt and curr_carrier == carrier:
			total_delay += delay 
			count += 1
		# different carrier or diff aprt
		else:
			if curr_aprt and curr_carrier:
				print("%s\t%s\t%.2f" % (
				      curr_aprt, curr_carrier, total_delay * 1.0/ count)) 
			curr_aprt = aprt
			curr_carrier = carrier
			total_delay = delay 
			count = 1
	# last aprt and carrier
	if curr_aprt == aprt and curr_carrier == carrier:
		print("%s\t%s\t%.2f" % (
			  curr_aprt, curr_carrier, total_delay * 1.0/ count)) 

if __name__ == "__main__":
	reducer()
		