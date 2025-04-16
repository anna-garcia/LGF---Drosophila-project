#!/bin/bash

mapping_files=`ls ./*.bam`

for bamfile in $mapping_files
do
    basename=$(basename $bamfile)
    output={$basename}.unique.bam
    awk '{{if($0~"@"){print $0}else{if($2!="4" && $15=="XM:i:1"){print $0}}}}' <(samtools view -h $bamfile) |
    samtools view -Sb &&
    samtools index $output
done
