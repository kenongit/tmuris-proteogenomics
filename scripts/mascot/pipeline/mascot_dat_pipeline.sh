#!/bin/sh
# Modified version of ../mascot_dat_pipeline.sh which creates 'superlist' of PSMs before running them through Qvality, thus generating better q values
# USAGE: mascot_dat_pipeline.sh /path/to/dat/directory/
path="${1}"
path="/Volumes/HUBBARDLAB_BUFFALO/tmuris/2013-04-19/mascot/2013/dat/pipeline/"

echo '-> Parsing'
mkdir -p ${path}
for file in ${path}*fwd*.dat
do
	./parse_mascot_dats_fwd.pl -p -q -e 10000000 -m1 -r1 ${file} > ${file}.parsed
done
for file in ${path}*dcy*.dat
do
	./parse_mascot_dats_dcy.pl -p -q -e 10000000 -m1 -r1 ${file} > ${file}.parsed
done

echo 'Pooling and sorting (completely crucial) PSMs from replicates to maximise q-value accuracy'
cat ${path}*adult*fwd*L2*parsed | sort -rnk6 > ${path}adult_fwd_L2.parsed.pooled
cat ${path}*adult*dcy*L2*parsed | sort -rnk6 > ${path}adult_dcy_L2.parsed.pooled
cat ${path}*adult*fwd*L3*parsed | sort -rnk6 > ${path}adult_fwd_L3.parsed.pooled
cat ${path}*adult*dcy*L3*parsed | sort -rnk6 > ${path}adult_dcy_L3.parsed.pooled
cat ${path}*embryo*fwd*L2*parsed | sort -rnk6 > ${path}embryo_fwd_L2.parsed.pooled
cat ${path}*embryo*dcy*L2*parsed | sort -rnk6 > ${path}embryo_dcy_L2.parsed.pooled
cat ${path}*embryo*fwd*L3*parsed | sort -rnk6 > ${path}embryo_fwd_L3.parsed.pooled
cat ${path}*embryo*dcy*L3*parsed | sort -rnk6 > ${path}embryo_dcy_L3.parsed.pooled
cat ${path}*frear*fwd*L2*parsed | sort -rnk6 > ${path}frear_fwd_L2.parsed.pooled
cat ${path}*frear*dcy*L2*parsed | sort -rnk6 > ${path}frear_dcy_L2.parsed.pooled
cat ${path}*frear*fwd*L3*parsed | sort -rnk6 > ${path}frear_fwd_L3.parsed.pooled
cat ${path}*frear*dcy*L3*parsed | sort -rnk6 > ${path}frear_dcy_L3.parsed.pooled
cat ${path}*stichosome*fwd*L2*parsed | sort -rnk6 > ${path}stichosome_fwd_L2.parsed.pooled
cat ${path}*stichosome*dcy*L2*parsed | sort -rnk6 > ${path}stichosome_dcy_L2.parsed.pooled
cat ${path}*stichosome*fwd*L3*parsed | sort -rnk6 > ${path}stichosome_fwd_L3.parsed.pooled
cat ${path}*stichosome*dcy*L3*parsed | sort -rnk6 > ${path}stichosome_dcy_L3.parsed.pooled
cat ${path}*augustus*fwd*L2*parsed | sort -rnk6 > ${path}augustus_fwd_L2.parsed.pooled
cat ${path}*augustus*dcy*L2*parsed | sort -rnk6 > ${path}augustus_dcy_L2.parsed.pooled
cat ${path}*augustus*fwd*L3*parsed | sort -rnk6 > ${path}augustus_fwd_L3.parsed.pooled
cat ${path}*augustus*dcy*L3*parsed | sort -rnk6 > ${path}augustus_dcy_L3.parsed.pooled

