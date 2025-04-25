input_file = 'yourfile.txt'          # Input file name
output_file = 'line_lengths.txt'     # Output file name

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for i, line in enumerate(infile, start=1):
        length = len(line.strip())
        outfile.write(f"Line {i} : {length}\n")