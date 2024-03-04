# This is how you create a new list in Python
users = ["Jack", "Sara", "Jacob"]
data = ["John", 58, True]
empty_data = []
a_list = list([1, "James", True]) # Even though it's kinda pointless but it's there as a method.

# This checks whether an element actually exists in a list and returns a Boolean value.
# print("Jack" in users)

# This uses the index of an element to retrieve it.
# print(users[1])
# print(users[-1])

# This is used to check the index of the given item in an list.
# print(users.index("Sara")) 

# You can also use ranges to return elements in a list.
# print(users[0:2])
# print(users[1:])
# print(users[-3:-1]) # This is the same as from 0:2

# To check the size of the array
# print(len(data))

#To add more items to a list, we need to append like this:
# users.append("Elsa")
# print(users)

# To combine two lists into one we do one the following:
users += ["John", "Cena", "Dwayne"] # When doing this make sure the square brackets are around the list item or it will add every letter of the name to the list as an item.
# print(users)
users.extend(["The Rock","Johnson"])
# print(users)
# The methods above add to the end of the list.

# To add items in specific positions we use:
users.insert(0, "Bob")
# print(users)
# To add multiple items at a specific position without losing the elements that were there, we do this:
users[2:2] = ["Eliud", "Chiran"]
# print(users)
# You can also replace items in a list using a range and the last item in the range will stay the same.
users[1:3] = ["Chan", "Jain"]
# print(users)


# This is how we remove items from a list.
users.remove("Bob")
# print(users)
# We can remove the last item in the list using the pop method.
# print(users.pop())
# print(users)
# We can also just use the del keyword and the user's index to chuck them out of the list.
del users[1]
# print(users)

# This delete keyword also comes in handy to delete an entire list.
# Or just clear it out completely
# del data
data.clear()
# print(data)


# After all this you probably wanna sort the given list and how do you do that?
# Like this...
# NB: These sort functions WILL CHANGE the list. So be CAREFUL!
users[1:2] = ["alan"]
users.sort() # This method usually sorts in Ascending order but the Capital letter words are given priority when sorting.
# print(users)

# Let's give alan the justice he deserves when sorting by introducing an argument that will allow lowercase names to be sorted accordingly.
users.sort(key=str.lower)
# print(users)


# Let's look at number Arrays/Lists and their associated functions.
nums = [5,96,2,75,23,15]
nums.reverse() # This function literally takes the array and flips the positions the elements.
print(nums)

# nums.sort(reverse=True) 
# This function on the other hand will not reverse it but it will sort in descending order.
# print(nums)

# In order to keep the original list and sort it for our purposes we can do the following...
# We're making use of the global sorted function.
print(sorted(nums, reverse=True))
print(nums)

# Or just make a copy of the original (in 3 ways) and sort it or whatever make you happy :)
print("")
print("Copying _ _ _")
# No. 1 -> Use the copy function.
numscopy = nums.copy()
print(numscopy)

# No. 2 -> Use the list constructor.
numscopy1 = list(nums)
print(numscopy1)

# No. 3 -> Use the list range without numbers.
numscopy2 = nums[:]
print(numscopy2)



# -------------Tuples-------------
# Tuples are very much like lists, except the data in them does not change and the order of that data does not change.

# Constructor method
tuple1 = tuple((1, "Sam", False))
print(tuple1)

# Normal Method
tuple2 = (1,5,9,65,2,78,64,23,10,5,5,5,5,5)
print(tuple2)

# As mentioned above, tuples cannot be changed. Therefore, what we can do is copy a tuple and perform the action on it.
# Create a list from the tuple.
tuplecopy = list(tuple1)
tuplecopy.append("Sara")
tuple3 = tuple(tuplecopy)
print(tuple3)

# What we have been doing above is creating a tuple by "Packing" it.
# Now we unpack it into different variables.
(one, *two, three) = tuple2 # The asterisk is to assign the remainder of the items to one variable as a list.
print(one)
print(two)
print(three)

# The tuple has methods available to it
# Like this count method when passed an argument like a number will count how many instanced=s if that number are there in that tuple.
print(tuple2.count(5))