#!/usr/bin/python

import sys

in_file = open(sys.argv[1], 'r')

for line in in_file:
	columns = line.strip().split('\t')
	if len(columns[2].split('|')) == 4:
		if float(columns[2].split('|')[3][5:]) < 1e-30:
		#if float(columns[2].split('|')[1][4:]) > 50 and float(columns[2].split('|')[3][5:]) < 1e-30:
			print line.strip()
			