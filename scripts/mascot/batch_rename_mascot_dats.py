#!/usr/bin/python
# Batch rename MASCOT .dat files including the relevant database name (line 30 'DB=') and source spectra file (line 34 'FILE=')
# Uses forward slashes - won't work on Windows
# Overwrite safe - adds underscores to duplicates
# USAGE: batch_rename_mascot_dats.py /path/to/directory/

import os
import sys
import fnmatch

path = sys.argv[1]

for file_name in os.listdir(sys.argv[1]):
	if fnmatch.fnmatch(file_name, '*.dat'):
		dat_file = open(path + '/' + file_name, 'r')
		
		for i in range(1, 50):
			line = dat_file.readline()
			if line.startswith('DB='):
				database_name = line[3:].strip()
			elif line.startswith('FILE='):
				spectra_file_path = line[5:].strip()
				spectra_file_name = spectra_file_path.split('\\')[-1]

		dat_file.close()
		
		new_file_name = database_name + '-' + spectra_file_name + '.dat'
		
		while os.path.exists(path + '/' + new_file_name):
			new_file_name = new_file_name[:-4] + '_' + '.dat'
		
		os.rename(path + '/' + file_name, path + '/' + new_file_name)
		print file_name + ' renamed to ' + new_file_name

			
		