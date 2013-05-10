#!/usr/bin/python

import sys

source_file = open(sys.argv[1])
proteomics_file = open(sys.argv[2])
proteomics_identifier = sys.argv[3]

accessions = {}

for line in proteomics_file:
	line = line.strip().split('\t')
	accession_proteomics = line[0]
	accessions[accession_proteomics] = {'psm':line[2], 'psm_unique':line[3]}

for line in source_file:
	accession_source = line.strip().split('\t')[0]
	if accession_source in accessions:
		if line.strip().split('\t')[-1] == '<none>':
			new_line = ('\t'.join(line.strip().split('\t')[:-1]) + '\t' + 'ms2:'
				+ proteomics_identifier + '|psm:' +  accessions[accession_source]['psm']
				+ '|psm_uniq:' + accessions[accession_source]['psm_unique'])
			print new_line
		else:
			new_line = (line.strip() + '|ms2:'
			+ proteomics_identifier + '|psm:' +  accessions[accession_source]['psm']
			+ '|psm_uniq:' + accessions[accession_source]['psm_unique'])
			print new_line
	else:
		print line.strip()