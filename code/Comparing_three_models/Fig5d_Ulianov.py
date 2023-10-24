import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines

datao = pd.read_csv('rs_simulation_ulianov2021.csv')  
#datao['avee']=datao.iloc[:, 3:18].mean(axis=1)
#for i in range(20):
    #print(data['avee'][0])
#    datao.iloc[:,i+2] = datao.iloc[:,i+2] / (datao['avee'][9])     
#datao['avee'] = datao.iloc[:, 3:22].mean(axis=1)
SD_100Kb = datao.iloc[13,2:22].std() # 100kb
SD_1Mb = datao.iloc[99,2:22].std() # 1Mb 
SD_10Mb = datao.iloc[999,2:22].std() # 10Mb
SD_15Mb = datao.iloc[1501,2:22].std() # 15Mb
SD_20Mb = datao.iloc[2002,2:22].std() # 20Mb


for i in range(20):
     datao.iloc[:,i+2] = datao.iloc[:,i+2] / (datao['avee'][11])
#datao.iloc[:,2:22] = datao.iloc[:,2:22] *.3
#print (datao.iloc[:,i+2][0])
plt.rcParams['figure.dpi'] = 150
# =============================================================================
# l1 = datao.iloc[9,2:22].std()
# l2 = datao.iloc[99,2:22].std()
# l3 = datao.iloc[999,2:22].std()
# l4 = datao.iloc[1999,2:22].std()
# print(l1)
# print(l2)
# print(l3)
# print(l4)
# =============================================================================
# https://matplotlib.org/stable/gallery/color/named_colors.html
#datao=datao.iloc[9:2242,:]
ax1 = datao.plot(linestyle='solid', x='Column1', y='Cell1', color='r') 
#https://towardsdatascience.com/how-xticks-and-xticklabels-really-work-a-walkthrough-aff80755838
ax1.set_yscale('log')
ax1.set_xscale('log')


ax1.get_yaxis().set_minor_formatter(matplotlib.ticker.OldScalarFormatter())
ax1.set(yticks=[0.6, 0.8, 6, 8])
ax1.get_legend().remove()
#ax1.set(xticks=[10**4, 10**5, 10**6, 10**7])
ax2 = datao.plot(linestyle='solid', x='Column1', y='Cell2', color='g', ax=ax1)
ax2.get_legend().remove()
ax3 = datao.plot(linestyle='solid', x='Column1', y='Cell3', color='limegreen', ax=ax1)
ax3.get_legend().remove()
ax4 = datao.plot(linestyle='solid', x='Column1', y='Cell4', color='darkorange', ax=ax1)
ax4.get_legend().remove() 
ax5 = datao.plot(linestyle='solid', x='Column1', y='Cell5', color='royalblue', ax=ax1)
ax5.get_legend().remove()
ax6 = datao.plot(linestyle='solid', x='Column1', y='Cell6', color='yellow', ax=ax1)
ax6.get_legend().remove()
ax7 = datao.plot(linestyle='solid', x='Column1', y='Cell7', color='m', ax=ax1)
ax7.get_legend().remove()
ax8 = datao.plot(linestyle='solid', x='Column1', y='Cell8', color='deeppink', ax=ax1)
ax8.get_legend().remove()
ax9 = datao.plot(linestyle='solid', x='Column1', y='Cell9', color='violet', ax=ax1)
ax9.get_legend().remove()
ax10 = datao.plot(linestyle='solid', x='Column1', y='Cell10', color='lightgreen', ax=ax1)
ax10.get_legend().remove()
ax11 = datao.plot(linestyle='solid', x='Column1', y='Cell11', color='gold', ax=ax1)
ax11.get_legend().remove()
ax12 = datao.plot(linestyle='solid', x='Column1', y='Cell12', color='c', ax=ax1)
ax12.get_legend().remove()
ax13 = datao.plot(linestyle='solid', x='Column1', y='Cell13', color='k', ax=ax1)
ax13.get_legend().remove()
ax14 = datao.plot(linestyle='solid', x='Column1', y='Cell14', color='olive', ax=ax1)
ax14.get_legend().remove()
ax15 = datao.plot(linestyle='solid', x='Column1', y='Cell15', color='slateblue', ax=ax1)
ax15.get_legend().remove()
ax16 = datao.plot(linestyle='solid', x='Column1', y='Cell16', color='lightpink', ax=ax1)
ax16.get_legend().remove()
ax17 = datao.plot(linestyle='solid', x='Column1', y='Cell17', color='greenyellow', ax=ax1)
ax17.get_legend().remove()
ax18 = datao.plot(linestyle='solid', x='Column1', y='Cell18', color='peru', ax=ax1)
ax18.get_legend().remove()
ax19 = datao.plot(linestyle='solid', x='Column1', y='Cell19', color='tomato', ax=ax1)
ax19.get_legend().remove()
ax20 = datao.plot(linestyle='solid', x='Column1', y='Cell20', color='maroon', ax=ax1)
ax20.get_legend().remove()
plt.xlim(10000,26500000)
plt.ylim(0.15,16)

plt.grid(True)
#plt.legend(loc='upper left', prop={"size":4.25}) 
plt.xlabel("Genomic Distance (bp)"+"\n Experiment", fontweight='bold')
plt.ylabel("<Rs>", fontweight='bold')
print(ax1 == ax2 == ax3 == ax4 == ax5 == ax6 == ax7 == ax8 == ax9 == ax10 == ax11 == ax12 == ax13 == ax14 == ax15 == ax16 == ax17 == ax18 == ax19 == ax20)  # True

