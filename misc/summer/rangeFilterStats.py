# Filter alignmentStats.py processed blastx output across a range of filter values
# The bounds of the range and the increment size can be specified
# Outputs number of hits (lines) to a text file for each filter value processed
# Empty arguments should be substitued with 'x'
# For expected values, the increment is geometric. Use smaller value first.

import sys

def die():
	sys.exit(
		'USAGE: filterStats.py <filename> <maxExpected> <minLengthAminoAcids> <minIdentity> <minQueryCoverage> <{filterType},min,max,increment>\n'
		'EG: filterStats.py foo.txt 1e-30 50 50 0.5 length,10,50,1'
		'EG:filterStats.py foo.txt 1e-30 50 50 0.5 expected,1e-180,1,100000000000000000000'
		'Empty filter values should be substitued with \'x\''
		'For expected values, the increment is geometric')


# Catch empty args
if(len(sys.argv) == 1):
	die()

# Init filter vars from args
if(sys.argv[2] != 'x'): maxExpected = float(sys.argv[2])
else: maxExpected = False
if(sys.argv[3] != 'x'): minLength = float(sys.argv[3])
else: minLength = False
if(sys.argv[4] != 'x'): minIdentity = float(sys.argv[4])
else: minIdentity = False
if(sys.argv[5] != 'x'): minQueryCoverage = float(sys.argv[5])
else: minQueryCoverage = False

# Filter range info
rangeInfo = sys.argv[6].split(',')
rangeType = rangeInfo[0]
rangeMin = float(rangeInfo[1])
rangeMax = float(rangeInfo[2])
rangeIncrement = float(rangeInfo[3])

# Empty the output file
open(sys.argv[1] + ".range", 'w').close()

# Iterate over range of filter values
rangeTracker = rangeMin
while(rangeTracker <= rangeMax):
	
	# Set the ranged variable as specified by user 
	if(rangeType == 'expected'): maxExpected = rangeTracker
	elif(rangeType == 'length'): minLength = rangeTracker
	elif(rangeType == 'identity'): minIdentity = rangeTracker
	elif(rangeType == 'queryCoverage'): minQueryCoverage = rangeTracker
	else: die()

	# Open I/O
	input = open(sys.argv[1], "r")
	output = open(sys.argv[1] + ".range", "a")

	# Iterate over lines in file 
	hitTracker = 0
	for line in input:
		lineContents = line.split()
		if(line.startswith('comp')):
			if(maxExpected):
				if(float(lineContents[10]) >= maxExpected):
					# print 'Expectation ' + lineContents[10] + ' filtered'
					continue
			if(minLength):
				if(float(lineContents[3]) <= minLength):
					# print 'Length ' + lineContents[3] + ' filtered'
					continue
			if(minIdentity):
				if(float(lineContents[2]) <= minIdentity):
					# print 'Identity ' + lineContents[2] + ' filtered'
					continue
			if(minQueryCoverage):
				if(float(lineContents[12]) <= minQueryCoverage):
					# print 'Query Coverage ' + lineContents[12] + ' filtered'
					continue
			# All filter conditions passed
			hitTracker += 1
		
	# Ensure correct inequality is used
	if(rangeType == 'expected'):
		output.write(rangeType + '	<	' + str(rangeTracker) + '	' + str(hitTracker) + '\n')
	else:
		output.write(rangeType + '	>	' + str(rangeTracker) + '	' + str(hitTracker) + '\n')

	input.close()
	output.close()

	# Treat increments as geometric for expectation values
	if(rangeType == 'expected'):
		rangeTracker *= rangeIncrement
	else:
		rangeTracker += rangeIncrement

print(sys.argv[1] + ' --> ' + sys.argv[1] + '.range')