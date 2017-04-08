# create_csv_IDSTechnology.py

import ReviewHelper
import pandas as pd

df = ReviewHelper.get_pandas_data_frame_created_from_bibtex_file()

# find problematic ones
df[df.metaIDSTechnology.isnull()]

list1 = df.metaIDSTechnology.str.split(",").tolist()



df1 = pd.DataFrame(list1)

for i in range(df1.columns.size):
    df1[i] = df1[i].str.strip()

stacked = df1.stack()


stacked_value_counts = stacked.value_counts()

#print stacked_value_counts

greater_than = stacked_value_counts[stacked_value_counts > 2]



content_inside="Type,LongName,Count\n"

for tech_name in greater_than.index:
    tech_count = greater_than[tech_name]

    print tech_name
    if("Machine" in tech_name):
        short_name = "ML"
    elif("Anomaly" in tech_name):
        short_name = "AD"
    elif("Alert" in tech_name):
        short_name = "AL"
    else:
        short_name = tech_name[0:2]


    line = "{short_name},{name},{count}\n".format(
        short_name = short_name
        ,name = tech_name
        ,count = tech_count)

    content_inside = content_inside + line

#print content_inside

filename = "../latex/excel/list_IDSTechnology.csv"
target = open(filename, 'w')
target.write(content_inside)
target.close()

