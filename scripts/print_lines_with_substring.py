#!/usr/bin/python

import sys

in_file = open(sys.argv[1], 'r')
string = sys.argv[2]

for line in in_file:
	if string in line:
		print line.strip()