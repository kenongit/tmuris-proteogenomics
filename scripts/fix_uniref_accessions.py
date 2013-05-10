#!/usr/bin/python

import sys

hit_src = open(sys.argv[1], 'r')
lookup_table_src = open(sys.argv[2], 'r')

accessions = {}

# Load lookup table in memory
for line in lookup_table_src:
	line = line.strip().split('~')
	accession = line[0]
	accessions[accession] = {'hit_accession':line[0], 'hit_name':line[1], 'hit_tax':line[2]}

# Get BLAST search info
for line in hit_src:
	this_accession = line.split('\t')[2].split('|')[0]
	if this_accession in accessions:
		line = line.strip().split('\t')
		new_line = (line[0] + '\t' + line[1] + '\t' + line[2] + '\t' + this_accession + '|'
			+ accessions[this_accession]['hit_name'] + '|' + accessions[this_accession]['hit_tax'])
		if len(line) == 5:
			new_line += '\t' + line[4]
		print new_line