# This is the normal way to concatenate strings.
person = "Dave"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

# There's definitely a better way to do this.
# Here are some old ways to do it.

# This is the %s method, order matters.
coins = 4
message = "\n%s has %s coins left." % (person, coins)
print(message)

# This is the newer format method, order matters.
coins = 5
message = "\n{} has {} coins left.".format(person, coins)
print(message)

# This is the newer format method, here we change order using indices.
coins = 6
message = "\n{1} has {0} coins left.".format( coins, person)
print(message)

# This is the newer format method and we can assign using names.
coins = 7
message = "\n{person} has {coins} coins left.".format( coins = coins, person = person)
print(message)

# This is the newer format method and we can assign using a dictionary but it is case-sensitive.
player = {'person': 'Dave', 'coins':8}
message = "\n{person} has {coins} coins left.".format(**player)
print(message)

#################################################
# Now we get to use the latest method - F-Strings

message = f"\n{person} has {coins} coins left."
print(message)

# You can also use calculations directly.
message = f"\n{person.lower()} has {2*5} coins left."
print(message)

# You can also use calculations directly.
message = f"\n{player['person']} has {player['coins']} coins left."
print(message)

#################################################
# You can pass formatting options to the method.
# We'll use the colon.

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1,11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1,11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")
