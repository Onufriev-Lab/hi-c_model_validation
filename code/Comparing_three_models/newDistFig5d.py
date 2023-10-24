# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 17:19:12 2022

@author: samir
"""
#Commenting line 80 and 81
#https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-x-or-y-axis-in-matplotlib
#https://stackoverflow.com/questions/21910986/why-set-xticks-doesnt-set-the-labels-of-ticks
#https://stackoverflow.com/questions/19626530/python-xticks-in-subplots
#https://stackoverflow.com/questions/14530113/set-ticks-with-logarithmic-scale
#https://www.google.com/search?q=set_yscale+tick+labels&rlz=1C1CHBF_enUS799US799&ei=adLLYavJEPWyytMPu8SymAY&oq=set_yscale+tick+l&gs_lcp=Cgdnd3Mtd2l6EAMYADIFCCEQoAEyBQghEKABMgUIIRCgATIFCCEQqwIyBQghEKsCOgcIABBHELADSgQIQRgASgQIRhgAUKUFWMsSYIgbaAFwAngAgAFYiAHrAZIBATOYAQCgAQHIAQjAAQE&sclient=gws-wiz
#https://stackoverflow.com/questions/48107596/edit-tick-labels-in-logarithmic-axis
#https://stackoverflow.com/questions/33847065/logarithmic-y-axis-makes-tick-labels-disappear
"""
0. Read data
1. Generate 18 random numbers from Guassian Dist, some are positive and
Â some are negative
2. Shift the curve for each single cell up and down.
log[(ax+b) * c]= log (ax+b) +log(c)
log[(ax+b) / c]= log (ax+b) -log(c)
log(c) is Â number generated in the first step
(positive and negative)
3. Calculate average Rs at 100Kb.
4. Normalized all values by the average Rs at 100Kb.
5. Transformed the axes to the log scale (as Ulianov did)
"""
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import pylab as plt
import matplotlib.lines
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
#CRIPT_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
#path = os.path.join(OUT_DIR, "contact_prob.csv", fname)
#df = pd.read_csv('data.csv')
#np.random.seed(108801)
#mu, sigma = 0, 0.05069541 # mean and standard deviation
#mu, sigma = 0, 0.2267901
#mu, sigma = 0, 0.0117813
#0.03681657
#mu, sigma = 0, 0.07363315
#mu, sigma  =  0, 0.104131747496052

'''
def truncated_normal(mean, sigma, lower_bound, upper_bound, size):
    samples = []
    while len(samples) < size:
        x = np.random.normal(mean, sigma)
        if lower_bound <= x <= upper_bound:
            samples.append(x)
    return samples

# Example usage
mu = 1.0360
sigma = 0.0304
lower_bound = 0.63616
upper_bound = 1.4359
sample_size = 18

s2 = truncated_normal(mu, sigma, lower_bound, upper_bound, sample_size)
print(s2)

'''

for i in range(18):
    data.iloc[:,i+2] = data.iloc[:,i+2] / (data['avee'][1]) 
  
mu, sigma = 0, 0.104
s2 = np.random.normal(mu, sigma, 18)

lower_bound = -0.35
upper_bound = 0.35

while not np.all((s2 > lower_bound) & (s2 < upper_bound)):
    indices = np.logical_not((s2 > lower_bound) & (s2 < upper_bound))
    s2[indices] = np.random.normal(mu, sigma, indices.sum())

print(s2)
#print(s2)

for i in range(18):
    #s2[i] = 10 ** s2[i]
    #Sazer, Shelley, and Helmut Schiessel. "The biology and polymer physics underlying large‐scale chromosome 
    #organization." Traffic 19, no. 2 (2018): 87-104.
    #if s2[i] > 0:
    data.iloc[:,i+2]+= s2[i]
        #data.iloc[:,i+2] /= data['avee'][0]
    #else:
        #s[i] = -(10 ** s[i])
        #data.iloc[:,i+2]-= s2[i]
        #data.iloc[:,i+2] /= data['avee'][0]
    #data.iloc[:,i+2]*= s[i]
    '''
    if data.iloc[:,i+2][0] < 0.112:
        data.iloc[:,i+2][0] = 0.112
    elif data.iloc[:,i+2][0] > 0.252:
        data.iloc[:,i+2][0] = 0.252
    ''' 
  
 
        #data.iloc[:,i+2] = data.iloc[:,i+2] / (data['avee'][0]) 
        # for j in range(183): 
        #     print(s)
        #     if data.iloc[:,i+2][j] > 4.00:
    #     #         data.iloc[:,i+2][j] = 4.00#data.iloc[0, 3:19].mean()

# line = DataFrame({"Column1": 10000, "CIS_X6S_6h": 1, "CIS_X6S_2_6h": 1, "CIS_X7N_6h": 1, "CIS_X7N_2_6h": 1, "m06_CIS_X6S_6h": 1.3, "m06_CIS_X6S_2_6h": 1, "m06_CIS_X7N_6h": 1, "m06_CIS_X7N_2_6h": 1, "m06_TRANS_X3S_6h": 1, "m06_TRANS_X4N_6h": 1, "p06_CIS_X6S_6h": 1, "p06_CIS_X6S_2_6h": 1, "p06_CIS_X7N_6h": 1, "p06_CIS_X7N_2_6h": 1, "p06_TRANS_X3S_6h": 1, "p06_TRANS_X4N_6h": 1, "TRANS_X3S_6h": 1, "TRANS_X4N_6h": 1}, index=[1])
# data = concat([data.iloc[:1], line, data.iloc[1:]]).reset_index(drop=True)  
x = [2,3,4,5]   

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

#print (l4)
plt.rcParams['figure.dpi'] = 300
ax1 = data.plot(linestyle='solid', x='Column1', y='1st', color='r')

x_value = [1062180,4484760]  # x-coordinate of the point
y_avg = [2,3] # Average value
y_std = [1.5,1]  # Standard deviation
ax1.errorbar(x_value, y_avg, yerr=y_std, fmt='o', markersize=8, color='black', capsize=2)

#ax1.errorbar(data['Column1'], data['1st'], yerr=0.2, fmt='none', ecolor='black')
#ax1.errorbar(x='Column1', y='1st', yerr=0.2, fmt='.', capsize=5, color='blue')

#ax1.set_yscale('log')
ax1.set_xscale('log')
#ax1.set_yticks([0.2,0.7,0.8,2,2.5,3,4,5,6,7,8])


ax1.yaxis.set_minor_formatter(ticker.ScalarFormatter())

ax1.tick_params(axis='y', which='minor', labelsize=13)
#ax1.set(xticks=[10000, 13000, 100000, 1000000, 10000000, 13000000, 20000000], xticklabels=['10 kb', '13 kb', '100 kb', '1 Mb', '10 Mb', '13 Mb', '20 Mb'])
xtick_labels = ['10 kb', '13 kb', '100 kb', '1 Mb', '10 Mb', '13 Mb', '20 Mb']
xtick_positions = [10000, 13000, 100000, 1000000, 10000000, 13000000, 20000000]

xticks = plt.xticks(xtick_positions, xtick_labels, rotation=45)

for tick in xticks[1]:
    tick.set_fontweight('bold')

#plt.locator_params(nbins = 4, axis= 'y')
#ax1.get_yaxis().set_minor_formatter(matplotlib.ticker.NullFormatter())
#ax1.set(xticks=[10**4, 10**5, 10**6, 10**7])
ax1.set(yticks=[0.15, 0.8, 2, 3, 4, 5, 6, 8, 10, 11, 12, 15])
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
#fig, ax = plt.subplots()
#ax.axis([1, 10000, 1, 100000])
#ax.axis([1, 10000, 1, 100000])
#plt.yticks(np.arange(0, 10, step=0.2))
#plt.yscale("log")
plt.xlim(10000,26500000)
plt.ylim(0.15,16)

#plt.yticks([0, 1],rotation=45)
plt.grid(True)
#plt.xscale("log")

#y = np.arange(0, 10, 1)
plt.xlabel("Genomic Distance (bp)"+"\n Ours", fontsize=16)
plt.ylabel("<Rs>""\n Normalized by Average Rs in 118kb", fontsize=14) 
#lt.legend(("Observed", "Fitted: s^-alpha", "Theoretical: s^-1.8"))
#plt.legend(loc='upper left',prop={"size":4.25}) 

#lt.legend(("SD in 100KB:" ))
#ig.savefig(fpath, bbox_inches="tight")
#lt.close(fig)
#lt.legend(loc='lower right', data.iloc[1,2:19].std())
print(ax1 == ax2 == ax3 == ax4 == ax5 == ax6 == ax7 == ax8 == ax9 == ax10 == ax11 == ax12 == ax13 == ax14 == ax15 == ax16 == ax17 == ax18)  # True
plt.xticks(fontsize=10, rotation=45)
plt.show()

# backup
#ax1.set_adjustable("datalim")
#ax1.set_aspect(0.1)
#ax1.set_yticks(np.arange(1, 9, step=1),[1,2,3,4,5,6,7,8,9] )
#ax1.set_yticklabels(x)
# from matplotlib.ticker import FixedLocator, FixedFormatter
# x_formatter = FixedFormatter([
#     "I like this spot", "and this", "and that"])
# y_formatter = FixedFormatter(["-1e7", "111", "007"])
# x_locator = FixedLocator([100000, 1000000, 10000000])
# y_locator = FixedLocator([.1, 1, 4.9])
# ax1.xaxis.set_major_formatter(x_formatter)
# ax1.yaxis.set_major_formatter(y_formatter)
# ax1.xaxis.set_major_locator(x_locator)
# ax1.yaxis.set_major_locator(y_locator)

#line134 for legend
