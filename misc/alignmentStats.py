# Shortlist alignments from a blastx output file (using blastx flag '-outfmt 7')
# > Append query coverage and hit order statistics to each line of output file 
# > Cull alignments to only the best n matches per query
# > Output a simple distribution of E values

from __future__ import division
import sys

input = open(sys.argv[1], "r")
output = open(sys.argv[1] + ".stats", "w")

nHitsPerQuery = 1

# Flow control vars
isNewQuery = True
queryLength = 0
queryHitCounter = 1

# Print column headers
output.write('Columns: query id, subject id, % identity, alignment length (aa), mismatches, gap opens, q. start (nuc), q. end (nuc), s. start, s. end, e-value, bit score, query coverage, hit class \n')

# Probablility distribution vars
probDist = {}
rangeMax = 100
rangeMin = 0.000000000000000000000000000000000000000000000000000000001
separationFactor = 10000
rangeTracker = rangeMin
rangeCounter = 1

# Build probability distribution skeleton
while(rangeTracker < rangeMax):
	probDist[rangeTracker] = {'max':rangeTracker, 'min':rangeTracker / separationFactor, 'count':0}
	# Determine values either side of specified range
	if(rangeTracker == rangeMin):
		probDist['BENEATH RANGE'] = {'max':rangeTracker / separationFactor, 'min':0, 'count':0}
	elif(rangeTracker * separationFactor > rangeMax):
		probDist['ABOVE RANGE'] = {'max':100000000000000000000, 'min':rangeTracker, 'count':0}
	rangeTracker *= separationFactor
	rangeCounter += 1

for line in input:
	if(line.startswith('# Query')):
		queryInfo = line.strip().split(' ')
		queryLength = int(''.join(i for i in queryInfo[3] if i.isdigit())) # Hackily extract length integer from string (avoiding regex)

	elif(line.startswith('comp') and (isNewQuery or queryHitCounter < nHitsPerQuery)):
		lineContents = line.strip().split('	')
		# Calculate query coverage from start/end values, ensuring start value is lower than end value
		queryStart = int(lineContents[6])
		queryEnd = int(lineContents[7])
		hitQueryCoverage = abs(float((queryEnd - queryStart + 1) / queryLength))
		# Calculate subject coverage - buggy - needs subjectLength value, not queryLength
		# subjectStart = int(lineContents[8])
		# subjectEnd = int(lineContents[9])
		# hitSubjectCoverage = float((subjectEnd - subjectStart + 1) / queryLength)
		# Fill probability distribution with frequencies
		for key in probDist:
			if(probDist[key]['min'] < float(lineContents[10]) <  probDist[key]['max']):
				probDist[key]['count'] += 1
		if(isNewQuery):
			isNewQuery = False
			queryHitCounter = 1
		else:
			queryHitCounter += 1
		
		# output.write('	'.join(lineContents) + '\t' + str("{0:.3f}".format(hitQueryCoverage)) + '\t' + str("{0:.3f}".format(hitSubjectCoverage)) + '\t' + str(queryHitCounter) + '\n')
		output.write('	'.join(lineContents) + '\t' + str("{0:.3f}".format(hitQueryCoverage)) + '\t' + str(queryHitCounter) + '\n')
	
	else:
		isNewQuery = True

# Output probability distribution as sorted list
for key in sorted(probDist.iterkeys()):
    print key, probDist[key]

input.close()
output.close()