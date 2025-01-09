def process_file(input_filename, output_filename):
  try:
    with open(input_filename, 'r') as infile:
      data = infile.read()

    with open(output_filename, 'w') as outfile:
      outfile.write(data + "\nThis line was added by the program.") 

  except FileNotFoundError:
    print(f"Error: Input file '{input_filename}' not found.")
  except IOError as e:
    print(f"An I/O error occurred: {e}")

if __name__ == "__main__":
  input_filename = input("Enter the name of the input file: ")
  output_filename = input("Enter the name of the output file: ")

  process_file(input_filename, output_filename)