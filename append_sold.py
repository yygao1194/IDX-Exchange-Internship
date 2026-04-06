import pandas as pd
import glob # Helps find files whose names match a pattern
import os

# Function for Combining CSVs
def combine_csvs(folder_path, file_prefix, output_name):
    # Contains all matching CSV files in order
    file_list = [
        f for f in sorted(glob.glob(os.path.join(folder_path, f"{file_prefix}*.csv")))
        if "Master" not in os.path.basename(f)
    ]
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

# Function for combining CSVs with Residential filter
def combine_csvs_residential(folder_path, file_prefix, output_name):
    # Contains all matching CSV files in order
    file_list = [
        f for f in sorted(glob.glob(os.path.join(folder_path, f"{file_prefix}*.csv")))
        if "Master" not in os.path.basename(f)
    ]

    # Empty list stores each CSV file after it is read
    all_dfs = []

    # Track total rows before concatenation
    total_rows_before_concat = 0

    # Loop through each file path in file_list
    for file in file_list:
        print(f"Reading: {os.path.basename(file)}")
        df = pd.read_csv(file, low_memory=False)

        # Count rows in this file before concatenation
        file_row_count = len(df)
        print(f"Rows in {os.path.basename(file)}: {file_row_count}")

        total_rows_before_concat += file_row_count
        all_dfs.append(df)

    # Combines all dfs into one big df
    master_df = pd.concat(all_dfs, ignore_index=True)

    # Row count after concatenation
    rows_after_concat = len(master_df)

    # Confirm row counts before and after concatenation
    print("\n--- Row Count Check for Concatenation ---")
    print(f"Total rows before concatenation: {total_rows_before_concat}")
    print(f"Total rows after concatenation: {rows_after_concat}")

    # Row count before Residential filter
    rows_before_filter = len(master_df)

    # Filter to PropertyType == 'Residential' only
    master_df = master_df[master_df["PropertyType"] == "Residential"]

    # Row count after Residential filter
    rows_after_filter = len(master_df)

    # Confirm row counts before and after Residential filter
    print("\n--- Row Count Check for Residential Filter ---")
    print(f"Rows before Residential filter: {rows_before_filter}")
    print(f"Rows after Residential filter: {rows_after_filter}")

    # Save the final combined CSV file
    output_path = os.path.join(folder_path, output_name)
    master_df.to_csv(output_path, index=False)

    print(f"\nFinished combining {len(file_list)} files.")
    print(f"Saved to: {output_path}")
    print(f"Final shape: {master_df.shape}\n")



# Sold files
sold_folder = r"/Users/cynthiagao/PycharmProjects/IDX Exchange Internship/IDX Files/CRMLSSold"
combine_csvs(sold_folder, "CRMLSSold", "CRMLSSold_Master.csv")

# Sold files - Residential
sold_folder = r"/Users/cynthiagao/PycharmProjects/IDX Exchange Internship/IDX Files/CRMLSSold"
combine_csvs_residential(sold_folder, "CRMLSSold", "CRMLSSold_Master_Residential.csv")
