def parse_fixed_width_file(input_file, output_file, field_offsets):
    with open(input_file, 'r', encoding='utf-8') as infile:
        with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
            for line in infile:
                fields = [line[start:end].strip() for start, end in field_offsets]
                csv_line = ','.join(fields)  # Use a different delimiter if needed
                outfile.write(csv_line + '\n')

# Example usage:
if __name__ == '__main__':
    input_file = 'spec.txt'  # Replace with your actual input file
    output_file = 'output.csv'  # Replace with your desired output file
    # Specify field offsets (start, end) based on your fixed-width spec
    field_offsets = [(0, 10), (10, 20), (20, 30)]  # Adjust as needed
    parse_fixed_width_file(input_file, output_file, field_offsets)
