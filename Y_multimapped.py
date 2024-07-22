#!/usr/bin/python3


import sys
import pysam
from collections import defaultdict


bamfile = sys.argv[1]
Y_scaffolds_file = sys.argv[2]

Y_scaffolds = []

for line in open(Y_scaffolds_file):
    Y_scaffolds.append(line.strip())


bam = pysam.AlignmentFile(bamfile, "rb")
All_mappings = defaultdict(list)

for mapping in bam:
    if not mapping.is_unmapped:
        read_id = mapping.query_name
        All_mappings[read_id].append(mapping.reference_name)


print("Read ID", "Mapping_Count", sep="\t")
for k,v in All_mappings.items():
    flag = all(item in Y_scaffolds for item in v)
    if flag == True:
        print(k, int(len(v)), sep="\t")