# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 13:18:00 2023

@author: samir
"""

import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV files
df = pd.read_csv('Rg_all_topologies.csv')
#df = pd.read_csv('Rg_all_topologies.csv')

df2 = pd.read_csv('Rg_Alber.csv')
#df3 = pd.read_csv('end_end_distance_Ulianov2021.csv')

# Extract the data from the DataFrames
values = df.iloc[:, 13].values.ravel()
values2 = df2.values.ravel()
#values3 = df3.iloc[:, 2].values.ravel()

# Combine all the values into one list for boxplot
all_values = [values, values2]#, values3]

# Create the main box plot with the combined values
plt.figure(figsize=(10, 6))

# Create the box plot with custom colors and no shadows
box_plot = plt.boxplot(all_values, vert=True, positions=[1, 2], widths=0.6, patch_artist=True, showmeans=True, meanline=True, meanprops=dict(linewidth=2, color='green'), boxprops=dict(facecolor='red', edgecolor='black'))
plt.rcParams['figure.dpi'] = 300

# Set different box colors
for box, color in zip(box_plot['boxes'], ['darkblue', 'green']):
    box.set(facecolor=color)

# Set median line color
for median in box_plot['medians']:
    median.set(color='black')

# Set means color
for mean in box_plot['means']:
    mean.set(marker='.', color='green', alpha=0.7)

# Customize x-axis tick labels without "dataset" word
plt.xticks([1, 2], ['this work', 'Li 2017'], fontsize=22)

# Customize y-axis tick labels
plt.yticks(fontsize=15)

# Add gridlines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add labels to axes
plt.xlabel('Methods', fontsize=24, weight='bold')
plt.ylabel('Radius of Gyration chr X ($\mu$m)', fontsize=22)

# Show the plot
plt.tight_layout()
plt.show()
