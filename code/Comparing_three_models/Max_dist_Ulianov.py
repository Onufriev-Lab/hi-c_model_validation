
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 18:54:33 2023

@author: samir
"""

# In line 48, 2,190 needs to be there instead of 2,243, since from 2,191 to the end, is
# heterochromatin, not TAD regions (Euchromatin)
import math
import numpy as np

def calculate_distance(coord1, coord2):
    return np.linalg.norm(coord1 - coord2)

def calculate_squared_distance(coord1, aveCoord):
    fixed_coord = aveCoord
    diff = np.array(coord1) - fixed_coord
    squared_distance = np.dot(diff, diff)
    return squared_distance

def read_file(filename):
    atom_section = False
    coordinates = []
    aa = 0
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('@<TRIPOS>ATOM'):
                atom_section = True
            elif line.startswith('@<TRIPOS>'):
                atom_section = False
            elif atom_section:
                parts = line.split()
                if len(parts) >= 5:
                    try:
                #         aa+=1
                #         if(aa==5): break
                        if int(parts[0]) >= 2243:
                            break
                        x, y, z = map(float, parts[2:5])
                        coordinates.append([x, y, z])
                        
                    except ValueError:
                        print(f"Ignoring line: {line.strip()}. Invalid coordinate values.")
                else:
                    print(f"Ignoring line: {line.strip()}. Insufficient data.")

    return np.array(coordinates)

def write_matrix_to_file(matrix, filename):
    with open(filename, 'w') as file:
        rows, cols = matrix.shape
        for i in range(rows):
            for j in range(cols):
                file.write(f"{matrix[i][j]:.4f} ")
            file.write("\n")

input_filename = 'input.txt'  # Replace with the actual input file name
#output_filename = 'output.txt'  # Replace with the desired output file name
filename = 'cell10.mol2'  # Replace with the actual file name
coordinates = read_file(filename)

aveCoordinates = [] 
aveCoordinates = np.mean(coordinates, axis=0)

squared_distance = np.zeros(len(coordinates))  # Initialize an array to store squared distances

maxDistance = 0
max_first_end = 0
max_second_end = 0
for i, coord in enumerate(coordinates):
    for j, coordj in enumerate(coordinates):     
        distance = calculate_distance(coordinates[i], coordinates[j])
        if (distance > maxDistance) :
            max_first_end = i;
            max_second_end = j;
            maxDistance = distance;

Max_Dist = maxDistance * 0.106
# Now squared_distance array contains squared distances for each set of coordinates
print("Sum of Squared Distances:", Max_Dist)
#diagonal_averages = calculate_diagonal_averages(distance_matrix)
#write_matrix_to_file(distance_matrix, output_filename)
#print("Distance matrix has been written to", output_filename)
#print("Diagonal Averages:", diagonal_averages)
   

# if __name__ == '__main__':
#     main()