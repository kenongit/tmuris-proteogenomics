#!/usr/bin/python

import sys

source_file = open(sys.argv[1])
proteomics_file = open(sys.argv[2])
proteomics_identifier = sys.argv[3]

accessions = {}

for line in proteomics_file:
	line = line.strip().split('\t')
	accession = line[0]
	accessions[accession] = {'psm':line[2], 'psm_unique':line[3]}

for line in source_file:
	if line.startswith('>'):
		accession = line.strip().split('\t')[0][1:]
		if accession in accessions:
			print (line.strip() + '\t' + 'ms2:'
				+ proteomics_identifier + '|psm:' +  accessions[accession]['psm']
				+ '|psm_uniq:' + accessions[accession]['psm_unique'])
		else:
			print line.strip() + '\t' + '<none>'
	else:
		print line.strip()