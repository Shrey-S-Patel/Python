# Functions are re-usable pieces of code that can be used when you call them.
# We start by defining or creating the function.
# The function definition in itself will do nothing.

# As for naming conventions, we need to keep them all lower-case and separate with _ where needed.
def hello():
    print("Kem Cho?")

# So we need to call it.
# hello()


# Next, we can create a function that takes parameters or values.
# I have assigned a default values to the nums incase a value is not provided.
def sum(num1 = 0, num2 = 0):
    if (type(num1) is not int or type(num2) is not int):
        return # This is what we call an early return and it prevents the coming lines from executing. It just returns none.
        # return 0 to make it return a zero.
    return num1+num2

# When we call this function and pass it values, these now become arguments.
# Fun Fact: The easiest way to differentiate between parameters and arguments is that 
# parameters never change, but arguments keep changing with every function call.
# The argument is the actual data passed in when the function is called.
total = sum()
print(total)


# Sometimes we can have a function where we don't know the number of arguments that will be passed.
# So we use the args keyword with an asterisk.
def multiple_items(*args):
    print(args)
    print(type(args))

# When the single asterisk is used it returns a tuple.
multiple_items("Donna", 2, True)

# If you want to assign names to the arguments then you can use keyword arguments
def multi_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

multi_named_items(First = "Donna", Last = "Anderson")
# The result from this is a dictionary and i think it will be much more useful than a tuple