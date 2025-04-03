# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 15:53:42 2023

@author: samir

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
import matplotlib.lines
from matplotlib.transforms import Bbox, TransformedBbox
from matplotlib.legend_handler import HandlerBase
from matplotlib.image import BboxImage
data = pd.read_csv('merged_asynch_1min.csv')

'''
for i in range(18):
   data.iloc[:,i+2] = data.iloc[:,i+2] / (data['avee'][0])
'''
SD_118Kb=data.iloc[0,2:19].std()
SD_1Mb=data.iloc[8,2:19].std()
SD_10Mb=data.iloc[84,2:19].std()
SD_15Mb=data.iloc[127,2:19].std()
SD_20Mb=data.iloc[169,2:19].std()

x = [2,3,4,5]   


plt.rcParams['figure.dpi'] = 300
ax1 = data.plot(linestyle='solid', x='Column1', y='1st', color='r')
#ax1.set_yscale('log')
ax1.set_xscale('log')

ax1.get_yaxis().set_minor_formatter(matplotlib.ticker.OldScalarFormatter())
ax1.tick_params(axis='y', which='minor', labelsize=13)
#plt.locator_params(nbins = 4, axis= 'y')
#ax1.get_yaxis().set_minor_formatter(matplotlib.ticker.NullFormatter())
#ax1.set(xticks=[10**4, 10**5, 10**6, 10**7])
ax1.set(yticks=[0.6, 0.8, 6, 8, 10, 11, 12, 14, 15])
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


plt.xlim(10000,26500000)
plt.ylim(0.15,16)
#plt.yticks([0, 1],rotation=45)
plt.grid(True)
#plt.xscale("log")

#y = np.arange(0, 10, 1)
plt.xlabel("Genomic Distance (bp)", fontsize=16)
plt.ylabel("<Rs>", fontsize=16) 
#lt.legend(("Observed", "Fitted: s^-alpha", "Theoretical: s^-1.8"))
#plt.legend(loc='upper left',prop={"size":4.25}) 

#lt.legend(("SD in 100KB:" ))
#ig.savefig(fpath, bbox_inches="tight")
#lt.close(fig)
#lt.legend(loc='lower right', data.iloc[1,2:19].std())
print(ax1 == ax2 == ax3 == ax4 == ax5 == ax6 == ax7 == ax8 == ax9 == ax10 == ax11 == ax12 == ax13 == ax14 == ax15 == ax16 == ax17 == ax18)  # True
plt.xticks(fontsize=15)
plt.show()


