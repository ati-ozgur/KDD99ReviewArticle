import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from math import log

plt.style.use('fivethirtyeight')


data1 = [line for line in open("../latex/excel/list_TrainingSetSizes_cleaned.csv", 'r')]

data =  sorted(map(int, data1))

print data

ylabel = 'Times used'
title = "Training Dataset Total of {0} times used".format(len(data))
xlabel = "Dataset Size"

n, bins, patches = plt.hist(data,histtype='barstacked')

plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)

plt.savefig('../latex/figure-training-size-raw.tex',format='pgf')

plt.show()