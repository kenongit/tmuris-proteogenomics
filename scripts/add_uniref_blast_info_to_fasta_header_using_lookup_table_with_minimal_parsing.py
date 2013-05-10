#!/usr/bin/python

import sys

hit_src = open(sys.argv[1], 'r')
lookup_table_src = open(sys.argv[2], 'r')

accessions = {}

# Load lookup table in memory
for line in lookup_table_src:
	line = line.strip().split(',')
	accession = line[0]
	accessions[accession] = {'hit_accession':line[0], 'hit_name':line[1], 'hit_tax':line[2]}

# Get BLAST search info
for line in hit_src:
	if line.split('\t')[1] in accessions:
		this_accession = line.split('\t')[1]
		print line.strip() + '\t' + this_accession + '|' + accessions[this_accession]['hit_name'] + '|' + accessions[this_accession]['hit_tax']