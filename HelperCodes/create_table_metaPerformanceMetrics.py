#create_table_metaPerformanceMetrics.py


import ReviewHelper
import pandas as pd

df = ReviewHelper.get_pandas_data_frame_created_from_bibtex_file()

# find problematic ones
df[df.metaPerformanceMetrics.isnull()]

list1 = df.metaPerformanceMetrics.str.split(",").tolist()

df1 = pd.DataFrame(list1)

for i in range(df1.columns.size):
    df1[i] = df1[i].str.strip()

stacked = df1.stack()


stacked_value_counts = stacked.value_counts()


#print stacked_value_counts

greater_than = stacked_value_counts[stacked_value_counts > 3]

table_content_inside=""

for performance_metric_name in greater_than.index:
    performance_metric_count = greater_than[performance_metric_name]
    performance_metric_name_in_table = performance_metric_name

    if(performance_metric_name == "None"):
        performance_metric_name_in_table = "\\rowcolor{Gray}\n" + performance_metric_name + "* "

    line = "{performance_metric_name} & {performance_metric_count} \\\\ \n".format(
        performance_metric_name = performance_metric_name_in_table
        ,performance_metric_count = performance_metric_count
    )
    table_content_inside = table_content_inside + line


# print table_content_inside

table_content_start = """
\\begin{table}[!ht]
\\centering 
    \\caption{ \\textbf{Performance Metrics Used}. Usage of performance metrics are highly irregular. Some articles does not give any metric(*). Only metrics used more than 3 articles are given. }
  \\scriptsize
     \\label{table-metaPerformanceMetrics}

\\begin{tabular}{ll}

\\toprule

\\textbf{Performance Metric}          & \\textbf{Article Count} \\\\

\\midrule
"""

table_content_end = """
\\bottomrule

\\end{tabular}

\\end{table}

"""

table_content_full = table_content_start + table_content_inside + table_content_end


#print table_content_full

filename = "../latex/table-metaPerformanceMetrics.tex"
target = open(filename, 'w')
target.write(table_content_full)
target.close()
