Commands used to prepare uniprot for blasting Trinity best_candidate exons
scripts/splitfasta.pl -s 100 best_candidates/adult.best_candidates.pep.out
scripts/splitfasta.pl -s 100 best_candidates/embryo.best_candidates.pep.out
scripts/splitfasta.pl -s 100 best_candidates/frear.best_candidates.pep.out
scripts/splitfasta.pl -s 100 best_candidates/stichosome.best_candidates.pep.out

Kadmon, run from /home/mfbx9bc4/scratch/uniref/:
/home/mfbx9bc4/bin/ncbi-blast-2.2.27+/bin/makeblastdb -in uniref50.fasta -dbtype prot -title uniref50 -parse_seqids -hash_index -out uniref50
Building a new DB, current time: 02/09/2013 14:06:03
New DB name:   uniref50
New DB title:  uniref50
Sequence type: Protein
Keep Linkouts: T
Keep MBits: T
Maximum file size: 1000000000B
Adding sequences from FASTA; added 6412887 sequences in 551.598 seconds.

Find diff file types in dir:
find -type f -name '*.*' | sed 's|.*\.||' | sort -u

11th Jan
python createJobsFastaBlastp.py ~/scratch/best_candidates/test/ adult.best_candidates.pep.out_o 1357 .fa ~/scratch/jobs/
qsub ../jobs/adult.best_candidates.pep.out_o1.fa.job.sh