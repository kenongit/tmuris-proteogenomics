#!/usr/bin/python
# Grab Uniref90 ID from second tab separated and pipe separated column and add name/taxa to end of header line

import sys

source_file = open(sys.argv[1], 'r')
lookup_table_file = open(sys.argv[2], 'r')

accessions = {}

for line in lookup_table_file:
	line = line.strip().split('~')
	accession = line[0]
	accessions[accession] = {'hit_accession':line[0], 'hit_name':line[1], 'hit_tax':line[2]}

for line in source_file:
		if line.split('\t')[2].split('|')[0] in accessions:
			this_accession = line.split('\t')[2].split('|')[0]
			print line.strip() + '\t' + this_accession + '|' + accessions[this_accession]['hit_name'] + '|' + accessions[this_accession]['hit_tax']
		else:
			print line.strip() + '\t' + '<none>'