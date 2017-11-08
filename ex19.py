def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print(f"Man that's enough for a party!")
    print("Get a blanket.\n")

# Passing numbers in the function
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Declaring variables, defining them, and passing them
# in the function
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# The following line does math first then passes the result
# to the function as arguments
print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

# The following takes the variales defined above and
# does math first, then passes them as arguments to the
# function
print("And we can combine the two, variables and math")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)


def testfunction(first_arg, second_arg):
    print(f"Addition: {first_arg}+{second_arg} = ", first_arg+second_arg)
    print(f"Subtraction: {first_arg}-{second_arg} = ", first_arg-second_arg)
    print(f"Multiplication: {first_arg}*{second_arg} = ", first_arg*second_arg)
    print(f"Division: {first_arg}/{second_arg} = ", first_arg/second_arg)

print("Now lets do custom math using two numbers")
user_first = int(input("Enter first number: "))
user_second = int(input("Enter second number: "))
testfunction(user_first, user_second)
