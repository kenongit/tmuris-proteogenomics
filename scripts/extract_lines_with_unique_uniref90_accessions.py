#!/usr/bin/python
# Revised, now prints lowest evalue hit for a distinct UniRef accession
# Also gives preferential treatment to proteins with MS/MS (ms2) hits
# Therefore no longer works line by line...

import sys

in_file = open(sys.argv[1], 'r')

accessions = {}

for line in in_file:
	columns = line.strip().split('\t')
	if len(columns[2].split('|')) == 4:
		accession = columns[2].split('|')[0]

		if accession in accessions and 'ms2:' in accessions[accession]['line']:
				ms2_ok = True if 'ms2:' in line else False

		if accession not in accessions or (float(columns[2].split('|')[3][5:]) < float(accessions[accession]['evalue']) and ms2_ok):
			accessions[accession] = { 'evalue':columns[2].split('|')[3][5:], 'line':line.strip() }

for this_accession in accessions:
	print accessions[this_accession]['line']

# accessions = []

# for line in in_file:
# 	columns = line.strip().split('\t')
# 	if len(columns[2].split('|')) == 4:
# 		accession = columns[2].split('|')[0]
# 		if accession not in accessions:
# 			accessions.append(accession)
# 			print line.strip()
