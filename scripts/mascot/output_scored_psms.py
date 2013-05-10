#!/usr/bin/python
# Merge PSMs with their Mascot, PEP and q value scores when given parsed MASCOT output and Qvality output
# Remove headers from input files before use
# USAGE: python output_scored_psms.py <parsed_mascot_output> <qvality_output>

import sys
import re

mascot_input = open(sys.argv[1], 'r')
qvality_input = open(sys.argv[2], 'r')
output = open(sys.argv[2] + '.psm', 'w')

for line in mascot_input:
	line = re.sub('[ \t]+' , ' ', line) # Normalise column spacing before splitting
	line = line.strip('\n').split(' ')
	stats = qvality_input.readline().strip('\n').split('	')
	output.write(line[8] + '\t' + str(stats[0]) + '\t' + str(stats[1]) +'\t' + str(stats[2]) + '\t' + line[10] + '\n')

print 'Output file: ' + sys.argv[2] + '.psm'
print 'Output columns: PSM, score, PEP, qValue, hits'

output.close()
qvality_input.close()
mascot_input.close()