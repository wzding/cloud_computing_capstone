#!/usr/bin/env python
"""reducer.py for question 1.2"""

import sys

def reducer():

	curr_carrier = None
	total_delay = 0
	count = 0

	for line in sys.stdin:
		carrier, delay = line.strip().split("\t")

		try:
			delay = float(delay)
		except ValueError:
			continue

		if curr_carrier == carrier:
			total_delay += delay 
			count += 1
		else:
			if curr_carrier:
				print("%s\t%.2f" % (curr_carrier, total_delay * 1.0/ count)) 
			curr_carrier = carrier 
			total_delay = delay
			count = 1
	# last carrier
	if curr_carrier == carrier:
		print("%s\t%.2f" % (carrier, total_delay * 1.0/ count)) 



if __name__ == "__main__":
	reducer()
		