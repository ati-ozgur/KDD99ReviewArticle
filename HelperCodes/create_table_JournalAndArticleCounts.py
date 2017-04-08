import ReviewHelper
import pandas as pd

df = ReviewHelper.get_pandas_data_frame_created_from_bibtex_file()

#df_journal = df.groupby('journal')["ID"]
dfJournalList = df.groupby(['journal'])['ID'].count().order(ascending=False)



isOdd = (dfJournalList.size % 2 == 1)
if (isOdd):
    table_row_length = dfJournalList.size / 2 +1
else:
    table_row_length = dfJournalList.size / 2


table_content_inside=""

for index in range(table_row_length):
    journal_name_1column = dfJournalList.index[index]
    journal_count_1column = dfJournalList[index]

    second_column_index = index + table_row_length
    if(second_column_index < dfJournalList.size):
        journal_name_2column = dfJournalList.index[second_column_index]
        journal_count_2column = dfJournalList[second_column_index]
    else:
        journal_name_2column = ""
        journal_count_2column = ""
    line = "{journal_name_1column} & {journal_count_1column} & {journal_name_2column} & {journal_count_2column}   \\\\ \n".format(
        journal_name_1column = journal_name_1column
        ,journal_count_1column = journal_count_1column
        ,journal_name_2column = journal_name_2column
        ,journal_count_2column = journal_count_2column
    )

    table_content_inside = table_content_inside + line


table_content_start = """
\\begin{table*}[!ht]
    \\caption{ \\textbf{Journals and Article Counts} }
    \\label{table-JournalAndArticleCounts}
    \\centering
   \\begin{adjustbox}{max width=\\textwidth}
    \\normalsize
\\begin{tabular}{llll}

\\toprule

Journal Name & Article Count & Journal Name & Article Count \\\\

\\midrule
"""
table_content_end = """

\\bottomrule

\\end{tabular}

\\end{adjustbox}

\\end{table*}
"""

table_content_full = table_content_start + table_content_inside + table_content_end



filename = "../latex/table-JournalAndArticleCounts.tex"
target = open(filename, 'w')
target.write(table_content_full)
target.close()
