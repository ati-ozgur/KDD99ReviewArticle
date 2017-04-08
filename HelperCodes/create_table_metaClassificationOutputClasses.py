# create_table_metaClassificationOutputClasses.py
import ReviewHelper
import pandas as pd

df = ReviewHelper.get_pandas_data_frame_created_from_bibtex_file()

count_nobinary = df[df.metaClassificationOutputClasses.str.contains("NoBinary")].ID.count()
count_binary = df[df.metaClassificationOutputClasses.str.contains("Binary")].ID.count()
count_Multi5General = df[df.metaClassificationOutputClasses.str.contains("Multi5General")].ID.count()
count_Multi23General = df[df.metaClassificationOutputClasses.str.contains("Multi23General")].ID.count()
count_MultiIndividual = df[df.metaClassificationOutputClasses.str.contains("Individual")].ID.count()


table_string = """ 
\\begin{{table}}[!ht]
    \centering 
    \caption{{ \\textbf{{Comparison of the published studied based on classification output classes}}. Experiments in articles may have more than one output class such as Binary and Multiclass 5; therefore total article count in this table is more than \\totalNumberOfArticles}}
    \label{{table-metaClassificationOutputClasses}}

\\begin{{tabular}}{{@{{}}p{{0.9\columnwidth}}p{{0.1\columnwidth}}@{{}}}}

\\toprule

Classification Output                  & Article Count      \\\\

\midrule

Binary (Attack/Normal)                  & {REPLACE_BINARY}        \\\\
Multiclass 5 (DOS/Probe/U2R/R2L/Normal) & {REPLACE_Multi5General}  \\\\
Multiclass 23 (22 attacks/Normal)       & {REPLACE_Multi23General} \\\\
No Binary: Gives other result           & {REPLACE_NOBINARY}       \\\\
Multi Class X (Subset of 23)            & {REPLACE_INDIVIDUAL}     \\\\

\\bottomrule

\end{{tabular}}


\end{{table}}
""".format(REPLACE_NOBINARY=count_nobinary
    ,REPLACE_BINARY=count_binary
    ,REPLACE_Multi5General=count_Multi5General
    ,REPLACE_Multi23General=count_Multi23General
    ,REPLACE_INDIVIDUAL=count_MultiIndividual
    )

filename = "../latex/table-metaClassificationOutputClasses.tex"
target = open(filename, 'w')
target.write(table_string)
target.close()
