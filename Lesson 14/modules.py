# This is an in-built module and Python ships with it
# It is really handy and has all the necessary functions and constant values needed to perform maths.

from math import pi
import sys
# Now this is an alias for the random module.
import random as rdm
from enum import Enum
from rps7 import rock_paper_scissors

# Importing my module on Kenya
import kenya

# print(pi)
# rdm.choice("123")

# for item in dir(rdm):
#     print(item)


# Using my imported Kenya module.
print(kenya.capital)
kenya.randomfunfact()

# Printing the name of the module.
# In this case it prints the name of the module that is currently running.
print(__name__)

# In this case it prints the name of the module you want it to.
print(kenya.__name__)

rock_paper_scissors()