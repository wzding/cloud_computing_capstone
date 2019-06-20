#!/usr/bin/env python

import sys

res = {}

def reducer():
	for line in sys.stdin:
		carrier, delay = line.strip().split("\t")

		try:
			delay = float(delay)
		except ValueError:
			continue

		if carrier in res:
			res[carrier].append(delay)
		else:
			res[carrier] = [delay]


if __name__ == "__main__":
	reducer()
	for carrier in res:
		avg_delay = sum(res[carrier]) / len(res[carrier])
		print("%s\t%s" % (carrier, avg_delay))