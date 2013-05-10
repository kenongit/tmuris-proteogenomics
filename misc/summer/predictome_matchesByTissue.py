# Count blastx hits across multiple (four) tissues/files
# Outputs CSV with row format <geneID>,<freq_tissue1>,<freq_tissue2>,<freq_tissue3>,<freq_tissue4>
# USAGE: python predictome_matchesByTissue.py <tissue1> <tissue2> <tissue3> <tissue4>

import sys

genes = {}

# Iterate over tissues
for arg in range(1,5):
	
	if(arg == 1): tissue = 'adult'
	if(arg == 2): tissue = 'embryo'
	if(arg == 3): tissue = 'frear'
	if(arg == 4): tissue = 'stichosome'

	tissueGenes = open(sys.argv[arg], "r")

	for line in tissueGenes:
		
		# Grab gene ID from second column
		currentGene = line.split('\t')[1].replace('g','').strip('\n')

		# Multidimensional dictionary vivification
		if currentGene not in genes: genes[currentGene] = {}
		if 'adult' not in genes[currentGene]: genes[currentGene]['adult'] = 0
		if 'embryo' not in genes[currentGene]: genes[currentGene]['embryo'] = 0
		if 'frear' not in genes[currentGene]: genes[currentGene]['frear'] = 0
		if 'stichosome' not in genes[currentGene]: genes[currentGene]['stichosome'] = 0
		if tissue in genes[currentGene]:
			genes[currentGene][tissue] += 1
	
	tissueGenes.close()

# Output comma separated expression levels to stdout for sorting / awk-ing etc.
for gene, expression in genes.iteritems():
	print(
		# gene + ',' + str(expression['adult']) + ',' +str(expression['embryo']) +
		str(expression['adult']) + ',' + str(expression['embryo']) +
		',' + str(expression['frear']) + ',' + str(expression['stichosome'])
	)