# A lambda function is a single expression that returns a value.
# These functions cannot be called as they have no name - also called anonymous functions.
# But they will definitely return a value. We can assign this function to a variable.

square = lambda num : num * num
print(square(2))

addTwo = lambda num : num + 2
print(addTwo(5))

sum_total = lambda a, b: a + b
print(sum_total(2,6))

#################################################
# These are most often used within another function as a quick and easy function.
# Instead of writing a whole new function, it is a quick and easy function.
def func_builder(x):
    return lambda num : num + x

addTen = func_builder(10)
addTwenty = func_builder(20)

print(addTen(7))
print(addTwenty(7))

#################################################
# A higher order function is a function that takes one or more functions as arguments 
# or a function that returns a function as its result.
numbers = [3,7,10,12,15,18,20]

# Map is a function that first receives a function as its first argument and a data collection as the second.
# It applies the function to every item in the collection and returns it.
squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

#################################################
# Filter only returns the values that are true.
odd_nums = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_nums))

#################################################
from functools import reduce

numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

print(sum(numbers, 10))


names = ['Dave grey', 'Sarah Jones', 'Nick Jonas', 'Alliah Mendez']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
print(char_count)