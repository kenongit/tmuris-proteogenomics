#!/usr/bin/python
# Correctly counts PSMs inside file(s) containing lists of PSMs as the first column
# Also counts unique PSMs and generates summary count statistics
# USAGE count_psms.py <source_files> 

import sys

psms_total = []
for file_name in sys.argv[1:]:

	source_file = open(file_name, 'r')
	
	psms_file = []
	for line in source_file:
		psms_file.append(line.split('	')[0])
		psms_total.append(line.split('	')[0])
	
	source_file.close()
	
	print file_name.split('/')[-1] + ': ' + str(len(psms_file)) + ' PSMs ' + 'of which ' + str(len(set(psms_file))) + ' are unique'

print str(len(psms_total)) + ' PSMs counted in ' + str(len(sys.argv[1:])) + ' files, of which ' + str(len(set(psms_total))) + ' are unique'
