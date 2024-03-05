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