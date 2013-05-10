#! /bin/sh
# Output PSMs with PEP and q values from forward and corresponding reverse/decoy MASCOT .dat files
# USAGE: datToScoredPSMs.pipe.sh <forward.dat> <decoy.dat>

echo Forward dat: $1 
echo Decoy dat: $2

# Parse
../mascot_dat_parser_fixed.pl -p -q -e 10000000 -m1 -r1 ../mascot/adu.f291554845.dat > ../mascot/adu.f291554845.dat.parsed
../mascot_dat_parser_fixed_dcy.pl -p -q -e 10000000 -m1 -r1 ../mascot/adu.dcy.f291554969.dat > ../mascot/adu.dcy.f291554969.dat.parsed

# Strip MASCOT scores
awk -F " " '{print $6}' ../mascot/adu.f291554845.dat.parsed > ../mascot/adu.f291554845.dat.parsed.stripped
awk -F " " '{print $6}' ../mascot/adu.dcy.f291554969.dat.parsed > ../mascot/adu.dcy.f291554969.dat.parsed.stripped

# Run MASCOT scores through qvality, with decoy scores serving as a null distribution
../qvality ../mascot/adu.f291554845.dat.parsed.stripped ../mascot/adu.dcy.f291554969.dat.parsed.stripped -o ../mascot/adu.f291554845.f291554969_dcy.stats

# Delete header line of qvality output
perl -pi -e '$_ = "" if ($. == 1);' ../mascot/adu.f291554845.f291554969_dcy.stats

# Merge PSMs with their corresponding qvality stats
python ../outputScoredPSMs.py ../mascot/adu.f291554845.dat.parsed ../mascot/adu.f291554845.f291554969_dcy.stats

# Tidy up
mv ../mascot/adu.f291554845.dat.parsed ../mascot/parsed/adu.f291554845.dat.parsed
mv ../mascot/adu.dcy.f291554969.dat.parsed ../mascot/parsed/adu.dcy.f291554969.dat.parsed
mv ../mascot/adu.f291554845.f291554969_dcy.stats.psm ../mascot/psm/adu.f291554845.f291554969_dcy.stats.psm
rm ../mascot/adu.dcy.f291554969.dat.parsed.stripped
rm ../mascot/adu.f291554845.dat.parsed.stripped
rm ../mascot/adu.f291554845.f291554969_dcy.stats