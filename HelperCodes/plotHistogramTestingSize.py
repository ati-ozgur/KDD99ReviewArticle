import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from math import log

plt.style.use('fivethirtyeight')

data1 = [line for line in open("../latex/excel/list_TestSetSizes_cleaned.csv", 'r') ]

data2 = [ line for line in data1 if int(line) < 311030 ]
data =  sorted(map(int, data2))

print data

ylabel = 'Times used'
title = "Testing Usage Frequency (total of {0} times).".format(len(data))

n, bins, patches = plt.hist(data, alpha=0.75)

plt.ylabel(ylabel)
plt.title(title)

#plt.savefig('../latex/figure-testing-size-raw.pgf',format='pgf')

plt.show()