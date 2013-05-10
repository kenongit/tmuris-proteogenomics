#!/usr/bin/python
# Throw away proteins with less than two unique PSMs
# Input row format: protein_accession	psm_peptide	number_of_psms
# Output row format: protein_accession	psm_peptide	number_of_psms number_of_unique_psms
import sys

n_required_unique_psms = 2

proteins = {}

in_file = open(sys.argv[1], 'r')

for line in in_file:
	line = line.split('	')
	protein = line[0]
	psms = line[1].split(',')
	if protein not in proteins:
		proteins[protein] = []
	for psm in psms:
		proteins[protein].append(psm)

in_file.close()

for protein, psms in proteins.iteritems():
	if len(set(proteins[protein])) >= 2:
		print protein + '\t' + ','.join(psms) + '\t' + str(len(psms)) + '\t' + str(len(set(psms)))