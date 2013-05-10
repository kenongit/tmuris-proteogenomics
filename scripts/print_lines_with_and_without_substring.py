#!/usr/bin/python

import sys

in_file = open(sys.argv[1], 'r')
with_string = sys.argv[2]
without_string = sys.argv[3]

for line in in_file:
	if (with_string in line) and (without_string not in line):
		print line.strip()