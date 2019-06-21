#!/usr/bin/env python
"""mapper.py for question 1"""

import sys

ORIGIN_AIRPORT = 11
CARRIER = 8
DEPDELAY = 27

def mapper():
	for line in sys.stdin:
		try:
			line = line.replace('"', '').split(",")
		except ValueError:
			continue
		if len(line) < 78:
			continue
		if len(line[ORIGIN_AIRPORT]) != 3:
			continue
		if not line[CARRIER] or not line[DEPDELAY]:
			continue

		print("{}\t{}\t{}"\
		      .format(line[ORIGIN_AIRPORT], line[CARRIER], line[DEPDELAY]))

if __name__ == "__main__":
	mapper()
