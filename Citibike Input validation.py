# -*- coding: utf-8 -*-
"""

@author: Sukit @ Ajya

"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


import csv

import_data = []
observed_checkout = []
observed_returning = []

with open('citibike_observed.csv') as files:
    reader = csv.reader(files)
    import_data = [i for i in reader]
    
observed_checkout = [float(i[0]) for i in import_data[1:]]
observed_returning = filter(None,[i[1] for i in import_data[1:]])
observed_returning = [float(i) for i in observed_returning]

scale_checkout = 1/1.57 # lambda of bike checked out calculated on Excel
scale_returning = 1/1.183 # lambda of bike returned calculated on Excel

values = np.array(observed_checkout)
values_cdf = [np.sum(values <= x)/float(len(values)) for x in values]


plt.figure()
plot_x = np.linspace(0,6.5)
plt.plot(plot_x, stats.expon.cdf(plot_x, scale= scale_checkout), '-r', label='$F(x)$ Expected')
plt.step(values, values_cdf, '-b', where='post', label='$F_n(x)$ Observed')
plt.xlabel('Arrival Time ($x$)')
plt.ylabel('Cumulative Probability ($P(x \\leq X)$)')
plt.title('Input validation (Inter-arrival of riders taking bikes)')
plt.legend(loc='best')
plt.savefig('K-s test for bike checked out.png')

ks, p_ks = stats.kstest(values, lambda i: stats.expon.cdf(i, scale= scale_checkout))
print 'k-s for bike checked out = {:.4f}, p-value = {:.4f}'.format(ks, p_ks)


values = np.array(observed_returning)
values_cdf = [np.sum(values <= x)/float(len(values)) for x in values]

plt.figure()
plot_x = np.linspace(0,8)
plt.plot(plot_x, stats.expon.cdf(plot_x, scale= scale_returning), '-r', label='$F(x)$ Expected')
plt.step(values, values_cdf, '-g', where='post', label='$F_n(x)$ Observed')
plt.xlabel('Returned-bike Time ($x$)')
plt.ylabel('Cumulative Probability ($P(x \\leq X)$)')
plt.title('Input validation (Inter-arrival of riders returning)')
plt.legend(loc='best')
plt.savefig('K-s test for bike returned.png')

ks, p_ks = stats.kstest(values, lambda i: stats.expon.cdf(i, scale= scale_returning))
print 'k-s for bike returned = {:.4f}, p-value = {:.4f}'.format(ks, p_ks)