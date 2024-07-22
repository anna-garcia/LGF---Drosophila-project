from collections import defaultdict
import pandas as pd
import sys

tabela = sys.argv[1]
dictionary = sys.argv[2]

df1 = pd.read_csv(tabela, sep='\t', header=0)
df2 = pd.read_csv(dictionary, sep='\t', header=0)


df = pd.merge(df1, df2, on='Superfamily')

df_raw = df.sort_values(['Class','Subclass/Order','Superfamily'], ascending=[True,True,True])
df_raw.to_csv("/home5/attilio/Anna_Garcia/Drosophila_teste/TEs/piRNAs/TEs_profiles/arizonae/raw_tables/te_ratio_ari_raw.tsv", sep='\t', index=False)

# df_raw['Y1_RPM'] = df_raw['Y1_RPM'].astype(float)

# data = df_raw[['Class','Subclass/Order','Superfamily','Y1_RPM','Y2_RPM']].groupby(['Class','Subclass/Order','Superfamily']).sum().reset_index()
# data.to_csv("/home5/attilio/Anna_Garcia/Drosophila_teste/TEs/piRNAs/TEs_profiles/mojavensis/te_ratio_dmoj_sum.tsv", sep='\t', index=False)