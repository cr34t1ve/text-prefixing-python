import os
import sys
import getpass
import datetime

def check_input_file(input_file):
    if not os.path.exists(input_file):
        print(f"Error: The file {input_file} does not exist.")
        sys.exit(1)

def get_output_file_path(output_file):
    if not os.path.isabs(output_file):
        # on windows
        # output_file = os.path.join('c:\\output-folder', output_file)
        output_file = os.path.abspath(output_file)
    return output_file

def handle_output_file(output_file):
    if os.path.exists(output_file):
        choice = input("The output file already exists. Do you want to overwrite it? (yes/no): ")
        if choice.lower() == 'yes':
            return output_file
        else:
            new_file = input("Enter a new filename: ")
            return get_output_file_path(new_file)
    else:
        return output_file

def write_header(output_file):
    with open(output_file, 'w') as f:
        f.write(f"File created by: {getpass.getuser()} on {os.name}\n")
        f.write(f"File created on: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S.%f')}\n")

def process_file(input_file, output_file):
    try:
        with open(input_file, 'r') as in_file, open(output_file, 'a') as out_file:
            for line in in_file:
                out_file.write(f"{datetime.datetime.now().strftime('%H:%M:%S.%f')}: {line}")
    except Exception as e:
        print(f"Error occurred while writing to the file: {e}")
        sys.exit(1)

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    check_input_file(input_file)
    output_file = handle_output_file(get_output_file_path(output_file))
    write_header(output_file)
    process_file(input_file, output_file)

if __name__ == "__main__":
    main()