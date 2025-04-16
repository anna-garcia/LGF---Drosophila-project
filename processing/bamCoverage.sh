#!/bin/bash

# listing mapping files folder:

mapping_files=`ls ../*.bam`

for bamfile in $mapping_files
do
    # inputs:
    basename=$(basename $bamfile)
    prefix=${basename%.*}

    sf_file="/data/analysis/carol/drosophila/Drosophila_snakemake/parental/results/mapping/scalefactor.tsv"
    outdir="/data/analysis/carol/drosophila/Drosophila_snakemake/parental/results/mapping/bam_cov_anna"

    # outputs:

    sense="$outdir/${prefix}.sense.bw"
    antisense="$outdir/${prefix}.antisense.bw"

    ## Getiing Scale Factor:

    sample=""

    sample=$(echo $basename | awk '{split($0,x,"."); print x[1]}')
    sf=$(grep $sample $sf_file | cut -f 2)

    echo "$basename , $prefix , $sample ,  $sf"
    ## Generating sense coverage:

    params="--samFlagInclude 0 -bs 10 -p 8 --scaleFactor $sf"
    bamCoverage -b $bamfile $params -o $sense

    ## Generating antisense coverage:

    params="--samFlagInclude 16 -bs 10 -p 8 --scaleFactor $sf"
    bamCoverage -b $bamfile $params -o $antisense

    echo "DONE $bamfile !!!"
done

echo "DONE FULL FOLDER"
