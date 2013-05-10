#!/usr/bin/python
# Append to a fasta header if the accession ID (immediately following '>') exists in the first column of a second file 
# EG: add_filtered_proteomics_hits_to_fasta_header.py genes_2012-10-12.prot.fasta augustus.L2.aggregated \|proteomics_hit:L2\|
# /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/hons-project-tmuris/scripts/add_filtered_proteomics_hits_to_fasta_header.py /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/dna/genes_2012-10-12.prot.blastxhits.L2.fasta /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/mascot/2013/dat/aggregated/augustus.L3.aggregated \|proteomics_hit:L3 > /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/dna/genes_2012-10-12.prot.blastxhits.L2L3.fasta

import sys

fasta_src = open(sys.argv[1], 'r')
hit_src = open(sys.argv[2], 'r')
hit_string = sys.argv[3]

hit_genes = []

for line in hit_src:
	hit_genes.append(line.split('\t')[0])

for line in fasta_src:
	if line.startswith('>') and line.strip().split('|')[0][1:] in hit_genes:
		print line.strip() + hit_string
	else:
		print line.strip()
		




