#!/usr/bin/python

import sys

in_file = open(sys.argv[1], 'r')
string = sys.argv[2]
second_string = sys.argv[3]

for line in in_file:
	if string in line or second_string in line:
		print line.strip()