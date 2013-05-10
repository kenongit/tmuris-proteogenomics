# Prefixes and suffixes fasta headers to create uniquity
# Accept files as command line arguments. Creates new .out file.

import sys

tissue_prefix = 'STI'
tissue_full = 'stichosome'

# Iterate through command line arguments
for n in sys.argv[1:]:
	print(n) + ' > ' + n + '.out'
	input = open(n, "r")
	output = open(n + ".out", "w")
	
	# Iterate through lines
	for line in input:
		if line.startswith('>')):
			header = '>' + tissue_prefix + line[1:].rstrip("\n\r") + ' ~' + tissue_full + '\n'
			output.write(header)
		else:
			output.write(line)

	input.close()
	output.close()