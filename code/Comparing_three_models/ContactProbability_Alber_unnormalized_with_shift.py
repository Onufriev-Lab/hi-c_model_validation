
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
#datao = pd.read_csv('rs_simulation_ulianov2021.csv')  
#datao = pd.read_csv('Alber_Rs.csv') 
 
data = pd.read_csv('Rs_Alber_noAverage.csv') 

#datao['avee']=datao.iloc[:, 3:18].mean(axis=1)
#for i in range(20):
    #print(data['avee'][0])
#    datao.iloc[:,i+2] = datao.iloc[:,i+2] / (datao['avee'][9])     
#datao['avee'] = datao.iloc[:, 3:22].mean(axis=1)

# for i in range(20):
#     data.iloc[:,i+2] = data.iloc[:,i+2] / (data['avee'][0])
     


#seed = 62000
seed = 61001
np.random.seed(seed)

average_of_row_1 = data.iloc[0,2:22].mean()    
mu, sigma = 0, 0.2068
s2 = np.random.normal(mu, sigma, 20)

lower_bound = average_of_row_1 - 0.35
upper_bound = average_of_row_1 + 0.35

tmpa = data.iloc[0, 2:22] + s2

# Clip the values to be between a and b
#it will modify the DataFrame df such that any values less than b will become b and any values greater than a will become a, effectively "clipping" the values within the range [b, a].
#df = df.clip(lower=b, upper=a)

s2_filtered = np.clip(tmpa, lower_bound, upper_bound)


for i in range(20):
    #data.iloc[:, i + 2] += s2_filtered[i]
    data.iloc[:, i + 2] += s2[i]
    
data_sizes = [
    ("118kb", 0),
    ("1Mb", 8),
    ("5Mb", 41),
    ("8Mb", 68),
    ("8_5Mb", 72),
    ("9Mb", 76),
    ("9_5Mb", 80),
    ("10Mb", 84),
    ("13Mb", 109),

]

for size, index in data_sizes:
    variable_name = f"SD_{size.replace('.', '_')}"
    value = data.iloc[index, 2:22].std()
    globals()[variable_name] = value
    print(f"{size} = {value}")

plt.rcParams['figure.dpi'] = 300
ax1 = data.plot(linestyle='solid', x='Column1', y='Li 2017', color='r')

x_value = [118020,1062180,8969520,10031700,12982200]  # x-coordinate of the point
y_avg = [0.222063611,0.696785111,1.685417778,1.725807778,1.821895] / (data['avee'][1])# Average value
y_std = [0.021562244, 0.018001999, 0.018996434, 0.023415487, 0.029978841]  # Standard deviation
#ax1.errorbar(x_value, y_avg, yerr=y_std, fmt='.', markersize=8, color='black', capsize=0.2)

ax1.set_xscale('log')

ax1.yaxis.set_minor_formatter(ticker.ScalarFormatter())

ax1.tick_params(axis='y', which='minor', labelsize=13)

xtick_labels = ['10 k', '118 k', '1 M', '10 M', '13 M']
xtick_positions = [10000, 118000, 1000000, 10000000, 13000000]

xticks = plt.xticks(xtick_positions, xtick_labels, rotation=45)

for tick in xticks[1]:
    tick.set_fontweight('bold')

ax1.set(yticks=[0.1, 0.8, 2, 3, 4, 5, 6, 8, 10, 11, 12, 15])
ax1.get_legend().remove()

ax2 = data.plot(linestyle='solid', x='Column1', y='Cell2', color='maroon', ax=ax1)
ax2.get_legend().remove()
ax3 = data.plot(linestyle='solid', x='Column1', y='Cell3', color='tomato', ax=ax1)
ax3.get_legend().remove()
ax4 = data.plot(linestyle='solid', x='Column1', y='Cell4', color='darkorange', ax=ax1)
ax4.get_legend().remove() 
ax5 = data.plot(linestyle='solid', x='Column1', y='Cell5', color='yellow', ax=ax1)
ax5.get_legend().remove() 
ax6 = data.plot(linestyle='solid', x='Column1', y='Cell6', color='violet', ax=ax1)
ax6.get_legend().remove() 
ax7 = data.plot(linestyle='solid', x='Column1', y='Cell7', color='m', ax=ax1)
ax7.get_legend().remove() 
ax8 = data.plot(linestyle='solid', x='Column1', y='Cell8', color='deeppink', ax=ax1)
ax8.get_legend().remove()
ax9 = data.plot(linestyle='solid', x='Column1', y='Cell9', color='g', ax=ax1)
ax9.get_legend().remove()
ax10 = data.plot(linestyle='solid', x='Column1', y='Cell10', color='lightgreen', ax=ax1)
ax10.get_legend().remove()
ax11 = data.plot(linestyle='solid', x='Column1', y='Cell11', color='gold', ax=ax1)
ax11.get_legend().remove()
ax12 = data.plot(linestyle='solid', x='Column1', y='Cell12', color='peru', ax=ax1)
ax12.get_legend().remove()
ax13 = data.plot(linestyle='solid', x='Column1', y='Cell13', color='lightpink', ax=ax1)
ax13.get_legend().remove()
ax14 = data.plot(linestyle='solid', x='Column1', y='Cell14', color='olive', ax=ax1)
ax14.get_legend().remove()
ax15 = data.plot(linestyle='solid', x='Column1', y='Cell15', color='k', ax=ax1)
ax15.get_legend().remove()
ax16 = data.plot(linestyle='solid', x='Column1', y='Cell16', color='royalblue', ax=ax1)
ax16.get_legend().remove()
ax17 = data.plot(linestyle='solid', x='Column1', y='Cell17', color='c', ax=ax1)
ax17.get_legend().remove()
ax18 = data.plot(linestyle='solid', x='Column1', y='Cell18', color='greenyellow', ax=ax1)
ax18.get_legend().remove()

plt.xlim(10000,26500000)
plt.ylim(0.001,12)

plt.grid(True)


plt.xlabel(r"$Genomic\ Distance\ [bp]$" + "\nLi 2017", fontsize=16)
#plt.ylabel("<Rs>"+"\n Normalized by Average TAD size", fontsize=14)
plt.ylabel(r"$<Rs>$" + "[micron]", fontsize=16)
print(ax1)
#print(ax1 == ax2 == ax3 == ax4 == ax5 == ax6 == ax7 == ax8 == ax9 == ax10 == ax11 == ax12 == ax13 == ax14 == ax15 == ax16 == ax17 == ax18)  # True
plt.xticks(fontsize=10, rotation=45)
plt.show()

