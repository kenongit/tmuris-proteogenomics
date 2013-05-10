#!/usr/bin/python
# Filter an NCBI BLAST+ output file (using flag '-outfmt 7') according to a number of scoring metrics
# > Generate a query coverage value for each hit
# > Preserve only the specified number of best hits per query (ranked by e-value)
# > Filter remaining hits by any combination of length, % identity and e-value
# > Beware of header line included in output
# USAGE: filter_blast_output.py -h
# EG: filter_blast_output.py -n 1 -e 1e-30 -l 150 -i 90 adult.best_candidates-uniref90.blastp.merged.out 

from __future__ import division
import argparse

# Handle args
parser = argparse.ArgumentParser()
parser.add_argument('blast_file', help='BLAST output file to process')
parser.add_argument('-n', '--max_hits_per_query', type=int, help='number of best hits per query to keep')
parser.add_argument('-e', '--max_hit_evalue', type=float, help='upper evalue limit')
parser.add_argument('-l', '--min_hit_length', type=int, help='lower alignment length limit')
parser.add_argument('-i', '--min_hit_identity', type=int, help='lower percent identity limit')
args = parser.parse_args()

in_file = open(args.blast_file, 'r')

# Declare state vars 
cur_query_length = 0
cur_hit_number = 0

# Print header line
# print 'Fields: query id, subject id, % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score, hit number'

for line in in_file:
	if line.startswith('# Query'):
		cur_hit_number = 0
	elif not line.startswith('#'):
		if int(cur_hit_number) < args.max_hits_per_query or not args.max_hits_per_query:
			cur_hit_number += 1
			hit = line.strip().split('\t')
			hit_identity = float(hit[2])
			hit_length = int(hit[3])
			hit_evalue = float(hit[10])
			if ((args.max_hit_evalue is None or hit_evalue < args.max_hit_evalue) and
				(args.min_hit_length is None or hit_length > args.min_hit_length) and
				(args.min_hit_identity is None or hit_identity > args.min_hit_identity)):
				print '	'.join(hit) + '\t' + str(cur_hit_number)

in_file.close()

