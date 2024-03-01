# String Data Type
# 1. Literal Assignment
import math
first = "Shrey"
last = "Patel"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))


# 2. Can also assign a string to a variable using the string constructor function.
vada = str("pav")
# print(type(vada))
# print(type(vada) == str)
# print(isinstance(vada, str))


# Concatenation
fullname = first + " " + last
# print(fullname)

fullname += "!"
# print(fullname)


# You can also take a different data type and cast it to a string.
decade = str(1980)
# print(type(decade))


# Multiple lines
multiline = """
Kem Cho ?


Majama?

                        Ha ha Tame bolo
                        
Jovo ne, Majama!
"""
# print(multiline)


# Moving on to escaping special characters in Python Strings
# \  = This backslash escapes the next character after it.
# \t = This is used to get a tab.
# \n = This is used to create a new line.
sentence = "I'm back at work!\tHey!\n\nWhere's this at\\located?"
# print(sentence)


# String Methods
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multiline.title())  # This will be used to capitalize every word's first letter
# print(multiline.replace("Majama", "Barobar"))

# When creating a string, all the whitespace characters also account for its length.
# So let's check on how to remove these whitespace characters.
# print(multiline.strip())
# print(len(multiline.strip()))
# print(multiline.lstrip())
# print(len(multiline.lstrip()))
# print(multiline.rstrip())
# print(len(multiline.rstrip()))


# Let's build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee ".ljust(16, ".") + "$4".rjust(4))
print("Croissant ".ljust(16, ".") + "$3".rjust(4))
print("Juice ".ljust(16, ".") + "$1".rjust(4))

print(" ")

# String index values
print(
    first[1]
)  # This does not give you the first letter of my name, instead it gives you the second letter because indexing in python starts at 0.
print(
    first[-1]
)  # This returns the last letter of my name. It is especially useful when you do not know the number of characters in a string.
print(
    first[1:-1]
)  # In this case we can get a range of characters from the string however it does not return the last letter of my name.
print(
    first[1:]
)  # In this case we can get a range of characters from the string up until the last character of my name.
print(" ")

# Some methods will return Boolean data, let's check it out.
print(
    first.startswith("S")
)  # This method is case-sensitive so be careful of what you type in those brackets.
print(first.endswith("y"))

print(" ")


# Lets look at boolean data types
myvalue = True
x = bool(False)  # This is the constructor method to create a Boolean variable.

print(type(x))
print(isinstance(x, bool))
print(" ")

# Let's move on to numeric data types
# Integer
price = 100
best_price = int(80)

print(type(price))
print(isinstance(best_price, int))

# Float Type - Has a Decimal
gpa = 3.89
y = float(1.62)
print(type(gpa))

# Complex Type
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers
print(abs(gpa))
print(round(gpa))
print(round(gpa, 1))

print(math.pi)
print(math.sqrt(81))
print(math.ceil(gpa))
print(math.floor(gpa))

# We can also cast a string to a number
zipcode = "15228"
zip_value = int(zipcode)
print(type(zip_value))

# This can throw an error if you try to cast an incorrect value to int.
zip_value = int("Nairobi")
