#!/usr/bin/env python
"""mapper.py for question 2.2
For each source-destination pair X-Y, rank the top-10 carriers
in decreasing order of on-time arrival performance at Y from X.
"""

import sys

ORIGIN_AIRPORT = 11
DESTINATION_AIRPORT = 18
DEPDATE = 5
DEPTIME = 25
CARRIER = 8
FLIGHTNUM = 10
ARRDELAY = 38

def mapper():
	for line in sys.stdin:
		try:
			line = line.replace('"', '').split(",")
		except ValueError:
			continue
		if len(line) < 78:
			continue
		if len(line[ORIGIN_AIRPORT]) < 3 or len(line[DESTINATION_AIRPORT]) < 3:
			continue
		if not line[DEPDATE] or line[DEPDATE][:4] != '1988' or not line[DEPTIME]:
			continue
		if not line[CARRIER] or not line[FLIGHTNUM] or not line[ARRDELAY]:
			continue

		if int(line[DEPTIME][:-2]) < 12:
			am_pm = 'AM'
		else:
			am_pm = 'PM'

		print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (
		      line[ORIGIN_AIRPORT], line[DESTINATION_AIRPORT],
			  line[DEPDATE], am_pm,
			  line[CARRIER], line[FLIGHTNUM],
			  line[DEPTIME], line[ARRDELAY]))

if __name__ == "__main__":
	mapper()
