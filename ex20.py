from sys import argv

script, input_file = argv

# Takes f as an argument which is a file and prints
# the contents of the file
def print_all(f):
    print(f.read())

# Takes in an argument which in this case would be a file
# and passes that through the seek function
def rewind(f):
    f.seek(0)

# The following function takes in 2 arguments
# Then prints the number passed First
# Then reads the line from the read head's current location
def print_a_line(line_count, f):
    print(line_count, f.readline(), end="")

current_file = open(input_file)

print("First let's print the whole file:\n")
# Calls the print_all function
print_all(current_file)

print("Now let's rewind, kind of line a tape.")
#Calls the rewind function
rewind(current_file)

print("Let's print three lines:")

# Create an integer of 1 and pass that to the print_a_line
# function
current_line = 1
print_a_line(current_line, current_file)


# Increment the integer by 1 and pass that to the print_a_line
# function. x+=y is the same as x = x+y
current_line += 1
print_a_line(current_line, current_file)

# Increment the integer by 1 and pass that to print_a_line
# function
current_line += 1
print_a_line(current_line, current_file)
