value = True
count = 0

# This statement assumes that while value is true or exists, it will execute.
while value:
    count += 1
    print(count)
    if(count == 5):
        break
    else:
        value = False # Or use a zero to do the same thing.
        continue