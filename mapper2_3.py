#!/usr/bin/env python
"""mapper.py for question 2.2
For each source-destination pair X-Y, rank the top-10 carriers
in decreasing order of on-time arrival performance at Y from X.
"""

import sys

ORIGIN_AIRPORT = 11
DESTINATION_AIRPORT = 18
CARRIER = 8
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
		if not line[CARRIER] or not line[ARRDELAY]:
			continue
		print("%s\t%s\t%s\t%s" % (
		      line[ORIGIN_AIRPORT], line[DESTINATION_AIRPORT],
			  line[CARRIER], line[ARRDELAY]))

if __name__ == "__main__":
	mapper()
