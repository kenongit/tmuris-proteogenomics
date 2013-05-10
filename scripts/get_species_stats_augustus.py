#!/usr/bin/python

import sys

in_file = open(sys.argv[1], 'r')

taxa_counts = {}
for line in in_file:
	if line.startswith('>'):
		if len(line.strip().split('\t')[4].split('|')) == 3:
			taxa = line.strip().split('\t')[4].split('|')[2]
			if taxa not in taxa_counts:
				taxa_counts[taxa] = 1
			else:
				taxa_counts[taxa] += 1
for taxa in taxa_counts:
	print taxa + ',' + str(taxa_counts[taxa])