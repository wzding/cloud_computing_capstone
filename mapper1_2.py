#!/usr/bin/env python
"""mapper.py for question 1"""

import sys

Carrier = 8
ArrDelay = 38

def mapper():
	for line in sys.stdin:
		try:
			line = line.replace('"', '').split(",")
		except ValueError:
			continue
		if len(line) < 78:
			continue
		if not line[Carrier] or not line[ArrDelay]:
			continue
		print("%s\t%s" % (line[Carrier], line[ArrDelay]))

if __name__ == "__main__":
	mapper()
