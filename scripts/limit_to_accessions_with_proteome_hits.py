#!/usr/bin/python

import sys

in_file = open(sys.argv[1], 'r')

for line in in_file:
	line = line.strip().split('\t')
	if len(line) == 5:
		print '\t'.join(line)
