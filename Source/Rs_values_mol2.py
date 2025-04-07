
# In line 48, 2,190 needs to be there instead of 2,243, since from 2,191 to the end, is
# heterochromatin, not TAD regions (Euchromatin)

import numpy as np

def calculate_distance(coord1, coord2):
    return np.linalg.norm(coord1 - coord2)

def calculate_distance_matrix(coordinates):
    num_atoms = len(coordinates)
    distance_matrix = np.zeros((num_atoms, num_atoms))

    for i in range(num_atoms):
        for j in range(i+1, num_atoms):
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

    return averages


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
filename = 'b15.mol2'  # Replace with the actual file name
coordinates = read_file(filename)
distance_matrix = calculate_distance_matrix(coordinates)
diagonal_averages = calculate_diagonal_averages(distance_matrix)
#write_matrix_to_file(distance_matrix, output_filename)
#print("Distance matrix has been written to", output_filename)
print("Diagonal Averages:", diagonal_averages)
   

# if __name__ == '__main__':
#     main()
