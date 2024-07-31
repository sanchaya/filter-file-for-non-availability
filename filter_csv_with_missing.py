import csv
import os

def filter_csv(input_csv, output_csv, missing_csv):
    # Read the input CSV file
    with open(input_csv, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)
        fieldnames = reader.fieldnames

    # Initialize lists to hold existing and missing rows
    existing_rows = []
    missing_rows = []

    # Filter rows based on file existence
    for row in rows:
        if os.path.exists(row['file']):
            existing_rows.append(row)
        else:
            missing_rows.append(row)

    # Write the existing rows to the output CSV file
    with open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(existing_rows)

    # Write the missing rows to the missing CSV file
    with open(missing_csv, mode='w', newline='', encoding='utf-8') as missingfile:
        writer = csv.DictWriter(missingfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(missing_rows)

    print(f"Filtered CSV saved as {output_csv}")
    print(f"Missing files CSV saved as {missing_csv}")

# Define the input and output CSV filenames
input_csv = 'input.csv'
output_csv = 'filtered_output.csv'
missing_csv = 'missing_files.csv'

# Run the filter function
filter_csv(input_csv, output_csv, missing_csv)
