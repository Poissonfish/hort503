from sys import argv
# Get import file from user intput
script, input_file = argv


# Define read file function
def print_all(f):
    print(f.read())


# Define a function for seeking a specific position of given file
def rewind(f):
    f.seek(0)


# Define a function for printing sepecific line from given file
def print_a_line(line_count, f):
    print(line_count, f.readline())


# Open input file
current_file = open(input_file)

# Print a string
print("First let's print the whole file:\n")

# Print all file content
print_all(current_file)

# Print a string
print("Now let's rewind, kind of like a tape.")

# Reset the pointer
rewind(current_file)

# Print a string
print("Let's print three lines:")

# Print one line at a time
current_line = 1
print_a_line(current_line, current_file)

# Push pointer to next line and print
current_line = current_line + 1
print_a_line(current_line, current_file)

# Push pointer to next line and print
current_line = current_line + 1
print_a_line(current_line, current_file)
