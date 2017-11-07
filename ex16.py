from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")

#Pressing CTRL+C while a python program is running will
#case python to raise a KeyboardInterrupt exception
print("If you don't want that, hit CTRL-C (^C).")

#Pressing Return will continue to the next instruction
print("If you do want that, hit RETURN")

input("?")

print("Opening the file...")
#'w' means it's a write-able file
target = open(filename,'w')


print("Truncating the file. Goodbye!")
#Empties the file
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

target.write(f"{line1}\n{line2}\n{line3}")

print("And finally, we close it.")
target.close()

print("But let's print your new file!")
temp = open(filename)
print(temp.read())
