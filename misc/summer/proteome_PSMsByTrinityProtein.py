# Generate list of potential Trinity proteins with comma separated supporting PSMs for each
# Accepts five column output from outputScoredPSMs.py
# Outputs format: Trinity ID, Matched peptides (comma delimited)
# USAGE: proteome_PSMsByTrinityProtein.py <tissue>

import sys

proteins = {}

input = open(sys.argv[1], "r")

for line in input:
	line = line.split('	')
	psm = line[0]
	trinity_proteins = line[4].replace(',\n', '').split(',')
	
	for trinity_protein in trinity_proteins:
		if trinity_protein not in proteins: 
			proteins[trinity_protein] = []
		proteins[trinity_protein].append(psm)

input.close()

# Output Trinity proteins with their corresponding PSMs
for trinity_protein, psms in proteins.iteritems():
	print trinity_protein + '\t' + ','.join(psms)
	


