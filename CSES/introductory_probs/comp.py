
def read_file(filename):
    """Reads a file and returns a set of strings."""
    with open(filename, 'r') as f:
        lines = f.readlines()
        # The first line indicates the number of rows of strings
        num_rows = int(lines[0].strip())
        # Read the next `num_rows` lines as strings
        strings = {line.strip() for line in lines[1:num_rows + 1]}
    return strings

def find_unique_strings(file_a, file_b):
    """Finds strings unique to each file."""
    strings_a = read_file(file_a)
    strings_b = read_file(file_b)

    # Find strings in A but not in B, and vice versa
    only_in_a = strings_a - strings_b
    only_in_b = strings_b - strings_a

    return only_in_a, only_in_b

def main():
    file_a = "a"
    file_b = "b"

    only_in_a, only_in_b = find_unique_strings(file_a, file_b)

    print("Strings only in A:")
    for string in sorted(only_in_a):
        print(string)

    print("\nStrings only in B:")
    for string in sorted(only_in_b):
        print(string)

if __name__ == "__main__":
    main()
