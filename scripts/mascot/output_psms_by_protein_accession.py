#!/usr/bin/python
# Generate list of potential candidate proteins with comma separated supporting PSMs for each
# Accepts five column output from output_scored_psms.py
# Outputs format: protein accession, matched peptides (comma delimited)
# USAGE: output_psms_by_protein_accession.py <scored_psm_file>

import sys

proteins = {}

in_file = open(sys.argv[1], "r")

for line in in_file:
	line = line.split('	')
	psm = line[0]
	psm_candidate_proteins = line[4].replace(',\n', '').split(',')

	for protein in psm_candidate_proteins:
		if protein not in proteins: 
			proteins[protein] = []
		proteins[protein].append(psm)

in_file.close()

# Output protein accessions with their corresponding PSMs
for protein, psms in proteins.iteritems():
	print protein + '\t' + ','.join(psms) + '\t' + str(len(psms))