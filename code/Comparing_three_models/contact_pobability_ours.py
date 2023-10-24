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


for i in range(18):
    data.iloc[:,i+2] = data.iloc[:,i+2] / (data['avee'][1]) 
  
mu, sigma = 0, 0.2068

s2 = np.random.normal(mu, sigma, 18)
print(s2)
'''
lower_bound = -0.35
upper_bound = 0.35

while not np.all((s2 > lower_bound) & (s2 < upper_bound)):
    indices = np.logical_not((s2 > lower_bound) & (s2 < upper_bound))
    s2[indices] = np.random.normal(mu, sigma, indices.sum())
'''    
#for i in range(18):

#    data.iloc[:,i+2]+= s2[i]

data_sizes = [
    ("118kb", 0),
    ("500kb", 3),
    ("1Mb", 8),
    ("1.5Mb", 12),
    ("2Mb", 16),
    ("2.5Mb", 20),
    ("3Mb", 24),
    ("3.5Mb", 29),
    ("4Mb", 33),
    ("4.5Mb", 37),
    ("5Mb", 41),
    ("5.5Mb", 46),
    ("6Mb", 50),
    ("6.5Mb", 54),
    ("7Mb", 59),
    ("7.5Mb", 63),
    ("8Mb", 67),
    ("8.5Mb", 71),
    ("9Mb", 75),
    ("9.1Mb", 76),
    ("9.2Mb", 77),
    ("9.3Mb", 78),
    ("9.4Mb", 79),
    ("9.5Mb", 80),
    ("9.6Mb", 81),
    ("9.7Mb", 82),
    ("9.8Mb", 83),
    ("9.9Mb", 84),
    ("10Mb", 85),
    ("10.5Mb", 88),
    ("11Mb", 92),
    ("11.5Mb", 97),
    ("12Mb", 101),
    ("12.5Mb", 105),
    ("13Mb", 111),
    ("15Mb", 127),
    ("20Mb", 169)
]

for size, index in data_sizes:
    variable_name = f"SD_{size.replace('.', '_')}"
    value = data.iloc[index, 2:19].std()
    globals()[variable_name] = value
    print(f"{size} = {value}")

plt.rcParams['figure.dpi'] = 300
ax1 = data.plot(linestyle='solid', x='Column1', y='this work- Trajectories', color='b')

x_value = [118020,1062180,8969520,10031700,12982200]  # x-coordinate of the point
y_avg = [0.222063611,0.696785111,1.685417778,1.725807778,1.821895] / (data['avee'][1])# Average value
y_std = [0.021562244, 0.018001999, 0.018996434, 0.023415487, 0.029978841]  # Standard deviation
#ax1.errorbar(x_value, y_avg, yerr=y_std, fmt='.', markersize=8, color='black', capsize=0.2)

ax1.set_xscale('log')
ax1.set_yscale('log')

ax1.xaxis.set_major_formatter(ticker.ScalarFormatter())

ax1.tick_params(axis='y', which='minor', labelsize=13)

xtick_labels = ['10 kb', '13 kb', '100 kb', '1 Mb', '10 Mb', '13 Mb', '20 Mb']
xtick_positions = [10000, 13000, 100000, 1000000, 10000000, 13000000, 20000000]

xticks = plt.xticks(xtick_positions, xtick_labels, rotation=45)

for tick in xticks[1]:
    tick.set_fontweight('bold')

# Set the tick locations and labels for the y-axis
# Adjust the tick positions and labels for the y-axis
# Adjust the tick positions and labels for the y-axis
ytick_labels = [0.1, 0.8,  1.0,  3.0,  5.0,  7.0,   11.0]
ytick_positions = [0.1, 0.8,  1.0,  3.0,  5.0,  7.0,   11.0]
ax1.set_yticks(ytick_positions)
ax1.set_yticklabels(ytick_labels)

# Adjust the tick parameters for the y-axis
ax1.tick_params(axis='y', which='both', labelsize=12)

# Adjust the tick parameters for the x-axis
ax1.tick_params(axis='x', which='both', labelsize=12)


# ContactProbability_Alber.py
datao = pd.read_csv('Rs_Alber_noAverage.csv')
for i in range(20):
     datao.iloc[:,i+2] = datao.iloc[:,i+2] / (datao['avee'][0])
ax2 = datao.plot(linestyle='solid', x='Column1', y='Li 2017', color='g', ax=ax1)


# Rs_plot_Sexton_Experiment.py
dfS = pd.read_csv('contact_decay_Sexton.csv')
for i in range(1):
     dfS.iloc[:,i+3] = dfS.iloc[:,i+3] / (dfS['avee'][1])
ax3 = dfS.plot(linestyle='solid', x='Column1', y='Sexton 2012- Hi-C contact map', color='r', ax=ax1)


dfS = pd.read_csv('ours_contact_decay_av18.csv')
for i in range(1):
     dfS.iloc[:,i+3] = dfS.iloc[:,i+3] / (dfS['avee'][1])
ax3 = dfS.plot(linestyle='solid', x='Column1', y='this work- Hi-C contact map', color='gold', ax=ax1)

datau = pd.read_csv('rs_Ulianov_fixedStop.csv') 
for i in range(20):
     datau.iloc[:,i+2] = datau.iloc[:,i+2] / (datau['avee'][12])
ax3 = datau.plot(linestyle='solid', x='Column1', y='Ulianov 2021', color='violet', ax=ax1)

'''
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
'''
plt.xlim(10000,26500000)
# Adjust the y-axis limits
#ax1.set_ylim(bottom=min(y)-1, top=max(y)+1)  # Increase the padding as needed

plt.ylim(0.1,12)

plt.grid(True)


plt.xlabel("Genomic Distance (bp)", fontsize=16)
plt.ylabel("<Rs>""\n Normalized by Average Rs in 118kb", fontsize=14) 
print(ax1)
#print(ax1 == ax2 == ax3 == ax4 == ax5 == ax6 == ax7 == ax8 == ax9 == ax10 == ax11 == ax12 == ax13 == ax14 == ax15 == ax16 == ax17 == ax18)  # True
plt.xticks(fontsize=10, rotation=45)
plt.show()


