import ReviewHelper
import pandas as pd

df = ReviewHelper.get_pandas_data_frame_created_from_bibtex_file()

# find wrong records
print df[df.metaTrainingSetSizes.isnull()].ID

list1 = df.metaTrainingSetSizes.str.split(",").tolist()

df1 = pd.DataFrame(list1)

for i in range(df1.columns.size):
    df1[i] = df1[i].str.strip()

stacked = df1.stack()


stacked_value_counts = stacked.value_counts()

print stacked_value_counts
