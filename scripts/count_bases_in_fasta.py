#!/usr/bin/python
# Count bases in fasta file. Account for single char newlines

import sys

in_file = open(sys.argv[1], 'r')

running_total = 0

for line in in_file:
	if not line.startswith('>'):
		line_total = len(line) - 1
		running_total += line_total

print running_total