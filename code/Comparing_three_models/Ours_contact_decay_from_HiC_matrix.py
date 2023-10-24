# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 15:21:35 2023

@author: samir
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 16:19:55 2023

@author: samir
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.lines
# Read the CSV file into a DataFrame
df = pd.read_csv('contact_decay.csv')

# Extract the x and y values from the DataFrame

for i in range(1):
     df.iloc[:,i+3] = df.iloc[:,i+3] / (df['avee'][1])
     
#ax1 = df.plot(linestyle='solid', x='Column1', y='Rs', color='r') 
plt.plot(df['Column1'], df['Rs'], linestyle='solid', color='r')
#https://towardsdatascience.com/how-xticks-and-xticklabels-really-work-a-walkthrough-aff80755838
plt.yscale('log')
plt.xscale('log')


#plt.get_yaxis().set_minor_formatter(matplotlib.ticker.OldScalarFormatter())
plt.tick_params(axis='y', which='minor', labelsize=13)
xtick_labels = ['100 kb', '1 Mb', '10 Mb', '13 Mb', '20 Mb']
xtick_positions = [100000, 1000000, 10000000, 13000000, 20000000]
plt.xticks(xtick_positions, xtick_labels)

xticks = plt.xticks(xtick_positions, xtick_labels, rotation=45)

for tick in xticks[1]:
    tick.set_fontweight('bold')
    
# Set custom ticks and labels for y-axis
'''ytick_labels = [0.8, 2, 3, 4]
ytick_positions = [ 0.8, 2, 3, 4]
plt.yticks(ytick_positions, ytick_labels)'''
# Plot the 2D line
#plt.plot(x, y)
# Set minor formatter for the y-axis
ax = plt.gca()
ax.yaxis.set_minor_formatter(ticker.OldScalarFormatter())

# Set the font size for the minor y-axis ticks
ax.tick_params(axis='y', which='minor', labelsize=13)

#=========================================================================================================
# Define the regions where you want to add line segments
region_thresholds = [100000, 230000, 500000, 1000000, 10000000]  # Example region thresholds

df = df.sort_values('Column1')
x = df['Column1']
y = df['Rs']
# Create a new figure and plot the existing line
plt.figure()
plt.plot(df['Column1'], df['Rs'], label='Existing Line')
plt.yscale('log')
plt.xscale('log')
# Set the offset value for the line segments (adjust as needed)
offset = 0.09
offset_text = 0.19
# Iterate over the regions and add line segments parallel to the curve
for i in range(len(region_thresholds)-1):
    region_start = region_thresholds[i]
    region_end = region_thresholds[i+1]

    # Find the indices corresponding to the region
    start_index = np.where(x >= region_start)[0][0]
    end_index = np.where(x >= region_end)[0][0]

    # Calculate the local slope within the region
    slope = (np.log10(y[end_index]) - np.log10(y[start_index])) / (np.log10(x[end_index]) - np.log10(x[start_index]))

    # Calculate the line segment
    segment_x = np.linspace(region_start, region_end, 10)
    segment_y = 10 ** (np.log10(y[start_index]) + slope * (np.log10(segment_x) - np.log10(x[start_index])))


    # Add the offset to the line segment y-values
    segment_y += offset
    
    # Plot the line segment
    plt.plot(segment_x, segment_y, color='red', linestyle='--')

    # Add slope annotation next to the line segment
    annotation_x = (region_start + region_end) / 2
    annotation_y = 10 ** (np.log10(y[start_index]) + slope * (np.log10(annotation_x) - np.log10(x[start_index])))
    # Convert the absolute value of the slope to string
    slope_abs_str = f'{abs(slope):.2f}'

    # Create a mapping of digit to Unicode superscript character
    superscript_mapping = {
        '0': '\u2070',
        '1': '\u00b9',
        '2': '\u00b2',
        '3': '\u00b3',
        '4': '\u2074',
        '5': '\u2075',
        '6': '\u2076',
        '7': '\u2077',
        '8': '\u2078',
        '9': '\u2079',
        '.': '\u22C5'
    }
    
    # Replace each digit in the string with its corresponding superscript character
    slope_text = ''.join(superscript_mapping.get(digit, digit) for digit in slope_abs_str)

    # Manually adjust the vertical position of the superscript text
    offset_superscript = 0.3
    plt.text(annotation_x, annotation_y + offset_text, f's {slope_text}', fontsize=8, ha='center', va='bottom')

#=========================================================================================================
# Set labels and title for the plot
plt.xlabel('Genomic Distance'+"\n Sexton2012 Experiment", fontsize=14)
plt.ylabel('Rs ~ P^{-1/3}', fontsize=14)
plt.title('Rs plot for experiment')

# Display the plot
plt.show()
