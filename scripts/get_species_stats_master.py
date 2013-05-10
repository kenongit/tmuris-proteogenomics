#!/usr/bin/python
import sys

in_file = open(sys.argv[1], 'r')
out_file = open(sys.argv[1] + '.taxa.csv', 'w+')

taxa_counts = {}
for line in in_file:
	if len(line.strip().split('\t')[5].split('|')) == 3:
		taxa = line.strip().split('\t')[5].split('|')[2]
		if taxa not in taxa_counts:
			taxa_counts[taxa] = 1
		else:
			taxa_counts[taxa] += 1
for taxa in taxa_counts:
	out_file.write(taxa + ',' + str(taxa_counts[taxa]) + '\n')