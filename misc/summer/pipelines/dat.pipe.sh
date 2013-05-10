#! /bin/sh
# Output peptides with Mascot scores, PEPs, q-values and alignment hits when fed forward and reverse Mascot .dat files
# USAGE: dat.pipe.sh <tissue_prefix> <forward_file_id> <decoy_file_id> <pair_prefix>
# EG: dat.pipe.sh adu f291554845 f2915549697 pellet1

base_path="../mascot/"
tissue_prefix="${1}"
forward_id="${2}"
decoy_id="${3}"
pair_prefix="${4}"
forward_dat="${tissue_prefix}.${pair_prefix}.${forward_id}.dat"
decoy_dat="${tissue_prefix}.dcy.${pair_prefix}.${decoy_id}.dat"

echo "Forward dat: ${forward_dat}"
echo "Decoy dat: ${decoy_dat}"

echo '-> Parsing'
../mascot_dat_parser_fixed.pl -p -q -e 10000000 -m1 -r1 ${base_path}${forward_dat} > ${base_path}${forward_dat}.parsed
../mascot_dat_parser_fixed_dcy.pl -p -q -e 10000000 -m1 -r1 ${base_path}${decoy_dat} > ${base_path}${decoy_dat}.parsed

echo '-> Generating Qvality stats'
# Strip MASCOT scores
awk -F " " '{print $6}' ${base_path}${forward_dat}.parsed > ${base_path}${forward_dat}.parsed.stripped
awk -F " " '{print $6}' ${base_path}${decoy_dat}.parsed > ${base_path}${decoy_dat}.parsed.stripped
# Run MASCOT scores through qvality, with decoy scores serving as a null distribution
../qvality ${base_path}${forward_dat}.parsed.stripped ${base_path}${decoy_dat}.parsed.stripped -o ${base_path}${tissue_prefix}.${pair_prefix}.${forward_id}.${decoy_id}_dcy.stats

echo '-> Tidying up'
# Delete header line of qvality output
perl -pi -e '$_ = "" if ($. == 1);' ${base_path}${tissue_prefix}.${pair_prefix}.${forward_id}.${decoy_id}_dcy.stats
# Merge PSMs with their corresponding qvality stats
python ../outputScoredPSMs.py ${base_path}${forward_dat}.parsed ${base_path}${tissue_prefix}.${pair_prefix}.${forward_id}.${decoy_id}_dcy.stats
# Tidy up
mv ${base_path}${forward_dat}.parsed ${base_path}parsed/${forward_dat}.parsed
mv ${base_path}${decoy_dat}.parsed ${base_path}parsed/${decoy_dat}.parsed
mv ${base_path}${tissue_prefix}.${pair_prefix}.${forward_id}.${decoy_id}_dcy.stats.psm ${base_path}psm/${tissue_prefix}.${pair_prefix}.${forward_id}.${decoy_id}_dcy.stats.psm
rm ${base_path}${forward_dat}.parsed.stripped
rm ${base_path}${decoy_dat}.parsed.stripped
rm ${base_path}${tissue_prefix}.${pair_prefix}.${forward_id}.${decoy_id}_dcy.stats

echo '-> Other bits and pieces'
# Filter PSMs to include only peptides with q value < 0.01 (1% FDR) and ensure each peptide occurs only once
awk '$4 <= 0.01 {print $0}' ${base_path}psm/${tissue_prefix}.${pair_prefix}.${forward_id}.${decoy_id}_dcy.stats.psm > ${base_path}psm/filtered_qvalue/${tissue_prefix}.${pair_prefix}.${forward_id}.${decoy_id}_dcy.stats.unique.psm
# As above, but also ensure each peptide occurs only once
awk '$4 <= 0.01 {print $0}' ${base_path}psm/${tissue_prefix}.${pair_prefix}.${forward_id}.${decoy_id}_dcy.stats.psm | awk '!array[$1]++' > ${base_path}psm/filtered_qvalue_unique/${tissue_prefix}.${pair_prefix}.${forward_id}.${decoy_id}_dcy.stats.unique.psm
# Generate list of potential Trinity proteins with comma separated supporting PSMs (for later cocatenation by tissue)
python ../proteome_PSMsByTrinityProtein.py ${base_path}psm/filtered_qvalue_unique/${tissue_prefix}.${pair_prefix}.${forward_id}.${decoy_id}_dcy.stats.unique.psm > ${base_path}psm/psm_by_trinity/${tissue_prefix}.${pair_prefix}.${forward_id}.${decoy_id}_dcy.trinity.psm

echo '-> DONE'