# Merge PSMs with their Mascot, PEP and q value scores when given parsed MASCOT output and qvality output
# Remove headers from input files before use
# USAGE: python outputScoredPSMs.py <parsed_mascot_output> <qvality_output>

import sys
import re

mascotInput = open(sys.argv[1], 'r')
qvalityInput = open(sys.argv[2], 'r')
output = open(sys.argv[2] + '.psm', 'w')

for line in mascotInput:
	line = re.sub('[ \t]+' , ' ', line) # Normalise column spacing before splitting
	line = line.strip('\n').split(' ')
	stats = qvalityInput.readline().strip('\n').split('	')
	output.write(line[8] + '\t' + str(stats[0]) + '\t' + str(stats[1]) +'\t' + str(stats[2]) + '\t' + line[10] + '\n')

print 'Output file: ' + sys.argv[2] + '.psm'
print 'Output columns: PSM, score, PEP, qValue, hits'

output.close()
qvalityInput.close()
mascotInput.close()