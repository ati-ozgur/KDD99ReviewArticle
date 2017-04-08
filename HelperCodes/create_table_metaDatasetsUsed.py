
import ReviewHelper
import pandas as pd

df = ReviewHelper.get_pandas_data_frame_created_from_bibtex_file()

# find problematic ones
df[df.metaDatasetsUsed.isnull()]

list1 = df.metaDatasetsUsed.str.split(",").tolist()


df1 = pd.DataFrame(list1)

for i in range(df1.columns.size):
    df1[i] = df1[i].str.strip()

stacked = df1.stack()


stacked_value_counts = stacked.value_counts()

greater_than = stacked_value_counts[stacked_value_counts > 3]

table_content_inside=""

list_ids_dataset_names = ["KDD99","NSL-KDD","DARPA","Kyoto","ISCX"]

table_content_inside=""

for dataset_name in greater_than.index:
    dataset_count = greater_than[dataset_name]
    dataset_name_in_table = dataset_name


    dataset_name_in_table = dataset_name
    if(dataset_name in list_ids_dataset_names):
        dataset_name_in_table = "\\rowcolor{Gray}\n" + dataset_name + "* "


    line = "{dataset_name} & {dataset_count} \\\\ \n".format(
        dataset_name = dataset_name_in_table
        ,dataset_count = dataset_count
    )
    table_content_inside = table_content_inside + line


table_content_start = """
\\begin{table}[!ht]
    \\centering 
    \\caption{ \\textbf{Most used Datasets}. * denotes IDS datasets. Datasets that are used less than three is not included.}
    \\label{table-metaDatasetsUsed}


\\begin{tabular}{ll}

\\toprule

\\textbf{Dataset Name  }     & \\textbf{Article Count} \\\\

\\midrule

"""

table_content_end = """
\\bottomrule

\\end{tabular}

\\end{table}

"""

table_content_full = table_content_start + table_content_inside + table_content_end


#print table_content_full

filename = "../latex/table-metaDatasetsUsed.tex"
target = open(filename, 'w')
target.write(table_content_full)
target.close()

