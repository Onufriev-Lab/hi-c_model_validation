import os
import numpy as np
import csv

def calculate_distance(coord1, coord2):
    return np.linalg.norm(coord1 - coord2)

def calculate_distance_matrix(coordinates):
    num_atoms = len(coordinates)
    distance_matrix = np.zeros((num_atoms, num_atoms))
    for i in range(num_atoms):
        for j in range(i + 1, num_atoms):
            distance = calculate_distance(coordinates[i], coordinates[j])
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance
    return distance_matrix

def calculate_diagonal_averages(matrix):
    num_rows, num_cols = matrix.shape
    max_diagonal = min(num_rows, num_cols)
    averages = np.zeros(max_diagonal)
    for i in range(max_diagonal):
        diagonal = np.diagonal(matrix, offset=i)
        averages[i] = np.mean(diagonal)
    return averages[1:]

def read_file(filename):
    atom_section = False
    coordinates = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except UnicodeDecodeError:
        with open(filename, 'r', encoding='latin-1') as file:
            lines = file.readlines()

    for line in lines:
        if line.startswith('@<TRIPOS>ATOM'):
            atom_section = True
        elif line.startswith('@<TRIPOS>'):
            atom_section = False
        elif atom_section:
            parts = line.split()
            if len(parts) >= 5:
                try:
                    if int(parts[0]) >= 2190:
                        break
                    x, y, z = map(float, parts[2:5])
                    coordinates.append([x, y, z])
                except ValueError:
                    print(f"Ignoring line: {line.strip()}. Invalid coordinate values.")
            else:
                print(f"Ignoring line: {line.strip()}. Insufficient data.")
    return np.array(coordinates)


def process_folder(folder_path, output_csv):
    mol2_files = [f for f in os.listdir(folder_path) if f.endswith('.mol2')]
    Rs_all = []
    file_names = []

    for mol2_file in mol2_files:
        full_path = os.path.join(folder_path, mol2_file)
        print(f"Processing: {mol2_file}")
        coordinates = read_file(full_path)
        if coordinates.size == 0:
            print(f"Skipping {mol2_file}, no valid coordinates.")
            continue
        distance_matrix = calculate_distance_matrix(coordinates)
        Rs = calculate_diagonal_averages(distance_matrix)
        Rs_all.append(Rs)
        file_names.append(mol2_file)

    # Transpose and pad Rs lists to match lengths
    max_len = max(len(rs) for rs in Rs_all)
    for i in range(len(Rs_all)):
        if len(Rs_all[i]) < max_len:
            Rs_all[i] = np.pad(Rs_all[i], (0, max_len - len(Rs_all[i])), 'constant', constant_values=np.nan)

    Rs_array = np.array(Rs_all).T  # Shape: (rows, num_files)
    row_averages = np.nanmean(Rs_array, axis=1)  # Final column: average per row (ignoring NaN)

    with open(output_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        header = file_names + ['Row_Average']
        writer.writerow(header)
        for row_vals, avg in zip(Rs_array, row_averages):
            writer.writerow(list(row_vals) + [avg])


    print(f"Rs values have been written to {output_csv}")

# Example usage:
folder_path = '/path_to_mol2_files'
output_csv = 'Rs_all_output.csv'
process_folder(folder_path, output_csv)
