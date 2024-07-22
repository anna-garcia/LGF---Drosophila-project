## THIS SCRIPT CREATE A COUNT PROFILE.
## MEANING: IT WILL COUNT SMALL RNAS THAT MAPPED IN TRANSPOSONS SUPERFAMILIES AND GENERATE A TABLE FOR IT.

import sys
from collections import defaultdict
# inform the scale factor before running this script.
# scale factor = (10^6/total mapped reads)
# Beware of filtration steps (e.g. excluding rRNAs). This may change the valor.
scale_factor = float(0.07160609829)
# tab_count is the featureCounts file in which counts reads mapped per feature.
# It needs formating to exclude the header and inert a column separator pattern.
# (awk '{OFS = "\t"}{if($0~"^Motif"){print $0}}' y1.repbase.fc > y1.repbase.fc.tsv)
tab_count = sys.argv[1]
# tab_out is the Repeatmasker.out file. 
# However, it needs formating since it does not have a column separator pattern.
# A simple awk script can fix this issue.
# (awk '{OFS="\t"}{print $0}' [file.out] > tab_separated_file.tsv)
tab_out_repeatmasker = sys.argv[2]

TEs_count = defaultdict(list)
TEs_family_dict_raw = defaultdict(list)
outfile = "piRNAs_TEs_ratio.tsv"

for line in open(tab_out_repeatmasker, "r"):
    a = line.strip().split()
    TEs_family_dict_raw[a[9]].append(a[10])

for line in open(tab_count,"r"):
    columns = line.strip().split('\t')
    motif = (columns[0].split(':'))[1]
    count = float(columns[-1])
    TEs_count[motif].append(count)

TEs_family_dict = {k: set(v) for k, v in TEs_family_dict_raw.items()}

with open(outfile, "w") as out:
    print("TE ID","RPM","Superfamily",sep='\t',file=out)
    for k,v in sorted(TEs_count.items(), key=lambda x:x[0]):
        family = str(TEs_family_dict.get(k)).strip('{}').replace("'","")
        print(k,float(sum(v)*scale_factor),family,sep='\t',file=out)