#!/usr/bin/python
# Pull accessions from fasta file
# Removes first '>' and ignores anything after a space char 
import sys

in_file = open(sys.argv[1], 'r')

for line in in_file:
	if line.startswith('>'):
		print line[1:].strip().split(' ')[0]