#!/usr/bin/python3

#The output file is a read id list. These reads have rRNA as a feature.

import sys
import pysam
from collections import defaultdict
from collections import Counter


fc_file = sys.argv[1]
rRNAs_file = sys.argv[2]


fc = pysam.AlignmentFile(fc_file, "rb")
outfile = "rRNA_reads.txt"

rRNA_genes = []
rRNA_fc = []


for line in open(rRNAs_file):
    rRNA_genes.append(line.strip())


for mapping in fc:
    if not mapping.is_unmapped:
        read_id = mapping.query_name
        read_tag = mapping.tags
        if len(read_tag) == 7:
            tag = read_tag[-1]
            if tag[1] in rRNA_genes:
                rRNA_fc.append(read_id)

rRNA_reads = list(set(rRNA_fc))

with open(outfile, "w") as out:
    for a in rRNA_reads:
        print(a, file=out)