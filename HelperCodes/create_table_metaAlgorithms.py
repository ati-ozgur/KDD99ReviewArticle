# create_table_metaAlgorithms.py

import ReviewHelper
import pandas as pd

df = ReviewHelper.get_pandas_data_frame_created_from_bibtex_file()


list1 = df.metaAlgorithms.str.split(",").tolist()

#strip_list = [map(str.strip, inner_list) for inner_list in list1]


df1 = pd.DataFrame(list1)

for i in range(df1.columns.size):
    df1[i] = df1[i].str.strip()
    df1[i] = df1[i].str.lower()

stacked = df1.stack()


stacked_value_counts = stacked.value_counts()
greater_than = stacked_value_counts[stacked_value_counts > 2]

table_content_inside=""

for algorithm_name in greater_than.index:
    algorithm_count = greater_than[algorithm_name]

    line = "{algorithm_name} & {algorithm_count} \\\\ \n".format(
        algorithm_name = algorithm_name
        ,algorithm_count = algorithm_count
    )
    table_content_inside = table_content_inside + line




table_content_start = """
\\begin{table}[!ht]
\\centering 
    \\caption{ \\textbf{Most used Algorithms in Proposed Methods}. }
    \\label{table-metaAlgorithms}

\\begin{tabular}{@{}p{0.75\\columnwidth}p{0.1\\columnwidth}@{}}

\\toprule

\\textbf{Name} & \\textbf{Article Count} \\\\

\\midrule

"""


table_content_end = """
\\bottomrule

\\end{tabular}

\\end{table}

"""

table_content_full = table_content_start + table_content_inside + table_content_end

#print table_content_full

filename = "../latex/table-metaAlgorithms.tex"
target = open(filename, 'w')
target.write(table_content_full)
target.close()
