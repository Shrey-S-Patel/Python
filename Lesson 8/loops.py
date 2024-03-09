# Let's start by looking at a while loop.
value = 1
# while value <= 10:
#     print(value)
#     # To get out of the loop using another condition we can.
#     if value == 5:
#         break
#     value+=1
    
"""
while value <= 10:
    value+=1
    # We can skip to the next cycle of the loop using the continue keyword.
    if value == 5:
        continue
    # Since we skip after the value is five, the print statement is not carried out.
    print(value)
# The else statement is carried out when we complete the loop but, it is ignored if we use the break keyword.
else:
    print("The values is now " + str(value))"""


# Moving on, let's check out FOR Loops.
# The for loop iterates over a sequence. The sequence can be the contents of a collection like lists, sets, tuples, dictionaries or even the characters of a string.

# for name in names:
#     print(name)

# # Iterating over the characters of a string 
# for letter in "Mississippi":
#     print(letter)

# for x in names:
#     if x == "Sara":
#         break
#     print(x)

# In this case, like before, Sara will be skipped and the next cycle of the loop will begin
# for x in names:
#     if x == "Sara":
#         continue
#     print(x)

# We can also have the FOR Loop iterate through a range.
# for i in range(4):
#     print(i)

# for i in range(2,4): #This starts at 2 and ends at 4.
#     print(i)

# for i in range(0,101,5): #This starts at 0, ends at 100(100 is not included unless increment it to 101) and increments in 5 steps.
#     print(i)
# else:
#     print("Glad that\'s over")


# Now we look at nested loops people!
# Fancy wording for a loop-within-a-loop.
names = ["Dave", "Jocelyn", "Sara", "Maki", "Jaya", "Anita", "Celia"]
actions = ["Works", "Eats", "Sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")
#     print("")

for action in actions:
    for name in names:
        print(name + " " + action + ".")
    print("")