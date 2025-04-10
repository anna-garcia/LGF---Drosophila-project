#!/usr/bin/python3

## removal of rRNA AND low complexity reads

import sys
from Bio import SeqIO
import pysam # type: ignore
import subprocess as sp

bam_file = sys.argv[1]

bam = pysam.AlignmentFile(bam_file, "rb")

for mapping in bam:
    if mapping.is_unmapped:
        read_id = mapping.query_name
        sequence = mapping.query_sequence
        quality = mapping.qual
        # print(read_id,quality,sep="\n")
        A = 0
        T = 0
        length = int(len(sequence))
        for i in sequence:
            if i == 'A':
                A +=1
            elif i == 'T':
                T +=1
        AT = A+T
        if float(AT/length) <= 0.75:
            print("@"+read_id,sequence,"+",quality,sep="\n")
