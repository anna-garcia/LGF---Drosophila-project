#!/usr/bin/python3

import sys
import pysam
from collections import defaultdict
from collections import Counter

bamfile = sys.argv[1]
outfile = 'mapping_reports'

bam = pysam.AlignmentFile(bamfile, "rb")

reads = []

for mapping in bam:
    if not mapping.is_unmapped:
        read_id = mapping.query_name
        reads.append(read_id)

uniquely_mapped = 0
read_mapping_count = Counter(reads)


with open(outfile, "w") as out:
    print('Read Id:','Mapping Count:',sep='\t',file=out)
    for a in sorted(read_mapping_count.items(), key=lambda x:x[1]):
        if a[1] == 1:
            uniquely_mapped +=1
        print(a[0], a[1], sep='\t',file=out)
    total = int(len(read_mapping_count))
    multimapped = int(len(read_mapping_count)-uniquely_mapped)
    print()
    print('Total Reads:',total, sep='\t',file=out)
    print('Uniquely mapped reads:',uniquely_mapped,'\t',(float(uniquely_mapped/total)*100), file=out)
    print('Multimapped reads:',multimapped,'\t',(1-(float(uniquely_mapped/total)))*100, file=out)