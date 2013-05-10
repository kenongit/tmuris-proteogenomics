# Check for presence of each gene in each tissue, with tissue data supplied as command line arguments.
# Output stats needed for a four tissue / set Venn diagram

import sys

# Usage instructions
if(len(sys.argv) == 1):
	sys.exit('fetchVennResults <tissue1> <tissue2> <tissue3> <tissue4>')

genes = {}
geneCounter = 1
genes[geneCounter] = {'adult':0, 'embryo':0, 'frear':0, 'stichosome':0}

# Out
for arg in range(1,5):
	if(arg == 1): tissue = 'adult'
	if(arg == 2): tissue = 'embryo'
	if(arg == 3): tissue = 'frear'
	if(arg == 4): tissue = 'stichosome'

	input = open(sys.argv[arg], "r")
	text = input.read()

	geneCounter = 1
	while geneCounter < 10000:
		if geneCounter not in genes:
			genes[geneCounter] = {}
		if tissue not in genes[geneCounter]:
			genes[geneCounter][tissue] = {}
		if 'g' + str(geneCounter) + '\n' in text:
			genes[geneCounter][tissue] = 1
		else:
			genes[geneCounter][tissue] = 0
		geneCounter += 1
	
	input.close()



print genes

	