#!/usr/bin/python
# Add the Best Augustus BLAST hit of every first column accession from a parsed blastx output file

import sys

def build_data_structure_from_blast_output(blast_output_file):
	blast_file = open(blast_output_file, 'r')
	blast_queries = {}
	for line in blast_file:
		if not line.startswith('#'):
			line = line.strip().split('\t')
			if line[0] not in blast_queries:
				blast_queries[line[0]] = {
					'subject':line[1],
					'identity':line[2],
					'length':line[3],
					'mismatches':line[4],
					'gap_opens':line[5],
					'query_start':line[6],
					'query_end':line[7],
					'subject_start':line[8],
					'subject_end':line[9],
					'evalue':line[10],
					'bit_score':line[11]
				}
	return blast_queries

blast_results = build_data_structure_from_blast_output(sys.argv[1])

source_file = open(sys.argv[2], 'r')

for line in source_file:
	line = line.strip().split('\t')
	if line[0] in blast_results:
		new_line = (line[0] + '\t' + blast_results[line[0]]['subject'] + '|%id:'
			+ blast_results[line[0]]['identity'] + '|len:'
			+ blast_results[line[0]]['length'] + '|ev:'
			+ blast_results[line[0]]['evalue'] + '\t'
			+ line[1] + '|' + line[2] + '\t' + line[3])
		if len(line) == 4:
			print new_line
		elif len(line) == 5:
			print new_line + '\t' + line[4]