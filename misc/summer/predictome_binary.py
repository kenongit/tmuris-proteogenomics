# Check for presence of specific genes across multiple (currently four) tissues/files
# Fifth argument is the query set of genes for which we are looking.
# Outputs CSV (fourth argument) with row format <geneID>,<bool_tis1>,<bool_tis2>,<bool_tis3>,<bool_tis4>
# USAGE: python predictome_binary.py <tis1> <tis2> <tis3> <tis4> <query> <outputCSV>

import sys

genes = {}

csv = open(sys.argv[6], "w")

# Iterate over tissues
for arg in range(1,5):
	if(arg == 1): tissue = 'adult'
	if(arg == 2): tissue = 'embryo'
	if(arg == 3): tissue = 'frear'
	if(arg == 4): tissue = 'stichosome'

	tissueGenesFile = open(sys.argv[arg], "r")
	tissueGenes = tissueGenesFile.read()
	query = open(sys.argv[5], "r")

	for line in query:
		currentQueryGene = line.replace('g','').strip('\n')
		if currentQueryGene not in genes: genes[currentQueryGene] = {}
		if tissue not in genes[currentQueryGene]: genes[currentQueryGene][tissue] = {}
		if currentQueryGene in tissueGenes:
			genes[currentQueryGene][tissue] = 1
		else:
			genes[currentQueryGene][tissue] = 0
	
	tissueGenesFile.close()
	query.close()

for gene, expression in genes.iteritems():
	csv.write(gene + ',' + str(expression['adult']) + ',' + str(expression['embryo']) + ',' + str(expression['frear']) + ',' + str(expression['stichosome']) + '\n')

csv.close()