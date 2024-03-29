#!/usr/bin/python
# Build an in-memory data structure of a CD-HIT (http://weizhong-lab.ucsd.edu/cd-hit/) .clstr output file
# Substitute first-column (tab delimited) clustered accession names with their cluster group's master accession
# Essentially repeats what CD-HIT already does, but allows one to calculate intersections / make Venns out of unclustered data
#  Let us have four sets of accessions generated by different tissues. We concatenate their fastas them and cluster with CD-HIT
#  This tools lets us rename individual set accessions according to the concatenated clustering information
#  We can therefore acheive the inter-set clustering needed to build Venns
# USAGE: substitute_cd_hit_clustered_accessions_with_master_accession.py <cd_hit_clstr_file> <file_with_accession_names_in_first_column>
# EG: substitute_cd_hit_clustered_accessions_with_master_accession.py all_rna_merged.best_candidates.pep.out.cdhit.clstr <(make_accession_list_from_fasta.py all_rna_merged.best_candidates.pep.out)
# EG2: /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/hons-project-tmuris/scripts/substitute_cd_hit_clustered_accessions_with_master_accession.py /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/cd_hit/all_rna_merged.best_candidates.pep.out.cdhit.clstr <(/Volumes/HUBBARDLAB_BUFFALO/tmuris/master/hons-project-tmuris/scripts/make_accession_list_from_fasta.py /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/cd_hit/adult.best_candidates.pep.out) | awk '!array[$1]'
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
				print master_accession





























