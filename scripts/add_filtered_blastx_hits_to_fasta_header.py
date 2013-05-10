#!/usr/bin/python
# Append filtered Trinity blastx hit info to Augustus header lines
# ./add_filtered_blastx_hits_to_fasta_header.py /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/dna/genes_2012-10-12.prot.fasta  /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/blastx_aug_trin/filtered/rna.combined.aug_trinity.unique_augustus_but_not_by_best_hit.blastx.out.filtered

import sys

fasta_src = open(sys.argv[1], 'r')
hit_src = open(sys.argv[2], 'r')

accessions = {}

for line in hit_src:
	line = line.strip().split('\t')
	accession = line[0]
	if accession not in accessions:
		accessions[accession] = {}
		accessions[accession]['hit_accession'] = line[1]
		accessions[accession]['hit_identity'] = line[2]
		accessions[accession]['hit_length'] = line[3]
		accessions[accession]['hit_evalue'] = line[10]

for line in fasta_src:
	if line.startswith('>') and line.strip().split('|')[0][1:] in accessions:
		print (line.strip() + '|blastx_trin_acc:' + accessions[line.strip()[1:]]['hit_accession']
			+ '|trin_eval:' + accessions[line.strip()[1:]]['hit_evalue']
			+ '|trin_%id:' + accessions[line.strip()[1:]]['hit_identity']
			+ '|trin_len:' + accessions[line.strip()[1:]]['hit_length'])
	else:
		print line.strip()
		




