#!/usr/bin/python
# Add a CD-HIT master cluster accession to the end of the line, where the start of the line is a CD-HIT cluster accession
# Builds an in-memory data structure of a CD-HIT (http://weizhong-lab.ucsd.edu/cd-hit/) .clstr output file
# USAGE: add_cd_hit_master_accession_as_column.py <cd_hit_clstr_file> <file_with_accession_names_in_first_column>
# EG: /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/hons-project-tmuris/scripts/add_cd_hit_master_accession_as_column.py /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/cd_hit/all_rna_merged.best_candidates.pep.out.cdhit.clstr /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/blast_trinity_uniref/complete_and_merged/all_rna_merged.best_candidates-uniref90.blastp.merged.filtered.1e-30.tophitonly
import sys

def build_cd_hit_data_structure(clstr_file):
	clstr_file = open(clstr_file, 'r')
	clusters = {}
	for line in clstr_file:
		if line.startswith('>'):
			found_master_accession = False
			line = line[1:].strip().split(' ')
			cluster_id = line[1]
			clusters[cluster_id] = []
		elif line[0].isdigit():
			accession = line.split(' ')[1][1:].strip('...')
			if '*' in line:
				found_master_accession = True
				master_accession = accession
				clusters[master_accession] = clusters.pop(cluster_id)
			if found_master_accession:
				clusters[master_accession].append(accession)
			else:
				clusters[cluster_id].append(accession)
	return clusters

clusters = build_cd_hit_data_structure(sys.argv[1])

accession_file = open(sys.argv[2], 'r')

for line in accession_file:
	accession = line.strip().split('\t')[0]
	for master_accession in clusters:
		for cluster_accession in clusters[master_accession]:
			if cluster_accession == accession:
				print line.strip() + '\t' + master_accession





























