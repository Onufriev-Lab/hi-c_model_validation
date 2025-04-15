# -*- coding: utf-8 -*-

################################################################################################################################
## This code reads the <Rs> values for 18 selected snapshots from 18 trajectories in Tolokh (2023) and plots the relative <Rs>## 
## for each corresponding snapshot in a single graph. Additionally, it prints the C.H. across the genome.            ##
################################################################################################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.ticker as ticker
import csv

# Output file
filename = "Rs_data_Tolokh_final_UpConversionPlusRelative.csv"

# Input file
data = pd.read_csv('../Data/3rd_set.csv')

   
#9898 is the largest one
seed = 61001
#seed = 9898
#seed = 765
np.random.seed(seed) 
  
mu, sigma = 0, 0.04
s2 = np.random.normal(mu, sigma, 18)
  
 
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
