import pandas as pd
import glob # Helps find files whose names match a pattern
import os

# Function for Combining CSVs
def combine_csvs(folder_path, file_prefix, output_name):
    # Contains all matching CSV files in order
    file_list = sorted(glob.glob(os.path.join(folder_path, f"{file_prefix}*.csv")))

    # Empty list stores each CSV file after it is read
    all_dfs = []

    # Loop for each file path in file_list
    for file in file_list:
        print(f"Reading: {os.path.basename(file)}")
        df = pd.read_csv(file, low_memory=False)
        all_dfs.append(df)

    # Combines all dfs into one big df
    master_df = pd.concat(all_dfs, ignore_index=True)

    # Save the final combined CSV file
    output_path = os.path.join(folder_path, output_name)
    master_df.to_csv(output_path, index=False)

    print(f"\nFinished combining {len(file_list)} files.")
    print(f"Saved to: {output_path}")
    print(f"Shape: {master_df.shape}\n")



# Sold files
sold_folder = r"/Users/cynthiagao/PycharmProjects/IDX Exchange Internship/IDX Files/CRMLSSold"
combine_csvs(sold_folder, "CRMLSSold", "CRMLSSold_Master.csv")