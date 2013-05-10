#!/usr/bin/python
# Merge files containing lists of protein names and their corresponding PSMs
# USAGE: merge_psms_by_protein.py <psm_files>
# EG ./merge_psms_by_protein.py dat/parsed/*adult*sorted | sort -rnk 3 -t '	'  > adult_rna.merged.psm.txt

import sys

proteins = {}

for file_name in sys.argv[1:]:

	dat_file = open(file_name, 'r')
	
	for line in dat_file:
		line = line.split('	')
		protein = line[0]
		psms = line[1].split(',')
		
		if protein not in proteins:
			proteins[protein] = []

		for psm in psms:
			proteins[protein].append(psm)
	
	dat_file.close()

# Output protein accessions with their corresponding PSMs
for protein, psms in proteins.iteritems():
	print protein + '\t' + ','.join(psms) + '\t' + str(len(psms))