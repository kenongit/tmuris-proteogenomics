#!/usr/bin/python

import sys

# Nematoda (and Trematoda) species in which we're interested
sought_after_substrings = [
	'Loa loa',
	'Meloidogyne',
	'Caenor',
	'Trichin',
	'Trichur',
	'Trichiu',
	'Ascaris', 
	'Wucherer',
	'Chromador',
	'Schistosom', # Trematode
	'Brugia',
	'Clonorchis', #Trematode
	'Onchocercid',
	'Pristionchus',
	'Nematod',
	'Angiostrong'
	]

in_file = open(sys.argv[1], 'r')

for line in in_file:
	for substring in sought_after_substrings:
		if substring in line:
			print line.strip()