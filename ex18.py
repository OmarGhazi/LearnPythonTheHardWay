# This one is like scripts with argv
# The * in *args tells Python to take all the arguments to
# the function and then put them in args as a list - similar
# to argv. This isn't very common
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# Ok, that *args is pretty pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# This just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# This one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Omar", "Ghazi")
print_two_again("Omar","Ghazi")
print_one("First!")
print_none()
