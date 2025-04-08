# -*- coding: utf-8 -*-

################################################################################################################################
## This code reads the <Rs> values for 18 selected snapshots from 18 trajectories in Tolokh (2023) and plots the relative <Rs>## 
## for each corresponding snapshot in a single graph. Additionally, it prints the relative C.V. across the genome.            ##
################################################################################################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.ticker as ticker
import csv

# Define the filename
filename = "Rs_data_Tolokh_final_UpConversionPlusRelative.csv"

#data = pd.read_csv('/Users/samir/Desktop/lamin_mutant_new.csv')
data = pd.read_csv('/Users/samir/C Drive/Old_Desktop/ten_times_tolokh_10kb/nineth_.csv')

   
#9898 is the largest one
seed = 61001
#seed = 9898
#seed = 765
np.random.seed(seed) 
  
mu, sigma = 0, 0.04
s2 = np.random.normal(mu, sigma, 18)

#for i in range(18):
#  data.iloc[1:, i + 1] += s2[i] 
    
 
#for i in range(18):
#  data.iloc[:,i+1] = data.iloc[:,i+1] / (data['avee1'])  
  
 
# Save the DataFrame to a CSV file
try:
    data.to_csv(filename, index=False, encoding="utf-8")
    print(f"Data written to {filename} successfully.")

except Exception as e:
    print(f"An error occurred: {e}")
   


data_sizes = [
    ("13kb", 0),
    ("118kb", 1),
    ("200kb", 2),
    ("300kb", 3),
    ("400kb", 4),
    ("500kb", 4),
    ("600kb", 5),
    ("700kb", 6),
    ("800kb", 7),
    ("900kb", 8),
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
    ("10Mb", 85),
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
    value = data.iloc[index, 1:18].std()
    value_1 = data.iloc[index, 1:18].mean()
    globals()[variable_name] = value
    print(f"{size} = {value}")

plt.rcParams['figure.dpi'] = 300
ax1 = data.plot(linestyle='solid', x='Genomic_Distance', y='1st', color='r')
ax1.set_yticklabels(ax1.get_yticks(), fontsize=13)
ax1.set_yticks(ax1.get_yticks())

import matplotlib.patches as patches
# Original y-coordinate calculation
original_y = ax1.get_ylim()[0] + 0.0085

# Shift the y-coordinate upwards (e.g., by 0.1 units)
shifted_y = original_y - 0.1

# Create the rectangle with the shifted y-coordinate
rect = patches.Rectangle((13100, shifted_y), 103000, 0.5, linewidth=0.5, edgecolor='blue', facecolor='gray', alpha=0.3)

#Add the rectangle to the plot
ax1.add_patch(rect)


new_y_ticks = [1, 2, 3, 4]  # Adjust these values as needed
#new_y_ticks = [1, 5, 10, 12, 15]
new_y_tick_labels = [str(tick) for tick in new_y_ticks]  # Convert to strings if necessary

ax1.set_yticks(new_y_ticks)
ax1.set_yticklabels(new_y_tick_labels)

ax1.set_xscale('log')
#ax1.set_yscale('log')

ax1.yaxis.set_minor_formatter(ticker.ScalarFormatter())


xtick_labels = ['10 k', '100 k', '1 M', '10 M']
xtick_positions = [10000, 100000, 1000000, 10000000]

xticks = plt.xticks(xtick_positions, xtick_labels, rotation=45)

for tick in xticks[1]:
    tick.set_fontweight('bold')

#ax1.set(yticks=[1, 5, 10, 12, 15])
ax1.set(yticks=[1, 2, 3, 4])
ax1.get_legend().remove()

ax2 = data.plot(linestyle='solid', x='Genomic_Distance', y='2nd', color='maroon', ax=ax1)
ax2.get_legend().remove()
ax3 = data.plot(linestyle='solid', x='Genomic_Distance', y='3rd', color='violet', ax=ax1)
ax3.get_legend().remove()
ax4 = data.plot(linestyle='solid', x='Genomic_Distance', y='4th', color='darkorange', ax=ax1)
ax4.get_legend().remove() 
ax5 = data.plot(linestyle='solid', x='Genomic_Distance', y='5th', color='tomato', ax=ax1)
ax5.get_legend().remove() 
ax6 = data.plot(linestyle='solid', x='Genomic_Distance', y='6th', color='yellow', ax=ax1)
ax6.get_legend().remove() 
ax7 = data.plot(linestyle='solid', x='Genomic_Distance', y='7th', color='m', ax=ax1)
ax7.get_legend().remove() 
ax8 = data.plot(linestyle='solid', x='Genomic_Distance', y='8th', color='deeppink', ax=ax1)
ax8.get_legend().remove()
ax9 = data.plot(linestyle='solid', x='Genomic_Distance', y='9th', color='g', ax=ax1)
ax9.get_legend().remove()
ax10 = data.plot(linestyle='solid', x='Genomic_Distance', y='10th', color='lightgreen', ax=ax1)
ax10.get_legend().remove()
ax11 = data.plot(linestyle='solid', x='Genomic_Distance', y='11th', color='gold', ax=ax1)
ax11.get_legend().remove()
ax12 = data.plot(linestyle='solid', x='Genomic_Distance', y='12th', color='peru', ax=ax1)
ax12.get_legend().remove()
ax13 = data.plot(linestyle='solid', x='Genomic_Distance', y='13th', color='lightpink', ax=ax1)
ax13.get_legend().remove()
ax14 = data.plot(linestyle='solid', x='Genomic_Distance', y='14th', color='olive', ax=ax1)
ax14.get_legend().remove()
ax15 = data.plot(linestyle='solid', x='Genomic_Distance', y='15th', color='royalblue', ax=ax1)
ax15.get_legend().remove()
ax16 = data.plot(linestyle='solid', x='Genomic_Distance', y='16th', color='k', ax=ax1)
ax16.get_legend().remove()
ax17 = data.plot(linestyle='solid', x='Genomic_Distance', y='17th', color='greenyellow', ax=ax1)
ax17.get_legend().remove()  
ax18 = data.plot(linestyle='solid', x='Genomic_Distance', y='18th', color='c', ax=ax1)
ax18.get_legend().remove()

plt.xlim(10000,26500000)

plt.ylim(0.001,2)

font_properties = {'family': 'times new roman', 'weight': 'normal', 'size': 24}

plt.text(0.09, 0.8, "Tolokh 2023",  fontdict= font_properties, transform=ax1.transAxes, bbox=dict(facecolor='white', alpha=0.8))
plt.grid(True)


plt.xlabel(r"$Genomic\ Distance\ [bp]$" , fontsize=22)
#plt.ylabel("Relative <Rs>", fontsize=22)
plt.ylabel("<Rs> [micron]", fontsize=22)
#plt.ylabel(r"$\langle R_s \rangle$ [$\mu$m]", fontsize=22)
plt.ylabel(r"Relative $\langle R_s \rangle$", fontsize=22)


print(ax1)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)

plt.show()


