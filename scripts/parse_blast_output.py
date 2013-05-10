#!/usr/bin/python
# Parse the top hit for each query of an NCBI BLAST output file created with '-outfmt 7'

import sys

def build_data_structure_from_blast_output(blast_output_file):
	blast_file = open(blast_output_file, 'r')
	blast_top_hits = {}
	for line in blast_file:
		if not line.startswith('#'):
			line = line.strip().split('\t')
			if line[0] not in blast_top_hits or float(line[10]) < float(blast_top_hits[line[0]]['evalue']):
				blast_top_hits[line[0]] = {
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
	return blast_top_hits

print build_data_structure_from_blast_output(sys.argv[1])