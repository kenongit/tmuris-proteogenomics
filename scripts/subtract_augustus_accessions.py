#!/usr/bin/python
# Remove UniRef90 accessions hit by Augustus to leave unannotated genes remaining
# EG: /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/hons-project-tmuris/scripts/subtract_augustus_accessions.py /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/combined/all_rna_merged.trin_best_candidates_blastp_uniref90.filtered.1e-30.tophitonly.formatted /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/blast_augustus_uniref/blastp_augustus_uniprot.merged.filtered.tophits
# EG2: /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/hons-project-tmuris/scripts/subtract_augustus_accessions.py /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/combined/all_rna_merged.trin_best_candidates_blastp_uniref90.filtered.1e-30.tophitonly.formatted.uniref90_dupes_removed /Volumes/HUBBARDLAB_BUFFALO/tmuris/master/blast_augustus_uniref/blastp_augustus_uniprot.merged.filtered.tophits
import sys

source_file = open(sys.argv[1], 'r')
deletions_file = open(sys.argv[2], 'r')

deletion_accessions = []
for line in deletions_file:
	deletion_accessions.append(line.strip().split('\t')[1])

for line in source_file:
	if line.strip().split('\t')[1] not in deletion_accessions:
		print line.strip()