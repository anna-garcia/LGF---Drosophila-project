#!/usr/bin/python3

import sys
import pysam
from collections import defaultdict
from collections import Counter

mapping_file = sys.argv[1]
map = pysam.AlignmentFile(mapping_file, "rb")
outfile = "histogram.tsv"

reads_size = []

seen = set()

for mapping in map:
    if mapping.query_name not in seen:
        seen.add(mapping.query_name)
        reads_size.append(len(mapping.query_sequence))

final=Counter(reads_size)

with open(outfile, "w") as out:
    print("Read Length","Count", sep='\t',file=out)
    for k,v in sorted(final.items(), key=lambda x:x[0]):
        print(k,v,sep='\t',file=out)