echo '-> Generating Qvality stats'
# Strip MASCOT scores
awk -F " " '{print $6}' ${path}adult_fwd_L2.parsed.pooled > ${path}adult_fwd_L2.parsed.pooled.scores
awk -F " " '{print $6}' ${path}adult_dcy_L2.parsed.pooled > ${path}adult_dcy_L2.parsed.pooled.scores
awk -F " " '{print $6}' ${path}adult_fwd_L3.parsed.pooled > ${path}adult_fwd_L3.parsed.pooled.scores
awk -F " " '{print $6}' ${path}adult_dcy_L3.parsed.pooled > ${path}adult_dcy_L3.parsed.pooled.scores
awk -F " " '{print $6}' ${path}embryo_fwd_L2.parsed.pooled > ${path}embryo_fwd_L2.parsed.pooled.scores
awk -F " " '{print $6}' ${path}embryo_dcy_L2.parsed.pooled > ${path}embryo_dcy_L2.parsed.pooled.scores
awk -F " " '{print $6}' ${path}embryo_fwd_L3.parsed.pooled > ${path}embryo_fwd_L3.parsed.pooled.scores
awk -F " " '{print $6}' ${path}embryo_dcy_L3.parsed.pooled > ${path}embryo_dcy_L3.parsed.pooled.scores
awk -F " " '{print $6}' ${path}frear_fwd_L2.parsed.pooled > ${path}frear_fwd_L2.parsed.pooled.scores 
awk -F " " '{print $6}' ${path}frear_dcy_L2.parsed.pooled > ${path}frear_dcy_L2.parsed.pooled.scores
awk -F " " '{print $6}' ${path}frear_fwd_L3.parsed.pooled > ${path}frear_fwd_L3.parsed.pooled.scores
awk -F " " '{print $6}' ${path}frear_dcy_L3.parsed.pooled > ${path}frear_dcy_L3.parsed.pooled.scores
awk -F " " '{print $6}' ${path}stichosome_fwd_L2.parsed.pooled > ${path}stichosome_fwd_L2.parsed.pooled.scores
awk -F " " '{print $6}' ${path}stichosome_dcy_L2.parsed.pooled > ${path}stichosome_dcy_L2.parsed.pooled.scores
awk -F " " '{print $6}' ${path}stichosome_fwd_L3.parsed.pooled > ${path}stichosome_fwd_L3.parsed.pooled.scores
awk -F " " '{print $6}' ${path}stichosome_dcy_L3.parsed.pooled > ${path}stichosome_dcy_L3.parsed.pooled.scores
awk -F " " '{print $6}' ${path}augustus_fwd_L2.parsed.pooled > ${path}augustus_fwd_L2.parsed.pooled.scores
awk -F " " '{print $6}' ${path}augustus_dcy_L2.parsed.pooled > ${path}augustus_dcy_L2.parsed.pooled.scores
awk -F " " '{print $6}' ${path}augustus_fwd_L3.parsed.pooled > ${path}augustus_fwd_L3.parsed.pooled.scores
awk -F " " '{print $6}' ${path}augustus_dcy_L3.parsed.pooled > ${path}augustus_dcy_L3.parsed.pooled.scores
# Run MASCOT scores through qvality, with decoy scores serving as a null distribution
./qvality ${path}adult_fwd_L2.parsed.pooled.scores ${path}adult_dcy_L2.parsed.pooled.scores -o ${path}adult_L2.qvality
./qvality ${path}adult_fwd_L3.parsed.pooled.scores ${path}adult_dcy_L3.parsed.pooled.scores -o ${path}adult_L3.qvality
./qvality ${path}embryo_fwd_L2.parsed.pooled.scores ${path}embryo_dcy_L2.parsed.pooled.scores -o ${path}embryo_L2.qvality
./qvality ${path}embryo_fwd_L3.parsed.pooled.scores ${path}embryo_dcy_L3.parsed.pooled.scores -o ${path}embryo_L3.qvality
./qvality ${path}frear_fwd_L2.parsed.pooled.scores ${path}frear_dcy_L2.parsed.pooled.scores -o ${path}frear_L2.qvality
./qvality ${path}frear_fwd_L3.parsed.pooled.scores ${path}frear_dcy_L3.parsed.pooled.scores -o ${path}frear_L3.qvality
./qvality ${path}stichosome_fwd_L2.parsed.pooled.scores ${path}stichosome_dcy_L2.parsed.pooled.scores -o ${path}stichosome_L2.qvality
./qvality ${path}stichosome_fwd_L3.parsed.pooled.scores ${path}stichosome_dcy_L3.parsed.pooled.scores -o ${path}stichosome_L3.qvality
./qvality ${path}augustus_fwd_L2.parsed.pooled.scores ${path}augustus_dcy_L2.parsed.pooled.scores -o ${path}augustus_L2.qvality
./qvality ${path}augustus_fwd_L3.parsed.pooled.scores ${path}augustus_dcy_L3.parsed.pooled.scores -o ${path}augustus_L3.qvality
echo '-> Deleting header lines'
for file in ${path}*.qvality
do
	perl -pi -e '$_ = "" if ($. == 1);' ${file}
