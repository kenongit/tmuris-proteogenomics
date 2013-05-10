#!/usr/bin/python
# Add Uniref hit info, change column structure

import sys

hit_src = open(sys.argv[1], 'r')
lookup_table_src = open(sys.argv[2], 'r')

accessions = {}

for line in lookup_table_src:
	line = line.strip().split(',')
	accession = line[0]
	accessions[accession] = {'hit_accession':line[0], 'hit_name':line[1], 'hit_tax':line[2]}

for line in hit_src:
	if line.split('\t')[1] in accessions:
		line = line.strip().split('\t')
		this_accession = line[1]
		# One hit
		if 14 == len(line):
			print (line[0] + '\t' + line[1] + '\t' + '%id:' + line[2] + '|len:' + line[3] + '|mis:'
			+ line[4] + '|go:' + line[5] + '|qs:' + line[6] + '|qe:' + line[7] + '|ss:' + line[8]
			+ '|se:' + line[9] + '|ev:' + line[10] + '|bs:' + line[11].strip(' ')
			+ '\t' + accessions[this_accession]['hit_accession'] + '|' + accessions[this_accession]['hit_name'] + '|'
			+ accessions[this_accession]['hit_tax'] + '\t' + line[13])
		elif 15 == len(line):
			print (line[0] + '\t' + line[1] + '\t' + '%id:' + line[2] + '|len:' + line[3] + '|mis:'
			+ line[4] + '|go:' + line[5] + '|qs:' + line[6] + '|qe:' + line[7] + '|ss:' + line[8]
			+ '|se:' + line[9] + '|ev:' + line[10] + '|bs:' + line[11].strip(' ')
			+ '\t' + accessions[this_accession]['hit_accession'] + '|' + accessions[this_accession]['hit_name'] + '|'
			+ accessions[this_accession]['hit_tax'] + '\t' + line[13] + ',' + line[14])
		else:
			print (line[0] + '\t' + line[1] + '\t' + '%id:' + line[2] + '|len:' + line[3] + '|mis:'
				+ line[4] + '|go:' + line[5] + '|qs:' + line[6] + '|qe:' + line[7] + '|ss:' + line[8]
				+ '|se:' + line[9] + '|ev:' + line[10] + '|bs:' + line[11].strip(' ')
				+ '\t' + accessions[this_accession]['hit_accession'] + '|' + accessions[this_accession]['hit_name'] + '|'
				+ accessions[this_accession]['hit_tax'])

