# Test to see if a list of genes is present in a sample  
# USAGE: python testCoreGenes.py <reference> <sample>

import sys

reference = open(sys.argv[1], "r")
sample = open(sys.argv[2], "r")
sampleContents = sample.read()

lineCounter = 0
hitCounter = 0
for line in reference:
	if(line in sampleContents):
		hitCounter += 1
	lineCounter += 1

print str(hitCounter) + ' / ' + str(lineCounter) + ' genes matched'