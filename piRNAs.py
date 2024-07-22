## Importing Libraries:
import pysam
import sys
import pandas as pd
import csv
from collections import defaultdict


## Calling files from terminal:
featurecounts_bam_file= sys.argv[1]
transposons_only = sys.argv[2]


## Opening files:
bam = pysam.AlignmentFile(featurecounts_bam_file, "rb")
TEs = pd.read_csv(transposons_only, sep='\t', header=0)


#Partial caracterization of piRNAs: size selection and mapped in repeats regions
partial_piRNAs = defaultdict(list)
piRNas_size = defaultdict(list)

for mapping in bam:
    if mapping.query_name:
        read_tag = mapping.tags
        if len(mapping.query_sequence) >= 25 and len(read_tag) == 7:
            length = int(len(mapping.query_sequence))
            repeats = read_tag[-1]
            motifs = repeats[-1].split(",")
            for b in motifs:
                a = b.split(":")[1]
            partial_piRNAs[mapping.query_name].append(a)
            piRNas_size[mapping.query_name].append(length)

partial_piRNAs = {k: set(v) for k, v in partial_piRNAs.items()}
piRNas_size = {k: set(v) for k, v in piRNas_size.items()}


## Filtrating raw piRNAs: Keep reads that mapped ONLY in TEs regions
dictionary = TEs['Repeat_ID_ari'].to_list()

print("Read ID","Read Length","TEs list", sep="\t")
for k,v in partial_piRNAs.items():
    flag = all(item in dictionary for item in v)
    if flag == True:
        transposon = str(v).strip('{}').replace("'","")
        size = str(piRNas_size.get(k)).strip('{}').replace("'","")
        print(k, size, transposon, sep="\t")