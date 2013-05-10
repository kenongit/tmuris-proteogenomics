#!/usr/bin/python
# Build an in-memory data structure of a CD-HIT (http://weizhong-lab.ucsd.edu/cd-hit/) .clstr output file
# USAGE: parse_cd_hit_cluster_library <clstr_file>

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

print build_cd_hit_data_structure(sys.argv[1])