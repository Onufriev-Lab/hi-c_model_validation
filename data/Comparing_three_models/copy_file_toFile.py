import pandas as pd

# Read the CSV files
x_df = pd.read_csv('random_number_10_times_Alber_LASTTT.csv')  # Assuming file_x.csv has 20 rows and 10 columns
y_df = pd.read_csv('file_yy.csv')  # Assuming file_y.csv has one column

# Create a function to find the value from y_df based on row number
def get_value(row_num, y_data):
    return y_data.iloc[row_num - 1, 0] if row_num <= len(y_data) else None

# Iterate through each cell in x_df and find the corresponding value in y_df
modified_data = []
for col in x_df.columns:
    new_col_data = []
    for val in x_df[col]:
        new_val = get_value(val, y_df)
        new_col_data.append(new_val)
    modified_data.append(new_col_data)

# Create a new DataFrame with modified data
modified_df = pd.DataFrame(modified_data).transpose()
modified_df.columns = [f'{col}_Y_value' for col in x_df.columns]  # Rename columns

# Save the modified data to a new CSV file
modified_df.to_csv('modified_file_x.csv', index=False)

