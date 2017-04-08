# create_table_metaSoftwareUsed.py
import ReviewHelper
import pandas as pd

df = ReviewHelper.get_pandas_data_frame_created_from_bibtex_file()

# find wrong records
df[df.metaSoftwareUsed.isnull()].ID

list1 = df.metaSoftwareUsed.str.split(",").tolist()

df1 = pd.DataFrame(list1)

for i in range(df1.columns.size):
    df1[i] = df1[i].str.strip()
    #df1[i] = df1[i].str.lower()

stacked = df1.stack()


stacked_value_counts = stacked.value_counts()

#print stacked_value_counts

greater_than = stacked_value_counts[stacked_value_counts > 1]

table_content_inside=""

for software_name in greater_than.index:
    software_count = greater_than[software_name]

    line = "{software_name} & {software_count} \\\\ \n".format(
        software_name = software_name
        ,software_count = software_count
    )
    table_content_inside = table_content_inside + line





table_content_start = """
\\begin{table}[!ht]
\\centering 

    \\caption{ \\textbf{Software used in Reviewed Articles}. Weka, Matlab, and Libsvm are used for comparison purposes. General purpose programming languages are used for implementation. Software that are used less than two is not included. }
    \\label{table-metaSoftwareUsed}

\\begin{tabular}{ll}

\\toprule

\\textbf{Software Tool/Package  }                  & \\textbf{Article Count }\\\\

\\midrule
"""

table_content_end = """
\\bottomrule

\\end{tabular}

\\end{table}

"""

table_content_full = table_content_start + table_content_inside + table_content_end

#print table_content_full


filename = "../latex/table-metaSoftwareUsed.tex"
target = open(filename, 'w')
target.write(table_content_full)
target.close()
