from sys import argv
from os.path import exists
# OS.PATH is a flexible way Python is able to tell what
# operating system it is in
# Exists is a function that returns true of false depending
# on the existence of file and read/write permissions

# First is the script name
# Next is the file we are copying from
# Then the file we are copying to
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# We could do these two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()

indata = open(from_file).read()

# len is length of the file in bytes
print(f"The input file is {len(indata)} bytes long")

# exists is the function we importet and returns TRUE or FALSE
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# If the to_file doesn't exist, Python will create it
out_file = open(to_file, 'w')
# Take the indata and write it to the out_file
out_file.write(indata)

print("Alright, all done.")

out_file.close()
# in_file.close()
in_data.close()

#Entire program in a single line

#out_file = open(to_file, 'w').write(open(from_file).read())
