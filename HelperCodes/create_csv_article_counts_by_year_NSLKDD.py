import ReviewHelper
import pandas as pd


df = ReviewHelper.get_pandas_data_frame_created_from_bibtex_file()

row_filter = df.metaDatasetsUsed.str.contains("NSL-KDD")

df_article_count_by_year = df[row_filter].year.value_counts().sort_index()


csv_file_name = ReviewHelper.get_csv_save_folder() + "article_counts_by_year_NSLKDD.csv"


str1 = df_article_count_by_year.to_csv(path=None)

with open(csv_file_name, 'wb') as f:
    f.write("{0},{1}\n".format("Year" , "Count"))
    f.write(str1)
