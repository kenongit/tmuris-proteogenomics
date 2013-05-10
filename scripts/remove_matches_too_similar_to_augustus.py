#!/usr/bin/python

import sys

in_file = open(sys.argv[1], 'r')

for line in in_file:
	line = line.strip().split('\t')
	if float(line[1].split('|')[1][4:]) >= 90 and float(line[1].split('|')[3][3:]) <= 1e-30:
		pass
	else:
		print '\t'.join(line)
