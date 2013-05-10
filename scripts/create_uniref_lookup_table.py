#!/usr/bin/python
# Create lookup table of UniRef/UniProt accession ID vs protein name
# Accepts UniRef50/90/100 fasta file as input, creates comma separated three column output
# Works on fasta headers that are like the one below:
# >UniRef90_Q6GZV5 Uncharacterized protein 020R n=8 Tax=Ranavirus RepID=020R_FRG3G

import sys

in_file = open(sys.argv[1], 'r')

for line in in_file:
	if line.startswith('>'):
		line = line.strip()
		protein_id = line.split(' ')[0][1:]
		protein_name = line.split(' n=')[0].split(' ', 1)[1]
		protein_tax = line.split('Tax=')[1].split(' RepID=')[0]
		print protein_id + '~' + protein_name + '~' + protein_tax