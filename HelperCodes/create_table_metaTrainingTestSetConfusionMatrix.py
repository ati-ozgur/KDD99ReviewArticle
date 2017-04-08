import ReviewHelper
import pandas as pd


df = ReviewHelper.get_pandas_data_frame_created_from_bibtex_file()


df.metaTrainingSet.str.contains("KDD99Training")

# find problematic records
df[df.metaTrainingSet.str.contains("KDD99Training").isnull()].ID
df[df.metaTestSet.str.contains("KDD99Training").isnull()].ID

df[df.metaTrainingSet.str.contains("KDD99Test").isnull()].ID
df[df.metaTestSet.str.contains("KDD99Test").isnull()].ID


TrainingAndTraining = df[df.metaTrainingSet.str.contains("KDD99Training")].ID.count()
TrainingAndTest = df[df.metaTrainingSet.str.contains("KDD99Test")].ID.count()

TestAndTraining = df[df.metaTestSet.str.contains("KDD99Training")].ID.count()
TestAndTest = df[df.metaTestSet.str.contains("KDD99Test")].ID.count()

table_content_full = """
\\begin{{table}}[!ht]
    \\centering 
    \\caption{{ \\textbf{{Confusion Matrix for Training and Test Set Usage}}. Normally, only  diagonal of matrix should have values, but most of the reviewed studies use KDD99 training dataset for both testing and training purposes. }}
    \\label{{table-metaTrainingTestSetConfusionMatrix}}

\\begin{{tabular}}{{llll}}

\\toprule
                                &          & \\multicolumn{{2}}{{l}}{{\\textbf{{KDD99}}}} \\\\
\\midrule
                                &          & Training      & Test      \\\\
\\multirow{{2}}{{*}}{{\\textbf{{Reviewed Study}}}} & Training & {TrainingAndTraining} & {TrainingAndTest} \\\\
                                & Test     & {TestAndTraining} & {TestAndTest}\\\\
\\bottomrule

\\end{{tabular}}
\\end{{table}}
""".format(TrainingAndTraining = TrainingAndTraining
    ,TrainingAndTest = TrainingAndTest
    ,TestAndTest = TestAndTest
    ,TestAndTraining = TestAndTraining
    )

#print table_content_full

filename = "../latex/table-metaTrainingTestSetConfusionMatrix.tex"
target = open(filename, 'w')
target.write(table_content_full)
target.close()

