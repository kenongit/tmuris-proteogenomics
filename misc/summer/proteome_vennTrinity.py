# Determine intersections for possible Trinity protein presence within concatenated proteome observations across four tissues
# USAGE: python proteome_vennTrinity.py <tissue_1> <tissue_2> <tissue_3> <tissue_4>
# Input file example row: STIm.266964	AADSAEYTCVAETK,GSTNAGVGDPSSVDVK,VTQLPGEGSFVLSK

import sys

proteins = {}

# Establish every individual protein present in the files supplied
for arg in range(1,5):
	for line in open(sys.argv[arg]):
		trinity_protein = line.strip('\n').split('\t')[0][3:]
		if trinity_protein not in proteins:
			proteins[trinity_protein] = []

# Establish whether PSMs exist for each protein across each tissue
for arg in range(1,5):
	if arg == 1: tissue = 'adult'
	if arg == 2: tissue = 'embryo'
	if arg == 3: tissue = 'frear'
	if arg == 4: tissue = 'stichosome'
	for line in open(sys.argv[arg]):
		trinity_protein = line.strip('\n').split('\t')[0][3:]
		if tissue not in proteins[trinity_protein]:
			proteins[trinity_protein].append(tissue)

# for protein, tissues in proteins.iteritems():
# 	print protein, tissues

# Generate Venn stats

counter = 0
for protein, tissues in proteins.iteritems():
	if 'adult' in tissues:
		counter += 1
print 'area1 = ' + str(counter)

counter = 0
for protein, tissues in proteins.iteritems():
	if 'embryo' in tissues:
		counter += 1
print 'area2 = ' + str(counter)

counter = 0
for protein, tissues in proteins.iteritems():
	if 'frear' in tissues:
		counter += 1
print 'area3 = ' + str(counter)

counter = 0
for protein, tissues in proteins.iteritems():
	if 'stichosome' in tissues:
		counter += 1
print 'area4 = ' + str(counter)

counter = 0
for protein, tissues in proteins.iteritems():
	if('adult' in tissues and 'embryo' in tissues):
		counter += 1
print 'n12 = ' + str(counter)

counter = 0
for protein, tissues in proteins.iteritems():
	if('adult' in tissues and 'frear' in tissues):
		counter += 1
print 'n13 = ' + str(counter)

counter = 0
for protein, tissues in proteins.iteritems():
	if('adult' in tissues and 'stichosome' in tissues):
		counter += 1
print 'n14 = ' + str(counter)

counter = 0
for protein, tissues in proteins.iteritems():
	if('embryo' in tissues and 'frear' in tissues):
		counter += 1
print 'n23 = ' + str(counter)

counter = 0
for protein, tissues in proteins.iteritems():
	if('embryo' in tissues and 'stichosome' in tissues):
		counter += 1
print 'n24 = ' + str(counter)

counter = 0
for protein, tissues in proteins.iteritems():
	if('frear' in tissues and 'stichosome' in tissues):
		counter += 1
print 'n34 = ' + str(counter)

counter = 0
for protein, tissues in proteins.iteritems():
	if('adult' in tissues and 'embryo' in tissues and 'frear' in tissues):
		counter += 1
print 'n123 = ' + str(counter)

counter = 0
for protein, tissues in proteins.iteritems():
	if('adult' in tissues and 'embryo' in tissues and 'stichosome' in tissues):
		counter += 1
print 'n124 = ' + str(counter)

counter = 0
for protein, tissues in proteins.iteritems():
	if('adult' in tissues and 'frear' in tissues and 'stichosome' in tissues):
		counter += 1
print 'n134 = ' + str(counter)

counter = 0
for protein, tissues in proteins.iteritems():
	if('embryo' in tissues and 'frear' in tissues and 'stichosome' in tissues):
		counter += 1
print 'n234 = ' + str(counter)

counter = 0
for protein, tissues in proteins.iteritems():
	if('adult' in tissues and 'embryo' in tissues and 'frear' in tissues and 'stichosome' in tissues):
		counter += 1
print 'n1234 = ' + str(counter)