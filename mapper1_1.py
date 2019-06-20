#!/usr/bin/env python
"""mapper.py for question 1"""

import sys

ORIGIN_AIRPORT = 11
DESTINATION_AIRPORT = 18

def mapper():
	for line in sys.stdin:
		try:
			line = line.replace('"', '').split(",")
		except ValueError:
			continue
		if len(line) < 58:
			continue
		if len(line[ORIGIN_AIRPORT]) != 3 or len(line[DESTINATION_AIRPORT]) != 3:
			continue
		
		print("{}\t1".format(line[ORIGIN_AIRPORT]))
		print("{}\t1".format(line[DESTINATION_AIRPORT]))

if __name__ == "__main__":
	mapper()
