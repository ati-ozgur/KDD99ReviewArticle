# create_csv_list_TestSizes.py

# create_table_metaSoftwareUsed.py
import ReviewHelper
import pandas as pd
df1 = ReviewHelper.get_pandas_data_frame_dataset_sizes_training()

df1.to_csv("../latex/excel/list_TrainingSetSizes_cleaned.csv",index =False)
