#!/usr/bin/env python
"""mapper.py for question 1"""

import sys

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
		if not line[CARRIER] or not line[ARRDELAY]:
			continue
		print("%s\t%s" % (line[CARRIER], line[ARRDELAY]))

if __name__ == "__main__":
	mapper()
