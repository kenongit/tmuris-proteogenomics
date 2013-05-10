#! /bin/sh

python /Users/bede/Scripts/rangeFilterStats.py /Users/bede/Data/adult/adult.blastx_trinity_augustus.fasta.stats 1e-30 50 80 0.5 length,0,3000,100
mv /Users/bede/Data/adult/adult.blastx_trinity_augustus.fasta.stats.range /Users/bede/Data/adult/adult.blastx_trinity_augustus.range.length

python /Users/bede/Scripts/rangeFilterStats.py /Users/bede/Data/adult/adult.blastx_trinity_augustus.fasta.stats 1e-30 50 80 0.5 expected,1e-180,1,100000000000000000000
mv /Users/bede/Data/adult/adult.blastx_trinity_augustus.fasta.stats.range /Users/bede/Data/adult/adult.blastx_trinity_augustus.range.expected

python /Users/bede/Scripts/rangeFilterStats.py /Users/bede/Data/adult/adult.blastx_trinity_augustus.fasta.stats 1e-30 50 80 0.5 identity,0,105,5
mv /Users/bede/Data/adult/adult.blastx_trinity_augustus.fasta.stats.range /Users/bede/Data/adult/adult.blastx_trinity_augustus.range.identity.1
python /Users/bede/Scripts/rangeFilterStats.py /Users/bede/Data/adult/adult.blastx_trinity_augustus.fasta.stats 1e-30 50 80 0.5 identity,91,99,1
mv /Users/bede/Data/adult/adult.blastx_trinity_augustus.fasta.stats.range /Users/bede/Data/adult/adult.blastx_trinity_augustus.range.identity.2
python /Users/bede/Scripts/rangeFilterStats.py /Users/bede/Data/adult/adult.blastx_trinity_augustus.fasta.stats 1e-30 50 80 0.5 identity,99.5,99.9,0.1
mv /Users/bede/Data/adult/adult.blastx_trinity_augustus.fasta.stats.range /Users/bede/Data/adult/adult.blastx_trinity_augustus.range.identity.3

python /Users/bede/Scripts/rangeFilterStats.py /Users/bede/Data/adult/adult.blastx_trinity_augustus.fasta.stats 1e-30 50 80 0.5 queryCoverage,0,1.1,0.1
mv /Users/bede/Data/adult/adult.blastx_trinity_augustus.fasta.stats.range /Users/bede/Data/adult/adult.blastx_trinity_augustus.range.queryCoverage