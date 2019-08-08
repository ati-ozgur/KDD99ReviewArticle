import ReviewHelper
import pandas as pd


df = ReviewHelper.get_pandas_data_frame_created_from_bibtex_file()


df_article_count_by_year = df.year.value_counts().sort_index()


csv_file_name = ReviewHelper.get_csv_save_folder() + "article_counts_by_year.csv"


str1 =  df_article_count_by_year.to_csv(header=False)

with open(csv_file_name, 'w') as f:
    f.write("Year,Count\n")
    f.write(str1)
