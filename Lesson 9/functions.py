# Functions are re-usable pieces of code that can be used when you call them.
# We start by defining or creating the function.
# The function definition in itself will do nothing.

# As for naming conventions, we need to keep them all lower-case and separate with _ where needed.
def hello():
    print("Kem Cho?")

# So we need to call it.
hello()


# Next, we can create a function that takes parameters or values.
def sum(num1, num2):
    print(num1+num2)

# When we call this function and pass it values, these now become arguments.
# Fun Fact: The easiest way to differentiate between parameters and arguments is that 
# parameters never change, but arguments keep changing with every function call.
# The argument is the actual data passed in when the function is called.
sum(5,4)