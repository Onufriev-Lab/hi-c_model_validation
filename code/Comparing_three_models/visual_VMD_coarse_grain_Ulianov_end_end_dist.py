#Thanks to GPT 3.5 to help me to write this script.
# In line 48, 2,190 needs to be there instead of 2,243, since from 2,191 to the end, is
# heterochromatin, not TAD regions (Euchromatin)

import numpy as np


def write_lines_to_new_file(lines, output_filename):
    with open(output_filename, 'a') as output_file:
        for line in lines:
            output_file.write(line)
            


def read_file(filename):
    atom_section = False
    coordinates = []
    aa = 0
    output_filename = 'outputVMD.txt'  # Replace with your output file name
    line_count = 0
    lines_to_write = []
    col3_sum = 0
    col4_sum = 0
    col5_sum = 0
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
                        line_count += 1
                        if line_count % 12 == 1:  # Check if it's the 1st line in every 10 lines
                        
                            lines_to_write.append(line)
                        else:
                            col3_sum += int(parts[2])
                            col4_sum += int(parts[3])
                            col5_sum += int(parts[4])
                    except ValueError:
                        print(f"Ignoring line: {line.strip()}. Invalid coordinate values.")
                else:
                    print(f"Ignoring line: {line.strip()}. Insufficient data.")
        
    write_lines_to_new_file(lines_to_write, output_filename)
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
filename = 'a8.mol2'  # Replace with the actual file name
coordinates = read_file(filename)
   

# if __name__ == '__main__':
#     main()