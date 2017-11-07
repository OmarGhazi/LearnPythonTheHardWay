from sys import argv

script, filename = argv

#returns file object, in this case filename and put it in
#txt variable
txt = open(filename)

#print Here is your file with the file name
#then reads the object that's stored in txt variable
#which in this case is filename
print(f"Here is your file {filename}")
print(txt).read())

#This time the script is asking the user for the input
#In this case, asking for the filename
#Here the user can input any filename, it doesn't have
#to be the one that they just typed to run the script
print("Type the filename again:")
file_again = input("> ")

#txt_again is just like txt variable, in this case it's
#holding the file object of the latest information
#entered by the user, which is the filename after the input
txt_again = open(file_again)

#prints the new file on to the screen
print(txt_again.read())

#closing the file
txt.close()
txt_again.close()
