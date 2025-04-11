#!/usr/bin/python3

## Creating a basic mapping statistical report and a table informing
## how many times each mapped read had

import sys
import fileinput
from collections import defaultdict

sample = sys.argv[1]
file = sys.argv[2]

outfile1 = "/data/analysis/carol/drosophila/Drosophila_snakemake/parental/results/mapping/stats/"+str(sample)+"_mult_map.tsv"
outfile2 = "/data/analysis/carol/drosophila/Drosophila_snakemake/parental/results/mapping/stats/"+str(sample)+"_stats.tsv"

unmapped = 0
uniq = 0
mult = 0

res = defaultdict(int)

with open(outfile1, "w") as out1:
    print("Read_ID","Mapping_Count",sep="\t", file=out1)
    for line in fileinput.input(file):
        cols = line.strip().split("\t")
        if cols[2] != "*":
            res[cols[0]] += 1
        else:
            unmapped +=1
    for i in res:
        if res[i] == 1:
            uniq += 1
        else:
            mult += 1
        print(i, res[i], sep="\t",file=out1)
    out1.close()

all = unmapped + uniq + mult

total_mapped = uniq + mult


with open(outfile2, "w") as out2:
    print('Total reads:',all, sep='\t',file=out2)
    print('Unmapped reads:',unmapped,(float(unmapped/all)*100),sep="\t", file=out2)
    print('Total mapped reads:', total_mapped,(float(total_mapped/all)*100),sep="\t",file=out2)
    print('Uniquely mapped reads:',uniq,(float(uniq/total_mapped)*100), sep="\t", file=out2)
    print('Multimapped reads:',mult,(float(mult/total_mapped)*100),sep="\t", file=out2)
    out2.close()
