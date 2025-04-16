#!/bin/bash

set -euo pipefail

# inputs
bamfile=$1
sf_file="/data/analysis/carol/drosophila/Drosophila_snakemake/parental/results/mapping/scalefactor.tsv"
outdir="/data/analysis/carol/drosophila/Drosophila_snakemake/parental/results/mapping/bam_cov_anna"

# outputs
basename=$(basename $bamfile)
prefix=${basename%.*}

sense="$outdir/${prefix}.sense.bw"
antisense="$outdir/${prefix}.antisense.bw"

## Get Scale Factor
sample=""
if [[ $basename =~ vs ]]; then
    sample=$(echo $basename | awk '{split($0,x,"."); print x[1]}')
    sf=$(grep $sample $sf_file | cut -f 2)
else
    sf=$(grep $prefix $sf_file | cut -f 2)
fi

echo "$basename , $sf"
## Generating sense coverage:

params="--samFlagInclude 0 -bs 10 -p 8 --scaleFactor $sf"
bamCoverage -b $bamfile $params -o $sense 

## Generating antisense coverage:

params="--samFlagInclude 16 -bs 10 -p 8 --scaleFactor $sf"
bamCoverage -b $bamfile $params -o $antisense 
