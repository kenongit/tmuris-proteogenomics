#!/usr/bin/python

import sys

in_file = open(sys.argv[1], 'r')

for line in in_file:
	columns = line.strip().split('\t')
	if len(columns[1].split('|')) == 4 and float(columns[1].split('|')[1][4:]) >= 90 and float(columns[1].split('|')[3][5:]) <= 1e-30:
		pass
	else:
		print line.strip()


