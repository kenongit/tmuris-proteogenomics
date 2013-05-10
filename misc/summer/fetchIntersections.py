# Check for presence of each gene in each of four tissues, with tissue data supplied as command line arguments.
# Output data needed for plotting a Venn diagram with the R package 'VennDiagram'
# python fetchIntersections.py /Users/Bede/Data/adult/adult.augustus_uniques.counts /Users/Bede/Data/embryo/embryo.augustus_uniques.counts /Users/Bede/Data/frear/frear.augustus_uniques.counts /Users/Bede/Data/stichosome/stichosome.augustus_uniques.counts

import sys

genes = {}
geneCounter = 1

# Determine the presence of each gene in each tissue
for arg in range(1,5):
	if(arg == 1): tissue = 'adult'
	if(arg == 2): tissue = 'embryo'
	if(arg == 3): tissue = 'frear'
	if(arg == 4): tissue = 'stichosome'

	input = open(sys.argv[arg], "r")
	text = input.read()

	geneCounter = 1
	while geneCounter < 10000:
		if geneCounter not in genes: genes[geneCounter] = {}
		if tissue not in genes[geneCounter]: genes[geneCounter][tissue] = {}
		if 'g' + str(geneCounter) + '\n' in text:
			genes[geneCounter][tissue] = 1
		else:
			genes[geneCounter][tissue] = 0
		geneCounter += 1
	
	input.close()

# Output statistics

counter = 0
for key, values in genes.iteritems():
	if(values['adult'] == 1):
		counter += 1
print 'area1 = ' + str(counter)

counter = 0
for key, values in genes.iteritems():
	if(values['embryo'] == 1):
		counter += 1
print 'area2 = ' + str(counter)

counter = 0
for key, values in genes.iteritems():
	if(values['frear'] == 1):
		counter += 1
print 'area3 = ' + str(counter)

counter = 0
for key, values in genes.iteritems():
	if(values['stichosome'] == 1):
		counter += 1
print 'area4 = ' + str(counter)

counter = 0
for key, values in genes.iteritems():
	if(values['adult'] == 1 and values['embryo'] == 1 ):
		counter += 1
print 'n12 = ' + str(counter)

counter = 0
for key, values in genes.iteritems():
	if(values['adult'] == 1 and values['frear'] == 1):
		counter += 1
print 'n13 = ' + str(counter)

counter = 0
for key, values in genes.iteritems():
	if(values['adult'] == 1 and values['stichosome'] == 1):
		counter += 1
print 'n14 = ' + str(counter)

counter = 0
for key, values in genes.iteritems():
	if(values['embryo'] == 1 and values['frear'] == 1):
		counter += 1
print 'n23 = ' + str(counter)

counter = 0
for key, values in genes.iteritems():
	if(values['embryo'] == 1 and values['stichosome'] == 1):
		counter += 1
print 'n24 = ' + str(counter)

counter = 0
for key, values in genes.iteritems():
	if(values['frear'] == 1 and values['stichosome'] == 1):
		counter += 1
print 'n34 = ' + str(counter)

counter = 0
for key, values in genes.iteritems():
	if(values['adult'] == 1 and values['embryo'] == 1 and values['frear'] == 1):
		counter += 1
print 'n123 = ' + str(counter)

counter = 0
for key, values in genes.iteritems():
	if(values['adult'] == 1 and values['embryo'] == 1 and values['stichosome'] == 1):
		counter += 1
print 'n124 = ' + str(counter)

counter = 0
for key, values in genes.iteritems():
	if(values['adult'] == 1 and values['frear'] == 1 and values['stichosome'] == 1):
		counter += 1
print 'n134 = ' + str(counter)

counter = 0
for key, values in genes.iteritems():
	if(values['embryo'] == 1 and values['frear'] == 1 and values['stichosome'] == 1):
		counter += 1
print 'n234 = ' + str(counter)

counter = 0
for key, values in genes.iteritems():
	if(values['adult'] == 1 and values['embryo'] == 1 and values['frear'] == 1 and values['stichosome'] == 1):
		counter += 1
print 'n1234 = ' + str(counter)