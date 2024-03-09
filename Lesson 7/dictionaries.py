# Dictionaries are the topic for today.
# Dictionaries store data in key:value pairs.
# Dictionaries are a lot like JavaScript Objects.

# Creating Dictionaries the normal way.
band = {
    "Vocals": "Plant",
    "Guitar": "Page"
}

# Creating Dictionaries with the constructor method.
band2 = dict(Vocals="Plant", Guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band2))

# Accessing items in a dictionary.
print(band["Vocals"])
print(band.get("Guitar"))

# To list all the keys we will.
print(band.keys())

# To list all the values we will.
print(band.values())

# List of key value pairs as tuples.
print(band.items())

# We can also check if a key exists in the dictionary.
print("Guitar" in band)
print("Triangle" in band)

# Changing values in a dictionary.
band["Vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)

# After adding now we remove.
# Using the pop method will usually return a value that we removed from the dictionary.
print(band.pop("bass"))
print(band)

band["Drums"] = "Bonham"
print(band)

# With this we will get the last item in the dictionary but it will return a key:value pair tuple and not a value.
print(band.popitem())
print(band)

# To delete and clear.
band["Drums"] = "Bonham"
del band["Drums"]
print(band)

# To completely clear a dictionary we use the clear method.
band2.clear()
print(band2)

# We can also delete the entire dictionary.
del band2
# print(band2)

# Next, Let's copy some dictionaries.
# band2 = band
# Now you might think this is a new band dictionary but it is just a reference instead.
# print("This is a bad copy!")
# print(band2)
# print(band)

# band2["Drums"] = "Bonham"
# print(band2)
# print(band)

# Let's look at the correct way to copy dictionaries.
band2 = band.copy()
print("\nThe Right Way!")
band2["Drums"] = "Bonham"
print(band2)
print(band)

# If you like complicating your life use the constructor function, still works.
band3 = dict(band)
print("\nStill The Right Way!")
band3["Drums"] = "Koko"
print(band3)
print(band)


# Another interesting concept to look at is the Nested Dictionaries.
# Basically, the value for a key will be another dictionary in this case.
member1 = {
    "name": "Plant",
    "instrument": "Vocals"
}
member2 = {
    "name": "Page",
    "instrument": "Guitar"
}

band4 = {
    "member1": member1,
    "member2": member2
}

print("\nLet's look at nested dictionaries. \nVoila!")
print(band4)

# How can you access values in a nested dictionary?
print(band4["member1"]["name"])


# Python Sets
nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums2))
print(len(nums2))

# The advantage of a set is that no duplicates are allowed.
nums = {1, 3, 2, 3, 4, 2}
print(nums)  # Will not throw an error, just ignores the duplicates.

# The True value is a dupe of 1 and the False value is a dupe of 0.
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# You can also check if a value is in a set.
print(4 in nums)

# The funny thing about a set is you cannot reference an item in the set using an index (like in lists) or using a key (like in dictionaries).

# Adding values to a set
nums.add(9)
print(nums)

# Adding elements from another set to our set.
morenums = {5, 6, 7, 8}
nums.update(morenums)
print(nums)

# Fun Fact: You can also use the update method with lists, Tuples and Dictionaries.

# Merge two sets to create a new set.
one = {1, 2, 3}
two = {4, 5, 6}

thenewset = one.union(two)
print(thenewset)

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4, 5, 6}

one.intersection_update(two) # This one modifies the first set - one.
the_new_set = one.intersection(two) # This returns the similarities between the set and assigns it to a new set.
print(one)
print(the_new_set)

# Keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4, 5, 6}

one.symmetric_difference_update(two)
print(one)