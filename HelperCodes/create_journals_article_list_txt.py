import ReviewHelper
import pandas as pd


df = ReviewHelper.get_pandas_data_frame_created_from_bibtex_file()

list1 = sorted(df.title.tolist())


content = ""
for title in list1:
    title = title.replace("{","")
    title = title.replace("}","")
    title = title.replace(":","")
    title = title.lower()
    content = content + title + "\n"


filename = "../latex/excel/list_ArticleTitles.csv"
target = open(filename, 'w')
target.write(content.encode('utf-8') )
target.close()

