#!/usr/bin/python
# Count PSMs inside file(s) containing lists of protein names and their corresponding PSMs
# USAGE count_corresponding_psms.py <source_files> 

import sys

psms_total = []
for file_name in sys.argv[1:]:

	source_file = open(file_name, 'r')
	
	psms_file = []
	for line in source_file:
		psms_line = line.split('	')[1].split(',')
		psms_file.extend(psms_line)
		psms_total.extend(psms_line)
	
	source_file.close()
	
	print file_name.split('/')[-1] + ': ' + str(len(psms_file)) + ' PSMs ' + 'of which ' + str(len(set(psms_file))) + ' are unique'

print str(len(psms_total)) + ' PSMs counted in ' + str(len(sys.argv[1:])) + ' file(s), of which ' + str(len(set(psms_total))) + ' are unique'
