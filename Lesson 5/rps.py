import sys
import random
from enum import Enum

# Constants are always in CAPS
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# Different ways to check Enums:
# print(RPS(2))
# print(RPS.ROCK)
# print(RPS["ROCK"])
# print(RPS.ROCK.value)
# sys.exit()

#  As can be seen below, you use input() to get input from a user.
# Input will always return a string so keep that in mind before doing any calcs or stuff.
# Simple and straight-forward.
# value = input("Please enter a value: \n")
# print("Your value is : " + value)

# Now we start coding the Rock-Paper-Scissors game.
print("")
player_choice = input("Enter...\n1 for Rock 🪨, \n2 for Paper 📄, \nor \n3 for Scissors ✂️:\n\n")

player = int(player_choice)

# Let's introduce some control-flow statements
if player < 1 or player >3:
    sys.exit("Please enter a valid choice!") # This will exit the program but still display the message given in brackets.

computer_choice = random.choice("123")
computer = int(computer_choice)

print("")
print("You chose " + str(RPS(player)).replace("RPS.", "") + ".")
print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".")
print("")

if player == 1 and computer ==3:
    print("🎉 You Win!")
elif player == 2 and computer ==1:
    print("🎉 You Win!")
elif player == 3 and computer ==2:
    print("🎉 You Win!")
elif player == computer:
    print("🪢 Tie Game!")
else:
    print("🐍 Python Wins!")