import sys
import os
import pandas as pd

# Get list of XLSX files from command line arguments
xlsx_files = sys.argv[1:]

# Iterate over each XLSX file
for file in xlsx_files:
    # Get the size of the file in bytes
    file_size = os.path.getsize(file)
    
    # Read the Excel file
    xls = pd.ExcelFile(file)
    
    # Iterate over each sheet in the Excel file
    for sheet_name in xls.sheet_names:
        # Read the sheet into a DataFrame
        df = pd.read_excel(xls, sheet_name)
        
        # Display the number of rows, columns, and file size
        print(f"|{file}|{file_size}|{df.shape[1]}|{df.shape[0]}|")
