import csv
import sys
import os
def csv_parser(file, column_name, output_file):
    print(f"Parsing file: {file}")
    print(f"Extracting column name: {column_name}")
    print(f"Outputting to: {output_file}")  

    try:
        file = os.path.join('data', file)
        print(f"Processing file: {file}")
 
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            text_data = [row[column_name] for row in reader]
        
        print(f"Outputting text to output_file: {output_file}")

        with open(output_file, 'w') as o_file:
            o_file.write('\n'.join(text_data))

    except FileNotFoundError:
        print(f"Error: File {file} not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occured: {e}")
        sys.exit(1)
            

if __name__ == "__main__":
    print(len(sys.argv))
    if (len(sys.argv) != 4):
        print('Error missing args: Usage: python csv_parser.py <file_name: data.csv> <column_name: Dialogue> <output_file: output.txt>')
        sys.exit(1)
    else:
        csv_parser(sys.argv[1], sys.argv[2], sys.argv[3])