done
echo '-> Merging Qvality stats'
./output_scored_psms.py ${path}adult_fwd_L2.parsed.pooled ${path}adult_L2.qvality
./output_scored_psms.py ${path}adult_fwd_L3.parsed.pooled ${path}adult_L3.qvality
./output_scored_psms.py ${path}embryo_fwd_L2.parsed.pooled ${path}embryo_L2.qvality
./output_scored_psms.py ${path}embryo_fwd_L3.parsed.pooled ${path}embryo_L3.qvality
./output_scored_psms.py ${path}frear_fwd_L2.parsed.pooled ${path}frear_L2.qvality
./output_scored_psms.py ${path}frear_fwd_L3.parsed.pooled ${path}frear_L3.qvality
./output_scored_psms.py ${path}stichosome_fwd_L2.parsed.pooled ${path}stichosome_L2.qvality
./output_scored_psms.py ${path}stichosome_fwd_L3.parsed.pooled ${path}stichosome_L3.qvality
./output_scored_psms.py ${path}augustus_fwd_L2.parsed.pooled ${path}augustus_L2.qvality
./output_scored_psms.py ${path}augustus_fwd_L3.parsed.pooled ${path}augustus_L3.qvality

echo '-> Discarding PSMs with q-value >0.01'
for file in ${path}*.qvality.psm
do
	awk '$4 <= 0.01 {print $0}' ${file} > ${file}.filtered
done

echo '-> Generating lists of putative proteins with their supporting PSMs'
for file in ${path}*.psm.filtered
do
	./output_psms_by_protein_accession.py ${file} | sort -rnk 3 -t '	' > ${file}.psmsbyprotein.sorted
done

echo '-> Discarding putative proteins with <2 unique PSMs'
for file in ${path}*.psmsbyprotein.sorted
do
	./remove_proteins_without_sufficient_unique_psms.py ${file} | sort -rnk 3 -t '	' > ${file}.2uniquepsms
done

echo '-> Discarding putative proteins with identical supporting PSMs to reduce redundancy in reported hits'
for file in ${path}*.sorted.2uniquepsms
do
	awk '!array[$2]++' ${file} > ${file}.deduped
done

echo '-> Aggregating putative proteins from the different RNAseq runs'
# Sort and deduplicate
cat ${path}*adult*.deduped ${path}*embryo*.deduped ${path}*frear*.deduped ${path}*stichosome*.deduped | sort -rnk 3 -t '	' | awk '!array[$2]++' > ${path}../aggregated/rna.alltissues.L2L3.aggregated
cat ${path}*adult*L2*.deduped ${path}*embryo*L2*.deduped ${path}*frear*L2*.deduped ${path}*stichosome*L2*.deduped | sort -rnk 3 -t '	' | awk '!array[$2]++' > ${path}../aggregated/rna.alltissues.L2.aggregated
cat ${path}*adult*L3*.deduped ${path}*embryo*L3*.deduped ${path}*frear*L3*.deduped ${path}*stichosome*L3*.deduped | sort -rnk 3 -t '	' | awk '!array[$2]++' > ${path}../aggregated/rna.alltissues.L3.aggregated
cat ${path}*augustus*.deduped  | sort -rnk 3 -t '	' | awk '!array[$2]++' > ${path}../aggregated/augustus.L2L3.aggregated
cat ${path}*augustus*L2*.deduped  | sort -rnk 3 -t '	' | awk '!array[$2]++' > ${path}../aggregated/augustus.L2.aggregated
cat ${path}*augustus*L3*.deduped  | sort -rnk 3 -t '	' | awk '!array[$2]++' > ${path}../aggregated/augustus.L3.aggregated

echo 'DONE'