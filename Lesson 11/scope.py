# This variable has Global scope so it is accessible from everywhere in the function.
name = "Dave"
count = 1

# Now we create a function that has local scope and this global variable will still be available there
def greeting(name):
    color = "Blue"
    # Local scope.
    # In this case color can only be accessed from within the function.
    # Trying to access this color variable outside will give you some problems.
    # However, the global variable is still accessible from inside here.
    print(color)
    print(name)
    # The name that is passed here is local and not the global variable name we see up there.

greeting("John\n\n")

# The scope also applies to functions and not only variables
def another():
    # In this case the color variable is in the parent scope (that is another).
    color = "Blue"
    
    # And this function is only available inside the another function and not the global scope.
    def greeting(name):
        print(color)
        print(name)
    greeting("Dave")

another()

# Like shown above you could have a nested function strictly because you only need that function within that function.
# Hence no need for a global declaration which could lead to the pollution of the global scope.

def another1():
    color = "Blue"
    
    # When I create a count here, that is treated like a new variable and not a reassignment.
    # count = 5
    # print(count)
    
    # You can access the global count but not modify it, it throws an error.
    # count += 1
    # print(count)
    
    # To use the global value from above we use the global keyword.
    global count
    count += 5
    print(count)
    
    def greeting(name):
        # Now to use the value from a parent scope we will use the nonlocal keyword.
        nonlocal color
        color = "red"
        print(color)
        print(name)
        
    greeting("Dave")

another1()