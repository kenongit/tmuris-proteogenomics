#!/usr/bin/python

import sys

in_file = open(sys.argv[1], 'r')

for line in in_file:
	columns = line.strip().split('\t')
	if 'ms2:l3_aug' in line:
		print columns[0][1:]


