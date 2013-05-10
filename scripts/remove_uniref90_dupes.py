#!/usr/bin/python

import sys

in_file = open(sys.argv[1], 'r')

accessions = []
for line in in_file:
	line = line.strip().split('\t')
	if line[2].split('|')[0] not in accessions:
		accessions.append(line[2].split('|')[0])
		print '\t'.join(line)
