# Recursion is when a function calls itself.
def add_one(num):
    
    if (num >= 9 ):
        return num + 1
    
    total = num + 1
    print(total)
    
    return add_one(total) # This return keyword is absolutely essential for recursion or else it returns a none.

# To see the output of 10 we first need a variable we can print.
output = add_one(0)
print("Your output is " + str(output))

