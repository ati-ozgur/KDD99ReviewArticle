import ReviewHelper
import pandas as pd


df = ReviewHelper.get_pandas_data_frame_created_from_bibtex_file()

dfJournalList = df.groupby(['journal'])['ID'].count().order(ascending=False)
