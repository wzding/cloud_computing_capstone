#!/usr/bin/env python
"""mapper.py for question 2.1
For each airport X, rank the top-10 carriers in decreasing order of on-time departure performance from X.
"""

import sys

ORIGIN_AIRPORT = 11
DESTINATION_AIRPORT = 18
DEPDELAY = 27

def mapper():
	for line in sys.stdin:
		try:
			line = line.replace('"', '').split(",")
		except ValueError:
			continue
		if len(line) < 78:
			continue
		if len(line[ORIGIN_AIRPORT]) != 3 or len(line[DESTINATION_AIRPORT]) != 3:
			continue
		if not line[DEPDELAY]:
			continue

		print("{}\t{}\t{}"\
		      .format(line[ORIGIN_AIRPORT], line[DESTINATION_AIRPORT], line[DEPDELAY]))

if __name__ == "__main__":
	mapper()
