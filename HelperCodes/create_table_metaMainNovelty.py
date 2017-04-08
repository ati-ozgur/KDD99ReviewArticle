#create_table_metaMainNovelty.py

import ReviewHelper
import pandas as pd

df = ReviewHelper.get_pandas_data_frame_created_from_bibtex_file()

# find problematic ones
# df[df.metaMainNovelty.isnull()]

list1 = df.metaMainNovelty.str.split(",").tolist()

df1 = pd.DataFrame(list1)

for i in range(df1.columns.size):
    df1[i] = df1[i].str.strip()

stacked = df1.stack()


stacked_value_counts = stacked.value_counts()


#print stacked_value_counts

greater_than = stacked_value_counts[stacked_value_counts > 3]

table_content_inside=""

for main_novelty_name in greater_than.index:
    main_novelty_count = greater_than[main_novelty_name]
    main_novelty_name_in_table = main_novelty_name

    main_novelty_figure_name = ""

    if(main_novelty_name == "Hybrid"):
        main_novelty_figure_name = " (2d,3a) "
    if(main_novelty_name in ["New Algorithm Classifier"
                        ,"New Algorithm Anomaly Detection"]):
        main_novelty_figure_name = " (3d) "
    if(main_novelty_name == "Feature Selection" ):
        main_novelty_figure_name = " (2a) "
    if(main_novelty_name in ["Feature Reduction","Feature Transformation"] ):
        main_novelty_figure_name = " (2b) "
    if(main_novelty_name == "New Algorithm Clustering"):
        main_novelty_figure_name = " (2c) "
    if(main_novelty_name == "Cascaded"):
        main_novelty_name_in_table = "Layered(Cascaded)"
        main_novelty_figure_name = " (3c) "
    if(main_novelty_name == "Ensemble"):
        main_novelty_figure_name = " (3b) "
    if(main_novelty_name == "New Optimization Algorithm"):
        main_novelty_figure_name = " (2d,3a) "




    line = "{main_novelty_name} & {main_novelty_count} & {main_novelty_figure_name} \\\\ \n".format(
        main_novelty_name = main_novelty_name_in_table
        ,main_novelty_count = main_novelty_count
        ,main_novelty_figure_name = main_novelty_figure_name
    )
    table_content_inside = table_content_inside + line


#print table_content_inside

table_content_start = """
\\begin{table}[!ht]
\\centering 


\\scriptsize
\\caption{ \\textbf{Evaluating the reviewed articles regarding to machine learning model Figure~\\ref{figure-GeneralMachineLearningFlowChart}} }
\\label{table-metaMainNovelty}

\\begin{tabular}{@{}p{0.6\\columnwidth}p{0.15\\columnwidth}p{0.15\\columnwidth}@{}} 


\\toprule

\\textbf{Contribution(Novelty)}           & \\textbf{Article Count} & \\textbf{Figure 3} \\\\

\\midrule
"""

table_content_end = """
\\bottomrule

\\end{tabular}

\\end{table}

"""

table_content_full = table_content_start + table_content_inside + table_content_end


#print table_content_full

filename = "../latex/table-metaMainNovelty.tex"
target = open(filename, 'w')
target.write(table_content_full)
target.close()
