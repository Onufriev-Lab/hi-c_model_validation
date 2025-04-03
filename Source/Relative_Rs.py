# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 17:19:12 2022

@author: samir
"""
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import pylab as plt
import matplotlib.lines
import scipy.stats as stats
from matplotlib.transforms import Bbox, TransformedBbox
from matplotlib.legend_handler import HandlerBase
from matplotlib.image import BboxImage
import matplotlib.ticker as ticker
data_err= pd.read_csv('error_bar_SD_less.csv')
genomic_distance = data_err['Column1']  # Genomic distance (x-axis)
y_mean = data_err['avee']  # Average values
y_std = data_err['std']  # Standard deviation values
y_mean = pd.to_numeric(y_mean)
y_std = pd.to_numeric(y_std)
valid_mask = np.isfinite(y_mean) & np.isfinite(y_std)
genomic_distance = genomic_distance[valid_mask]
y_mean = y_mean[valid_mask]
y_std = y_std[valid_mask]

data = pd.read_csv('merged_asynch_11h.csv')
#With normalization, line 50 needs to be s2, otherwise line 50 needs to be s2_filtered
# for i in range(18):
#     data.iloc[:,i+2] = data.iloc[:,i+2] / (data['avee'][1]) 

#9898 is the lagest one
seed = 61001
np.random.seed(seed)

average_of_row_1 = data.iloc[1,2:20].mean()    
mu, sigma = 0, 0.2068
s2 = np.random.normal(mu, sigma, 18)

lower_bound = average_of_row_1 - 0.35
upper_bound = average_of_row_1 + 0.35

tmpa = data.iloc[1, 2:20] + s2

# Clip the values to be between a and b
#it will modify the DataFrame df such that any values less than b will become b and any values greater than a will become a, effectively "clipping" the values within the range [b, a].
#df = df.clip(lower=b, upper=a)

s2_filtered = np.clip(tmpa, lower_bound, upper_bound)


for i in range(18):
    # data.iloc[:, i + 2] += s2_filtered[i]
    data.iloc[1:, i + 2] += s2[i]


# for i in range(18):
#     data.iloc[:, i + 2] += s2[i]
#     while not np.any((data.iloc[1, i + 2] > lower_bound) & (data.iloc[1, i + 2] < upper_bound)):      
#         ival = data.iloc[1, i + 2]
#         indices = (ival < lower_bound) | (ival > upper_bound)     
#         s2[indices]= np.random.normal(mu, sigma, 18)

    
data_sizes = [
    ("118kb", 1),
    ("500kb", 4),
    ("1Mb", 9),
    ("1.5Mb", 13),
    ("2Mb", 17),
    ("2.5Mb", 21),
    ("3Mb", 25),
    ("3.5Mb", 30),
    ("4Mb", 34),
    ("4.5Mb", 38),
    ("5Mb", 42),
    ("5.5Mb", 47),
    ("6Mb", 51),
    ("6.5Mb", 55),
    ("7Mb", 60),
    ("7.5Mb", 64),
    ("8Mb", 68),
    ("8.5Mb", 72),
    ("9Mb", 76),
    ("9.1Mb", 77),
    ("9.2Mb", 78),
    ("9.3Mb", 79),
    ("9.4Mb", 80),
    ("9.5Mb", 81),
    ("9.6Mb", 82),
    ("9.7Mb", 83),
    ("9.8Mb", 84),
    ("9.9Mb", 85),
    ("10Mb", 86),
    ("10.5Mb", 89),
    ("11Mb", 93),
    ("11.5Mb", 98),
    ("12Mb", 102),
    ("12.5Mb", 106),
    ("13Mb", 112),
    ("15Mb", 128),
    ("20Mb", 170)
]

for size, index in data_sizes:
    variable_name = f"SD_{size.replace('.', '_')}"
    value = data.iloc[index, 2:19].std()
    globals()[variable_name] = value
    print(f"{size} = {value}")

plt.rcParams['figure.dpi'] = 300
ax1 = data.plot(linestyle='solid', x='Column1', y='this work- Trajectories', color='r')

x_value = [118020,1062180,8969520,10031700,12982200]  # x-coordinate of the point
y_avg = [0.222063611,0.696785111,1.685417778,1.725807778,1.821895] / (data['avee'][1])# Average value
y_std = [0.021562244, 0.018001999, 0.018996434, 0.023415487, 0.029978841]  # Standard deviation
#ax1.errorbar(x_value, y_avg, yerr=y_std, fmt='.', markersize=8, color='black', capsize=0.2)

ax1.set_xscale('log')

ax1.yaxis.set_minor_formatter(ticker.ScalarFormatter())

ax1.tick_params(axis='y', which='minor', labelsize=13)

xtick_labels = ['13 k', '118 k', '1 M', '10 M', '13 M']
xtick_positions = [13000, 118000, 1000000, 10000000, 13000000]

xticks = plt.xticks(xtick_positions, xtick_labels, rotation=45)

for tick in xticks[1]:
    tick.set_fontweight('bold')

ax1.set(yticks=[0.1, 0.8, 2, 3, 4, 5, 6, 8, 10, 11, 12, 15])
ax1.get_legend().remove()

ax2 = data.plot(linestyle='solid', x='Column1', y='2nd', color='maroon', ax=ax1)
ax2.get_legend().remove()
ax3 = data.plot(linestyle='solid', x='Column1', y='3rd', color='violet', ax=ax1)
ax3.get_legend().remove()
ax4 = data.plot(linestyle='solid', x='Column1', y='4th', color='darkorange', ax=ax1)
ax4.get_legend().remove() 
ax5 = data.plot(linestyle='solid', x='Column1', y='5th', color='tomato', ax=ax1)
ax5.get_legend().remove() 
ax6 = data.plot(linestyle='solid', x='Column1', y='6th', color='yellow', ax=ax1)
ax6.get_legend().remove() 
ax7 = data.plot(linestyle='solid', x='Column1', y='7th', color='m', ax=ax1)
ax7.get_legend().remove() 
ax8 = data.plot(linestyle='solid', x='Column1', y='8th', color='deeppink', ax=ax1)
ax8.get_legend().remove()
ax9 = data.plot(linestyle='solid', x='Column1', y='9th', color='g', ax=ax1)
ax9.get_legend().remove()
ax10 = data.plot(linestyle='solid', x='Column1', y='10th', color='lightgreen', ax=ax1)
ax10.get_legend().remove()
ax11 = data.plot(linestyle='solid', x='Column1', y='11th', color='gold', ax=ax1)
ax11.get_legend().remove()
ax12 = data.plot(linestyle='solid', x='Column1', y='12th', color='peru', ax=ax1)
ax12.get_legend().remove()
ax13 = data.plot(linestyle='solid', x='Column1', y='13th', color='lightpink', ax=ax1)
ax13.get_legend().remove()
ax14 = data.plot(linestyle='solid', x='Column1', y='14th', color='olive', ax=ax1)
ax14.get_legend().remove()
ax15 = data.plot(linestyle='solid', x='Column1', y='15th', color='royalblue', ax=ax1)
ax15.get_legend().remove()
ax16 = data.plot(linestyle='solid', x='Column1', y='16th', color='k', ax=ax1)
ax16.get_legend().remove()
ax17 = data.plot(linestyle='solid', x='Column1', y='17th', color='greenyellow', ax=ax1)
ax17.get_legend().remove()
ax18 = data.plot(linestyle='solid', x='Column1', y='18th', color='c', ax=ax1)
ax18.get_legend().remove()

plt.xlim(13000,26500000)
plt.ylim(0.001,15)

plt.grid(True)


plt.xlabel(r"$Genomic\ Distance\ [bp]$" + "\nthis work", fontsize=16)
plt.ylabel("<Rs>"+"\n Normalized by Average bead size", fontsize=14)
#plt.ylabel(r"$<Rs>$" + "[micron]", fontsize=16)
print(ax1)
#print(ax1 == ax2 == ax3 == ax4 == ax5 == ax6 == ax7 == ax8 == ax9 == ax10 == ax11 == ax12 == ax13 == ax14 == ax15 == ax16 == ax17 == ax18)  # True
plt.xticks(fontsize=10, rotation=45)
plt.show()


