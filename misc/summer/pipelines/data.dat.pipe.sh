#! /bin/sh
# Send DATs into the dat.pipe.sh pipeline 

base_path="../mascot/"

./dat.pipe.sh adu f291555368 f291555369 p1
./dat.pipe.sh adu f291555370 f291555371 p2
./dat.pipe.sh adu f291555372 f291555373 p3
./dat.pipe.sh adu f291555389 f291555381 s1
./dat.pipe.sh adu f291555390 f291555383 s2
./dat.pipe.sh adu f291555392 f291555385 s3

./dat.pipe.sh emb f291555484 f291555362 p1
./dat.pipe.sh emb f291555486 f291555364 p2
./dat.pipe.sh emb f291555488 f291555366 p3
./dat.pipe.sh emb f291555356 f291555485 s1
./dat.pipe.sh emb f291555357 f291555487 s2
./dat.pipe.sh emb f291555359 f291555489 s3

./dat.pipe.sh fre f291555072 f291555073 p1
./dat.pipe.sh fre f291555079 f291555080 p2
./dat.pipe.sh fre f291555084 f291555085 p3
./dat.pipe.sh fre f291555093 f291555092 s1
./dat.pipe.sh fre f291555096 f291555095 s2
./dat.pipe.sh fre f291555099 f291555098 s3

./dat.pipe.sh sti f291554995 f291554996 p1
./dat.pipe.sh sti f291554997 f291554998 p2
./dat.pipe.sh sti f291555003 f291555002 p3
./dat.pipe.sh sti f291555110 f291555111 s1
./dat.pipe.sh sti f291555113 f291555114 s2
./dat.pipe.sh sti f291555115 f291555116 s3

# Combine <1% local FDR PSMs by Trinity protein from all biological repeats (supernatant + pellet) for each tissue.
awk '!array[$1]++' ${base_path}psm/psm_by_trinity/adu.*.psm > ${base_path}psm/psm_by_trinity/combined/adu.trinity.combined.psm
awk '!array[$1]++' ${base_path}psm/psm_by_trinity/emb.*.psm > ${base_path}psm/psm_by_trinity/combined/emb.trinity.combined.psm
awk '!array[$1]++' ${base_path}psm/psm_by_trinity/fre.*.psm > ${base_path}psm/psm_by_trinity/combined/fre.trinity.combined.psm
awk '!array[$1]++' ${base_path}psm/psm_by_trinity/sti.*.psm > ${base_path}psm/psm_by_trinity/combined/sti.trinity.combined.psm

# As above, but by PSM peptide
awk '!array[$1]++' ${base_path}psm/filtered_qvalue_unique/adu.*.psm > ${base_path}psm/filtered_qvalue_unique/combined/adu.psm.combined.psm
awk '!array[$1]++' ${base_path}psm/filtered_qvalue_unique/emb.*.psm > ${base_path}psm/filtered_qvalue_unique/combined/emb.psm.combined.psm
awk '!array[$1]++' ${base_path}psm/filtered_qvalue_unique/fre.*.psm > ${base_path}psm/filtered_qvalue_unique/combined/fre.psm.combined.psm
awk '!array[$1]++' ${base_path}psm/filtered_qvalue_unique/sti.*.psm > ${base_path}psm/filtered_qvalue_unique/combined/sti.psm.combined.psm
