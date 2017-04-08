import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from math import log

#plt.style.use('ggplot')
plt.style.use('fivethirtyeight')

data1 = [line for line in open("../latex/excel/list_TrainingSetSizes_cleaned.csv", 'r')]

data =  sorted(map(int, data1))

plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))


ylabel = 'Times used'
xlabel = "KDD99 Training Dataset is used {0} times for all sizes".format(len(data))

x_figure_text = 0.4
y_figure_text1 = 0.85
y_figure_text2 = 0.55
y_figure_text3 = 0.2


plt.subplot(3,1,1)

dataset_bins = [10000,100000,500000,1000000,2000000,3000000,4000000,5000000]
dataset_bins_labels = ['$10000$','$100000$','$500000$','$1000000$','$2000000$','$3000000$','$4000000$','$5000000$']

n, bins, patches = plt.hist(data,dataset_bins , alpha=0.75)



plt.ylabel(ylabel)
plt.figtext(x_figure_text,y_figure_text1,xlabel,fontsize=24)

plt.xticks(bins,dataset_bins_labels,rotation=20)







data_lower_10000 = [x for x in data if x <= 10000]

xlabel = "KDD99 Training Dataset is used {0} times for sizes less than 10.000".format(len(data_lower_10000))



plt.subplot(3,1,2)
n, bins, patches = plt.hist(data_lower_10000, bins=10, alpha=0.75)
plt.ylabel(ylabel)
plt.figtext(x_figure_text,y_figure_text2,xlabel,fontsize=24)



data_between_10000_100000 = [x for x in data if x > 10000 and x <100000]


xlabel = "KDD99 Training Dataset is used {0} times for sizes between 10.000 and 100.000".format(len(data_between_10000_100000))



plt.subplot(3,1,3)
n, bins, patches = plt.hist(data_between_10000_100000, bins=10, alpha=0.75)

plt.ylabel(ylabel)
plt.figtext(x_figure_text,y_figure_text3,xlabel,fontsize=24)

plt.tight_layout()

#plt.savefig('../latex/figure-training-size-raw.pgf',format='pgf')


plt.show()
