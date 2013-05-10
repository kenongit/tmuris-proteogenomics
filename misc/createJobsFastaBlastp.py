# Create blastp jobscripts from split Trinity best_candidate CDSs
# USAGE python createJobsFastaBlastp.py <fasta_fasta_path> <filename_prefix> <n_files> <filename_suffix> <jobs_path>
# EG python createJobsFastaBlastp.py ~/scratch/best_candidates/test/ adult.best_candidates.pep.out_o 1357 .fa ~/scratch/jobs/
# EG python createJobsFastaBlastp.py ~/scratch/best_candidates/test/ adult.best_candidates.pep.out_o 1357 .fa ~/scratch/jobs/
# while true; do qstat; date; sleep 60; done
# python ../scripts/createJobsFastaBlastp.py ~/scratch/best_candidates/test/ adult.best_candidates.pep.out_o 5 .fa ~/scratch/jobs/parallelbench/
# python createJobsFastaBlastpSerial.py ~/scratch/best_candidates/test/ adult.best_candidates.pep.out_o 5 .fa ~/scratch/jobs/serialbench/

import sys

fasta_path = sys.argv[1]
prefix = sys.argv[2]
pieces = int(sys.argv[3])
suffix = sys.argv[4]
jobs_path = sys.argv[5]


blastdb = '~/scratch/uniref/uniref50'
threads = 4

for piece in range(1, 2):
	
	query_filename = prefix + str(piece) + suffix
	out_filename = query_filename + '.out'
	jobscript_filename = prefix + str(piece) + suffix + '.job.sh'

	jobscript = open(fasta_path + jobscript_filename, 'w+')
	jobscript_contents = """
		#!/bin/bash
		# -cwd
		# -V
		# -pe smp.pe {threads}
		~/bin/ncbi-blast-2.2.27+/bin/blastp -outfmt 7 -max_target_seqs 5 -num_threads {threads} -db {blastdb} -query {fasta_path}{query_filename} -out {fasta_path}{out_filename}
		""".format(threads=threads, blastdb=blastdb, fasta_path=fasta_path, query_filename=query_filename, out_filename=out_filename)
	#print jobscript_contents
	jobscript.write(jobscript_contents)



# input.close()
# output.close()