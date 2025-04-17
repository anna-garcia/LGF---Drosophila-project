#!/usr/bin/python3

import pysam
from collections import defaultdict
import sys

file_in =  sys.argv[1]

lengths = defaultdict(int)
seen = set()

bam = pysam.AlignmentFile(file_in)

for mapping in bam:
    if not mapping.is_unmapped and mapping.query_name not in seen:
        lengths[mapping.query_length] += 1
        seen.add(mapping.query_name)

for i in sorted(lengths):
    print(i, lengths[i], sep="\t")
