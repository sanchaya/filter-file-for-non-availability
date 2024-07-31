# filter-file-for-non-availability
Check if the file exists or not from a list of files available in a csv, create new csv with available and missing file names. 


1. Reading the Input CSV: The script reads the input CSV file using csv.DictReader.
2. Filtering the Rows: It checks for file existence and separates the rows into existing_rows and missing_rows.
3. Writing the Output CSV: Writes the existing_rows to the output_csv.
4. Writing the Missing Files CSV: Writes the missing_rows to a separate CSV file named missing_csv.
5. You can save this script as filter_csv_with_missing.py and run it in the directory containing your input CSV file. Make sure to replace 'input.csv', 'filtered_output.csv', and 'missing_files.csv' with the actual names of your input and output files, if they are different.
