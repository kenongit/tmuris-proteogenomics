#!/usr/bin/python
# Add relevant BLASTP hit information to fasta header lines
# Accepts NCBI BLASTP output created using flag '-outfmt 7'
# Uses a three-column comma delimited lookup table to get full protein names and taxa from a UniRef accession
# Adds first occurence of accession in BLAST output file, which is the highest ranked alignment
# USAGE: add_uniref_blast_info_to_fasta_header_using_lookup_table.py <fasta_file> <blast_output> <lookup_table>
# WARNING: Lookup tables with >1m rows will take hours to process

import sys

fasta_src = open(sys.argv[1], 'r')
blast_src = open(sys.argv[2], 'r')
lookup_table_src = open(sys.argv[3], 'r')
accessions = {}

# Get BLAST search info
for line in blast_src:
	if not line.startswith('#'):
		line = line.strip().split('\t')
		accession = line[0]
		if accession not in accessions:
			accessions[accession] = {}
			accessions[accession]['hit_accession'] = line[1]
			accessions[accession]['hit_identity'] = line[2]
			accessions[accession]['hit_length'] = line[3]
			accessions[accession]['hit_evalue'] = line[10]

# Retrieve full protein names from lookup table
for line in lookup_table_src:
	line = line.strip().split(',')
	for accession in accessions:
		if accessions[accession]['hit_accession'] == line[0]:
			accessions[accession]['hit_name'] = line[1]
			accessions[accession]['hit_tax'] = line[2]

# Add BLAST info to fasta headers
for line in fasta_src:
	if line.startswith('>'):
		accession = line.strip()[1:]
		if accession in accessions:
			if 'hit_name' in accessions[accession]:
				print( '>' + accession + '|accession:' + accessions[accession]['hit_accession']
					+ '|name:' + accessions[accession]['hit_name']
					+ '|tax:' + accessions[accession]['hit_tax']
					+ '|evalue:' + accessions[accession]['hit_evalue']
					+ '|%identity:' + accessions[accession]['hit_identity']
					+ '|length:' + accessions[accession]['hit_length'])
			else:
				print( '>' + accession + '|accession:' + accessions[accession]['hit_accession']
					+ '|evalue:' + accessions[accession]['hit_evalue']
					+ '|%identity:' + accessions[accession]['hit_identity']
					+ '|length:' + accessions[accession]['hit_length'])
	else:
		print line.strip()



