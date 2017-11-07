##The following line declares types_of_people as an integer with a value of 10
types_of_people = 10
#The following line creates a variable with type integer and format string that
#includes types_of_people within the string
x=f"There are {types_of_people} types of people."

#The following lines creates strings of binary, don't, and another string that
#combines binary and do_not within it using the format string
binary = "binary"
do_not = "don't"
y=f"Those who know {binary} and those who {do_not}."

#The following two lines actually print x and y
print(x)
print(y)

#The following two lines print the above two lines but with added string and
#string format method
print(f"I said: {x}")
print(f"I also said: '{y}'")

#The following line declares hilarious as a boolean variable with value as false
hilarious = False

#The following line creates a string variable with an empty formatted string
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w+e)
