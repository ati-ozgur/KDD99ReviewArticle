
import ReviewHelper
import pandas as pd

df = ReviewHelper.get_pandas_data_frame_created_from_bibtex_file()

# find problematic ones
df[df.metaComparedClassifiers.isnull()]



list1 = df.metaComparedClassifiers.str.split(",").tolist()

#strip_list = [map(str.strip, inner_list) for inner_list in list1]


df1 = pd.DataFrame(list1)

for i in range(df1.columns.size):
    df1[i] = df1[i].str.strip()
    df1[i] = df1[i].str.lower()

stacked = df1.stack()


stacked_value_counts = stacked.value_counts()

greater_than = stacked_value_counts[stacked_value_counts > 3]

table_content_inside=""

for compared_classifier_name in greater_than.index:
    compared_classifier_count = greater_than[compared_classifier_name]


    compared_classifier_name_in_table = compared_classifier_name
    if(compared_classifier_name == "none"):
        compared_classifier_name_in_table = "\\rowcolor{Gray}\n" + compared_classifier_name + "(Not compared with other methods)"

    if(compared_classifier_name == "literature"):
        compared_classifier_name_in_table = "\\rowcolor{Gray}\n" + compared_classifier_name + "(no experimental comparison)"


    line = "{compared_classifier_name} & {compared_classifier_count} \\\\ \n".format(
        compared_classifier_name = compared_classifier_name_in_table
        ,compared_classifier_count = compared_classifier_count
    )
    table_content_inside = table_content_inside + line




table_content_start = """
\\begin{table}[!ht]
 \\centering 

    \\caption{ \\textbf{Classifiers used for comparison in Experiments}.}

    \\label{table-metaComparedClassifiers}
\\footnotesize


\\begin{tabular}{@{}p{0.8\\columnwidth}p{0.2\\columnwidth}@{}}

\\toprule

\\textbf{Classifier }                                 & \\textbf{Article Count} \\\\

\\midrule

"""

table_content_end = """
\\bottomrule

\\end{tabular}

\\end{table}

"""

table_content_full = table_content_start + table_content_inside + table_content_end

#print table_content_full


filename = "../latex/table-metaComparedClassifiers.tex"
target = open(filename, 'w')
target.write(table_content_full)
target.close()
