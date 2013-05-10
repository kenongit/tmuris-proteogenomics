#!/usr/bin/python
# Filter an NCBI BLAST+ output file (using flag '-outfmt 7') according to a number of scoring metrics
# > Generate a query coverage value for each hit
# > Preserve only the specified number of best hits per query (ranked by e-value)
# > Filter remaining hits by any combination of length, % identity, e-value and % query coverage
# > Beware of header line included in output
# USAGE: filter_blast_output.py -h
# EG: filter_blast_output.py -n 1 -e 1e-30 -l 150 -i 90 -c 50 adult.best_candidates-uniref90.blastp.merged.out

from __future__ import division
import argparse

# Handle args
parser = argparse.ArgumentParser()
parser.add_argument('blast_file', help='BLAST output file to process')
parser.add_argument('-n', '--max_hits_per_query', type=int, help='number of best hits per query to keep')
parser.add_argument('-e', '--max_hit_evalue', type=float, help='upper evalue limit')
parser.add_argument('-l', '--min_hit_length', type=int, help='lower alignment length limit')
parser.add_argument('-i', '--min_hit_identity', type=int, help='lower percent identity limit')
parser.add_argument('-c', '--min_hit_query_coverage', type=int, help='lower percent query coverage limit')
args = parser.parse_args()

in_file = open(args.blast_file, 'r')

# Declare state vars 
cur_query_length = 0
cur_hit_number = 0

# Print header line
# print 'Fields: query id, subject id, % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score, % query coverage, hit number'

for line in in_file:
	if line.startswith('# Query'):
		query = line.strip().split(' ')
		cur_query_length = int(''.join(i for i in query[3] if i.isdigit())) # Ugly but functional
		cur_hit_number = 0
	elif not line.startswith('#'):
		if int(cur_hit_number) < args.max_hits_per_query or not args.max_hits_per_query:
			cur_hit_number += 1
			hit = line.strip().split('\t')
			query_start = int(hit[6])
			query_end = int(hit[7])
			hit_query_coverage = abs(float(((query_end * 3) - (query_start * 3) + 1) / cur_query_length)) * 100
			hit_identity = float(hit[2])
			hit_length = int(hit[3])
			hit_evalue = float(hit[10])
			if ((args.max_hit_evalue is None or hit_evalue < args.max_hit_evalue) and
				(args.min_hit_length is None or hit_length > args.min_hit_length) and
				(args.min_hit_identity is None or hit_identity > args.min_hit_identity) and
				(args.min_hit_query_coverage is None or float(hit_query_coverage) > args.min_hit_query_coverage)):
				print '	'.join(hit) + '\t' + str("{0:.3f}".format(hit_query_coverage)) + '\t' + str(cur_hit_number)

in_file.close()

