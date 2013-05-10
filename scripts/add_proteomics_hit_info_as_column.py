#!/usr/bin/python
# Add proteomics hit information to line where the first tab delimited column is an PSM-supported accession
# USAGE: add_proteomics_hit_info_as_column.py <existing_file> <proteomics_file> <identifier>
# EG: add_proteomics_hit_info_as_column.py all_rna_merged.best_candidates-uniref90.blastp.merged.filtered.1e-30.tophitonly rna.alltissues.L2.aggregated.notunique L2
# EG2: /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/hons-project-tmuris/scripts/add_proteomics_hit_info_as_column.py /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/blast_trinity_uniref/complete_and_merged/all_rna_merged.best_candidates-uniref90.blastp.merged.filtered.1e-30.tophitonly /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/mascot/2013/dat/aggregated/rna.alltissues.L2.aggregated L2
# EG3: /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/hons-project-tmuris/scripts/add_proteomics_hit_info_as_column.py /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/blast_trinity_uniref/combined/all_rna_merged.trin_best_candidates_blastp_uniref90.filtered.1e-30.tophitonly.l2hits /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/mascot/2013/dat/aggregated/rna.alltissues.L3.aggregated L3 > /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/blast_trinity_uniref/combined/all_rna_merged.trin_best_candidates_blastp_uniref90.filtered.1e-30.tophitonly.l2l3hits

import sys

accessions_library_file = open(sys.argv[1], 'r')
proteomics_accessions_file = open(sys.argv[2], 'r')
proteomics_identifier = sys.argv[3]

proteomics_accessions = {}
for line in proteomics_accessions_file:
	proteomics_accession = line.strip().split('\t')[0]
	proteomics_accessions[proteomics_accession] = line.strip()

for line in accessions_library_file:
	is_proteome_hit = False
	accessions_library_accession = line.strip().split('\t')[0]
	for accession in proteomics_accessions:
		if accession == accessions_library_accession:
			is_proteome_hit = True
			proteomics_stats = proteomics_accessions[accession].strip().split('\t')
	if is_proteome_hit:
		print (line.strip() + '\t' + 'ms2:'
			+ proteomics_identifier + '|n_psm:' +  proteomics_stats[2]
			+ '|n_psm_uniq:' + proteomics_stats[3])
	else:
		print line.strip()
