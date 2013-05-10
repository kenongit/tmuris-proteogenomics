# Extracts on reads with a specified header accession (the number before the penultimate slash character)
# Works with old–style Illumina paired-end reads with the following header style:
# @HS23_6814:1:1101:2092:2242#6/1
# In the example above, 
# USAGE: python extractFastq.py <fastq_file> <accession_integer>
# EG: python extractFastq.py reads.fastq 6

import sys

input_file = open(sys.argv[1], 'r')
accession = sys.argv[2]

is_inside_read = False

for line in input_file:
	if line.startswith('@'):
		if line[-4:-3] is accession:
			is_inside_read = True
			print line.strip()
		else:
			is_inside_read = False
	elif is_inside_read:
		print line.strip()