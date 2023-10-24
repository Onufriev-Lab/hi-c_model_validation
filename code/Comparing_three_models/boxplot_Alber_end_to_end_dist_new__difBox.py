import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV files
df = pd.read_csv('Alber_end_end.csv')
df2 = pd.read_csv('end_end_400K_ours.csv')
df3 = pd.read_csv('end_end_distance_Ulianov2021.csv')

# Extract the data from the DataFrames
values = df.iloc[:, 0].values.ravel()
values2 = df2.values.ravel()
values3 = df3.iloc[:, 2].values.ravel()

# Combine all the values into one list for boxplot
all_values = [values, values2, values3]

# Create the main box plot with the combined values
plt.figure(figsize=(10, 6))

# Custom box plot properties
box_props = dict(
    patch_artist=True,
    boxprops=dict(facecolor='orange', edgecolor='black'),
    medianprops=dict(color='red'),
    whiskerprops=dict(color='black', linestyle='-'),
    capprops=dict(color='black'),
    flierprops=dict(marker='o', markersize=5, markerfacecolor='black'),
)

# Create the box plot
plt.boxplot(all_values, vert=True, positions=[1, 2, 3], widths=0.6, **box_props, showmeans=True, meanline=True, meanprops=dict(linewidth=2, color='green'))

# Customize x-axis tick labels without "dataset" word
plt.xticks([1, 2, 3], ['this work', 'Li 2017', 'Ulianov 2021'], fontsize=18)

# Customize y-axis tick labels
plt.yticks(fontsize=15)

# Add gridlines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add labels to axes
plt.xlabel('Methods', fontsize=18)
plt.ylabel('End-to-End distance chr X ($\mu$m)', fontsize=20)

# Add a title
#plt.title('Box Plots of End-to-End distance chrX', fontsize=20)

# Show the plot
plt.tight_layout()
plt.show()
