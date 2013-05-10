# Determine intersections of PSM peptides within concatenated proteome observations across four tissues
# USAGE: python proteome_vennPSM.py <tissue_1> <tissue_2> <tissue_3> <tissue_4>
# Input file example row: QIVQSSAIMR	37.1	0.0499727	0.00339721	STIm.8653,STIm.9156,

import sys

peptides = {}

# Establish every individual protein present in the files supplied
for arg in range(1,5):
	for line in open(sys.argv[arg]):
		peptide = line.strip('\n').split('\t')[0]
		if peptide not in peptides:
			peptides[peptide] = []

# Establish whether PSMs are present across individual tissues
for arg in range(1,5):
	if arg == 1: tissue = 'adult'
	if arg == 2: tissue = 'embryo'
	if arg == 3: tissue = 'frear'
	if arg == 4: tissue = 'stichosome'
	for line in open(sys.argv[arg]):
		peptide = line.strip('\n').split('\t')[0]
		if tissue not in peptides[peptide]:
			peptides[peptide].append(tissue)

# for peptide, tissues in peptides.iteritems():
# 	print peptide, tissues

# Generate Venn stats

counter = 0
for peptide, tissues in peptides.iteritems():
	if 'adult' in tissues:
		counter += 1
print 'area1 = ' + str(counter)

counter = 0
for peptide, tissues in peptides.iteritems():
	if 'embryo' in tissues:
		counter += 1
print 'area2 = ' + str(counter)

counter = 0
for peptide, tissues in peptides.iteritems():
	if 'frear' in tissues:
		counter += 1
print 'area3 = ' + str(counter)

counter = 0
for peptide, tissues in peptides.iteritems():
	if 'stichosome' in tissues:
		counter += 1
print 'area4 = ' + str(counter)

counter = 0
for peptide, tissues in peptides.iteritems():
	if('adult' in tissues and 'embryo' in tissues):
		counter += 1
print 'n12 = ' + str(counter)

counter = 0
for peptide, tissues in peptides.iteritems():
	if('adult' in tissues and 'frear' in tissues):
		counter += 1
print 'n13 = ' + str(counter)

counter = 0
for peptide, tissues in peptides.iteritems():
	if('adult' in tissues and 'stichosome' in tissues):
		counter += 1
print 'n14 = ' + str(counter)

counter = 0
for peptide, tissues in peptides.iteritems():
	if('embryo' in tissues and 'frear' in tissues):
		counter += 1
print 'n23 = ' + str(counter)

counter = 0
for peptide, tissues in peptides.iteritems():
	if('embryo' in tissues and 'stichosome' in tissues):
		counter += 1
print 'n24 = ' + str(counter)

counter = 0
for peptide, tissues in peptides.iteritems():
	if('frear' in tissues and 'stichosome' in tissues):
		counter += 1
print 'n34 = ' + str(counter)

counter = 0
for peptide, tissues in peptides.iteritems():
	if('adult' in tissues and 'embryo' in tissues and 'frear' in tissues):
		counter += 1
print 'n123 = ' + str(counter)

counter = 0
for peptide, tissues in peptides.iteritems():
	if('adult' in tissues and 'embryo' in tissues and 'stichosome' in tissues):
		counter += 1
print 'n124 = ' + str(counter)

counter = 0
for peptide, tissues in peptides.iteritems():
	if('adult' in tissues and 'frear' in tissues and 'stichosome' in tissues):
		counter += 1
print 'n134 = ' + str(counter)

counter = 0
for peptide, tissues in peptides.iteritems():
	if('embryo' in tissues and 'frear' in tissues and 'stichosome' in tissues):
		counter += 1
print 'n234 = ' + str(counter)

counter = 0
for peptide, tissues in peptides.iteritems():
	if('adult' in tissues and 'embryo' in tissues and 'frear' in tissues and 'stichosome' in tissues):
		counter += 1
print 'n1234 = ' + str(counter)