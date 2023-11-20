
input_file = "outputVMD.mol3"
output_file = "output.mol3"

# Initialize counters
counter = 1

# Create a dictionary to store mappings of old numbers to new counters
number_mapping = {}

# Open the input and output files
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        # Check if the line starts with "AAA"
        if line.startswith("AAA"):
            # Split the line by tabs
            parts = line.strip().split('\t')
            if len(parts) >= 2:
                # Get the old number from the first column
                old_number = parts[0]
                
                # Replace the old number with the new counter
                new_number = str(counter)
                number_mapping[old_number] = new_number
                
                # Increment the counter
                counter += 1
                
                # Write the updated line to the output file
                outfile.write("{}\t{}\n".format(new_number, '\t'.join(parts[1:])))
        # Check if the line starts with "BBB"
        elif line.startswith("BBB"):
            # Split the line by tabs
            parts = line.strip().split('\t')
            if len(parts) >= 2:
                # Get the old number from the second column
                old_number = parts[1]
                
                # Replace the old number with the corresponding new counter
                if old_number in number_mapping:
                    new_number = number_mapping[old_number]
                    # Write the updated line to the output file
                    outfile.write("{}\t{}\t{}\n".format(parts[0], new_number, '\t'.join(parts[2:])))
                else:
                    # If the old number is not found in the mapping, write the line as is
                    outfile.write(line)
        else:
            # For other lines, write them to the output file as is
            outfile.write(line)

# Print a message indicating the process is complete
print("File processing complete. Output written to", output_file)
