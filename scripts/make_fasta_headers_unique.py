#!/usr/bin/python
# Adds identifier to fasta header lines
# Accept files as command line arguments. Creates new .out file.

import sys

# Change as desired
identifier = 'frear'
identifier_prefix = 'FRE'

# Iterate through command line arguments
for n in sys.argv[1:]:
	print(n) + ' > ' + n + '.out'
	in_file = open(n, "r")
	out_file = open(n + ".out", "w")
	
	for line in in_file:
		if line.startswith('>'):
			header = '>' + identifier_prefix + line[1:].rstrip("\n\r") + ' ~' + identifier + '\n'
			out_file.write(header)
		else:
			out_file.write(line)

	in_file.close()
	out_file.close()