#!/usr/bin/env python
"""reducer.py for question 2.2
For each source-destination pair X-Y, rank the top-10 carriers 
in decreasing order of on-time arrival performance at Y from X.
"""

import sys

def reducer():

	curr_origin = None
	curr_dest = None
	curr_date = None
	curr_am_pm = None
	curr_carrier = None 
	curr_num = None 
	curr_time = None
	curr_delay = None

	for line in sys.stdin:
		origin, dest, date, am_pm, carrier, flight_num, time, delay = line.strip().split("\t")

		try:
			delay = float(delay)
		except ValueError:
			continue
		# same key
		if curr_origin == origin and curr_dest == dest and curr_date == date and curr_am_pm == am_pm:
			if delay < curr_delay:
				curr_delay = delay
				curr_carrier = carrier
				curr_num = flight_num 
				curr_time = time
		# different key
		else:
			if curr_origin and curr_dest and curr_date and curr_am_pm:
				print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%.2f" % (
					  curr_origin, curr_dest, curr_date, 
					  curr_am_pm, curr_carrier, curr_num,
					  curr_time, curr_delay)) 
			curr_origin = origin
			curr_dest = dest
			curr_date = date 
			curr_am_pm = am_pm 
			curr_carrier = carrier
			curr_num = flight_num
			curr_time = time
			curr_delay = delay 
	# last OD
	if curr_origin == origin and curr_dest == dest and curr_date == date and curr_am_pm == am_pm:
		print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%.2f" % (
			  curr_origin, curr_dest, curr_date, 
			  curr_am_pm, curr_carrier, curr_num,
			  curr_time, curr_delay)) 

if __name__ == "__main__":
	reducer()
		