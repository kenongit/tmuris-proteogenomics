# Create reverse decoy of specified fasta file
# Accept files as command line arguments. Creates new .out file.

import sys

print(sys.argv[1]) + ' > ' + sys.argv[1] + '.decoy'

input = open(sys.argv[1], "r")
sequence = dict()
for line in input:
	if(line.startswith('>')):
		header = '>DECOY_' + line[1:]
		sequence[header] = ''
	else:
		sequence[header] += line.strip().upper()
input.close()

output = open(sys.argv[1] + ".decoy", "w")
for h in sequence.keys():
	reversed_peptide = (h + sequence[h][::-1])
	if '*' in reversed_peptide:
 		# Stop codon needs moving to the end of the sequence
 		decoy_peptide = reversed_peptide.replace('*', '') + '*' + '\n'
 	else:
 		decoy_peptide = reversed_peptide + '\n'
	output.write(decoy_peptide)
output.close()