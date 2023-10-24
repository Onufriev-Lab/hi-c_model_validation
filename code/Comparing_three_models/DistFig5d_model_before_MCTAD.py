# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 15:53:42 2023

@author: samir
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 17:19:12 2022

@author: samir
"""


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
data = pd.read_csv('merged_asynch_11h.csv')
#CRIPT_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
#path = os.path.join(OUT_DIR, "contact_prob.csv", fname)
df = pd.read_csv('data.csv')
#np.random.seed(10000)
#mu, sigma = 0, 0.05069541 # mean and standard deviation
#mu, sigma = 0, 0.2267901
#mu, sigma = 0, 0.0117813
#0.03681657
"""
mu, sigma = 0, 0.07363315
s1 = np.random.normal(mu, sigma, 18)
s2 = np.random.normal(mu, sigma, 18)
s3 = np.random.normal(mu, sigma, 18)
#s = [-1.22, -1.22, -1.22, 1.22, -1.22, -1.22, 1.22, 0.7, -1.22, -1.22, 1.22, -1.22, 1.22, -0.7, -1.22, 1.22, -0.7, 1] 
#s = np.array(s)/5
# s=[ 1.06726478, -0.93863676, -0.75836377, Â 1.20878123, -0.86321056,
# Â  Â  Â  Â -0.83653022, -0.90348329, Â 1.56789177, Â 1.04496334, -0.84585867,
# Â  Â  Â  Â  1.09237798, -0.92107807, -0.79119869, Â 1.08409491, -0.91465416,
# Â  Â  Â  Â  1.13791392, -0.97783665, Â 1.15238278]

#data['avee']=data.iloc[:, 3:18].mean(axis=1)

for i in range(18):
    s2[i] = 10 ** s2[i]
    #Sazer, Shelley, and Helmut Schiessel. "The biology and polymer physics underlying large‐scale chromosome 
    #organization." Traffic 19, no. 2 (2018): 87-104.
    if s2[i] > 0:
        data.iloc[:,i+2]*= s2[i]
        #data.iloc[:,i+2] /= data['avee'][0]
    else:
        #s[i] = -(10 ** s[i])
        data.iloc[:,i+2]/= s2[i]
        #data.iloc[:,i+2] /= data['avee'][0]
    #data.iloc[:,i+2]*= s[i]
    if data.iloc[:,i+2][0] < 0.112:
        data.iloc[:,i+2][0] = 0.112
    elif data.iloc[:,i+2][0] > 0.252:
        data.iloc[:,i+2][0] = 0.252
    #data.iloc[:,i+2] = data.iloc[:,i+2] / (data['avee'][0]) 
    # for j in range(183): 
    #     print(s)
    #     if data.iloc[:,i+2][j] > 4.00:
#     #         data.iloc[:,i+2][j] = 4.00#data.iloc[0, 3:19].mean()

"""
SD_100Kb=data.iloc[0,2:19].std()
SD_1Mb=data.iloc[8,2:19].std()
SD_10Mb=data.iloc[84,2:19].std()
SD_15Mb=data.iloc[127,2:19].std()
SD_20Mb=data.iloc[169,2:19].std()

for i in range(18):
   data.iloc[:,i+2] = data.iloc[:,i+2] / (data['avee'][0])
# line = DataFrame({"Column1": 10000, "CIS_X6S_6h": 1, "CIS_X6S_2_6h": 1, "CIS_X7N_6h": 1, "CIS_X7N_2_6h": 1, "m06_CIS_X6S_6h": 1.3, "m06_CIS_X6S_2_6h": 1, "m06_CIS_X7N_6h": 1, "m06_CIS_X7N_2_6h": 1, "m06_TRANS_X3S_6h": 1, "m06_TRANS_X4N_6h": 1, "p06_CIS_X6S_6h": 1, "p06_CIS_X6S_2_6h": 1, "p06_CIS_X7N_6h": 1, "p06_CIS_X7N_2_6h": 1, "p06_TRANS_X3S_6h": 1, "p06_TRANS_X4N_6h": 1, "TRANS_X3S_6h": 1, "TRANS_X4N_6h": 1}, index=[1])
# data = concat([data.iloc[:1], line, data.iloc[1:]]).reset_index(drop=True)  
x = [2,3,4,5]   

#print (l4)
plt.rcParams['figure.dpi'] = 300
ax1 = data.plot(linestyle='solid', x='Column1', y='1st', color='r')
ax1.set_yscale('log')
ax1.set_xscale('log')
#ax1.set_yticks([0.2,0.7,0.8,2,2.5,3,4,5,6,7,8])
#https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-x-or-y-axis-in-matplotlib
#https://stackoverflow.com/questions/21910986/why-set-xticks-doesnt-set-the-labels-of-ticks
#https://stackoverflow.com/questions/19626530/python-xticks-in-subplots
#https://stackoverflow.com/questions/14530113/set-ticks-with-logarithmic-scale
#https://www.google.com/search?q=set_yscale+tick+labels&rlz=1C1CHBF_enUS799US799&ei=adLLYavJEPWyytMPu8SymAY&oq=set_yscale+tick+l&gs_lcp=Cgdnd3Mtd2l6EAMYADIFCCEQoAEyBQghEKABMgUIIRCgATIFCCEQqwIyBQghEKsCOgcIABBHELADSgQIQRgASgQIRhgAUKUFWMsSYIgbaAFwAngAgAFYiAHrAZIBATOYAQCgAQHIAQjAAQE&sclient=gws-wiz
#https://stackoverflow.com/questions/48107596/edit-tick-labels-in-logarithmic-axis
#https://stackoverflow.com/questions/33847065/logarithmic-y-axis-makes-tick-labels-disappear
ax1.get_yaxis().set_minor_formatter(matplotlib.ticker.OldScalarFormatter())
#plt.locator_params(nbins = 4, axis= 'y')
#ax1.get_yaxis().set_minor_formatter(matplotlib.ticker.NullFormatter())
#ax1.set(xticks=[10**4, 10**5, 10**6, 10**7])
ax1.set(yticks=[0.6, 0.8, 6, 8])
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
plt.xlabel("Genomic Distance (bp)", fontweight='bold')
plt.ylabel("<Rs>", fontweight='bold') 
#lt.legend(("Observed", "Fitted: s^-alpha", "Theoretical: s^-1.8"))
#plt.legend(loc='upper left',prop={"size":4.25}) 

#lt.legend(("SD in 100KB:" ))
#ig.savefig(fpath, bbox_inches="tight")
#lt.close(fig)
#lt.legend(loc='lower right', data.iloc[1,2:19].std())
print(ax1 == ax2 == ax3 == ax4 == ax5 == ax6 == ax7 == ax8 == ax9 == ax10 == ax11 == ax12 == ax13 == ax14 == ax15 == ax16 == ax17 == ax18)  # True
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
