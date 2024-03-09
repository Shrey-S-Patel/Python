# Dictionaries are the topic for today.
# Dictionaries store data in key:value pairs.
# Dictionaries are a lot like JavaScript Objects.

# Creating Dictionaries the normal way.
band = {
    "Vocals": "Plant",
    "Guitar": "Page"
}

# Creating Dictionaries with the constructor method.
band2 = dict(Vocals = "Plant", Guitar = "Page")

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

