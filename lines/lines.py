import linecache
import sys

def main():
    # Check for too few arguments
    if len(sys.argv) < 2:
        sys.exit("Usage: python script.py <file_path.py>")

    # Check for too many arguments
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")

    # Extract the file path from command-line arguments
    file_path = sys.argv[1]

    # Check if the file path ends with '.py' and if the file exists
    if not file_path.endswith(".py") or not it_exists(file_path):
        sys.exit("Not a valid Python file")

    # Count lines of code in the file
    lines_of_code = count_lines_of_code(file_path)
    print(lines_of_code)

def count_lines_of_code(file_path):
    # Open the file and read its lines
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Count non-blank, non-comment lines
    code_lines = 0
    for line in lines:
        # Exclude blank lines
        if line.strip():
            # Exclude lines starting with #
            if not line.strip().startswith('#'):
                code_lines += 1

    return code_lines

def it_exists(check_file):
    # Check if the file exists
    try:
        with open(check_file, 'r'):
            pass
        return True
    except FileNotFoundError:
        return False

if __name__ == "__main__":
    # Execute the main function if the script is run directly
    main()
