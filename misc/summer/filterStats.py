# Output rows of alignmentStats.py processed blastx output with filtering ability
# USAGE: filterStats.py <maxExpected> <minLengthAminoAcids> <minIdentity> <minQueryCoverage>
# Empty filter values should be substitued with 'x'

import sys

# Usage instructions
if(len(sys.argv) == 1):
	sys.exit(
		'USAGE: filterStats.py <filename> <maxExpected> <minLengthAminoAcids> <minIdentity> <minQueryCoverage>\n' +
		'Empty filter values should be substitued with \'x\'')

input = open(sys.argv[1], "r")

# Init filter vars from args
if(sys.argv[2] != 'x'): maxExpected =  float(sys.argv[2])
else: maxExpected = False
if(sys.argv[3] != 'x'): minLength = float(sys.argv[3])
else: minLength = False
if(sys.argv[4] != 'x'): minIdentity = float(sys.argv[4])
else: minIdentity = False
if(sys.argv[5] != 'x'): minQueryCoverage = float(sys.argv[5])
else: minQueryCoverage = False

# Output lines with filtering
for line in input:
	lineContents = line.split()
	if line.startswith('comp'):
		if(maxExpected):
			if(float(lineContents[10]) >= maxExpected):
				continue
		if(minLength):
			if(float(lineContents[3]) <= minLength):
				continue
		if(minIdentity):
			if(float(lineContents[2]) <= minIdentity):
				continue
		if(minQueryCoverage):
			if(float(lineContents[12]) <= minQueryCoverage):
				continue
		# All filter conditions passed
		print line.strip()

input.close()