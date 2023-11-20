# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 11:39:30 2023

@author: samir
"""

import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Load your data
# data= pd.read_csv('1st_.csv')
# data= pd.read_csv('2nd_.csv')
# data= pd.read_csv('3rd_.csv')
# data= pd.read_csv('4th_.csv')
# data= pd.read_csv('5th_.csv')
# data= pd.read_csv('6th_.csv')
# data= pd.read_csv('7th_.csv')
# data= pd.read_csv('8th_.csv')
# data= pd.read_csv('9th_.csv')
data= pd.read_csv('10th_.csv')




# Normalize the data as you did before
for i in range(2, 22):  # Columns containing curve data
    curve_name = data.columns[i]
    data[curve_name] = data[curve_name] / data['avee'].iloc[0]
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
    
# Calculate the mean of all curves


import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have a single CSV file with multiple sheets and each sheet represents a dataset.
# You can specify the filename and the sheet names like this:
csv_filename = "new_sigma_10times_Alber_10sheets.xlsx"
sheet_names = ["Sheet1", "Sheet2", "Sheet3", "Sheet4", "Sheet5",
               "Sheet6", "Sheet7", "Sheet8", "Sheet9", "Sheet10"]

# Create an empty DataFrame to store the combined data from all sheets
combined_data = pd.DataFrame()

# Load data from each sheet and combine it into the combined_data DataFrame
for sheet_name in sheet_names:
    df = pd.read_excel(csv_filename, sheet_name=sheet_name)
    combined_data = pd.concat([combined_data, df.iloc[:, 2:22]], axis=1)

# Calculate the mean curve for all the combined data
overall_mean_curve = combined_data.mean(axis=1)

# Load the modified_SD column from the 10th sheet for shading
df_10th_sheet = pd.read_excel(csv_filename, sheet_name="Sheet10")
shaded_region = data['modified_SD']

# Plot the overall mean curve with shaded region
plt.figure(figsize=(10, 6))
plt.plot(overall_mean_curve, label='Overall Mean Curve', color='b')
plt.fill_between(
    overall_mean_curve.index,
    overall_mean_curve - shaded_region,
    overall_mean_curve + shaded_region,
    color='b',
    alpha=0.2,
    label='Shaded Region (modified_SD)'
)
# plt.xlabel('Data Point Index')
# plt.ylabel('Mean Curve Value')
# plt.legend()
# plt.title('Overall Mean Curve with Shaded Region (modified_SD)')
# plt.grid(True)
# plt.show()

# Create a figure and axis
plt.rcParams['figure.dpi'] = 300
fig, ax1 = plt.subplots()

# Use your modified SD values in the shading calculation
shading =  2* data['modified_SD']  # Replace 'Modified_SD' with the name of your modified SD column

# Add fill_between for the shaded region
ax1.fill_between(data['Column1'], overall_mean_curve - shading, overall_mean_curve + shading, color='lightcoral', alpha=0.5, label='2 Sigma Range')

# Plot the mean curve
ax1.plot(data['Column1'], overall_mean_curve, 'r-', label='Mean Curve')

# Set the x-axis to logarithmic scale
ax1.set_xscale('log')

# Customize tick positions and labels
xtick_labels = ['10 k', '118 k', '1 M', '10 M', '13 M']
xtick_positions = [10000, 118000, 1000000, 10000000, 13000000]

xticks = ax1.set_xticks(xtick_positions)
ax1.set_xticklabels(xtick_labels, rotation=45)

# Customize y-axis tick positions
ax1.set(yticks=[0.1, 0.8, 2, 3, 4, 5, 6, 8, 10, 11, 12, 15])

# Set axis labels
ax1.set_xlabel(r"$Genomic\ Distance\ [bp]$", fontsize=16)
ax1.set_ylabel("<Rs>" + "\nNormalized by Average TAD size", fontsize=14)

# Add legend
ax1.legend()

# Set the plot limits and grid
plt.xlim(10000, 26500000)
plt.ylim(0.001, 12)
plt.grid(True)

# Show the plot
plt.show()
