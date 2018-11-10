# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 18:33:06 2018

@author: Rhonda
"""

import pandas as pd
import pylab as plt
import numpy as np
from collections import defaultdict, Counter

bcancer = pd.read_csv('Breast-Cancer-Wisconsin.csv')
list(bcancer)

bcancer = bcancer.replace('?',np.nan)
bcancer["A7"] = pd.to_numeric(bcancer["A7"])
bcancer.fillna(bcancer.mean())
#for saving file:  bcancer.to_csv('bcancer.csv')
print(bcancer.describe())

from pandas.tools import plotting
plotting.scatter_matrix(bcancer[['A3', 'A4', 'A7','CLASS']])

import matplotlib.pyplot as plt
def plot_corr(bcancer,size=10):
    corr = bcancer.corr()
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr)
    plt.xticks(range(len(corr.columns)), corr.columns);
    plt.yticks(range(len(corr.columns)), corr.columns);
plot_corr(bcancer,size = 10)

def correlation_matrix(df):
    from matplotlib import pyplot as plt
    from matplotlib import cm as cm

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    cmap = cm.get_cmap('jet', 60)
    cax = ax1.imshow(df.corr(), interpolation="nearest", cmap=cmap)
    ax1.grid(True)
    plt.title('Breast Cancer Wisconsin Correlation')
    labels=['A2','A3','A4','A5','A6','A7','A8','A9','A10','CLASS',]
    ax1.set_xticklabels(labels,fontsize=12)
    ax1.set_yticklabels(labels,fontsize=12)
    # Add colorbar, make sure to specify tick locations to match desired ticklabels
    fig.colorbar(cax, ticks=[.75,.8,.85,.90,.95,1])
    plt.show()
correlation_matrix(bcancer)

#3. Uniformity of Cell Size       1 - 10
#4. Uniformity of Cell Shape      1 - 10
#7. Bare Nuclei                   1 - 10

from pandas.tools import plotting
plotting.scatter_matrix(bcancer[['A3', 'A4', 'A7', 'CLASS']])