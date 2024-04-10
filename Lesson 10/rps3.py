import sys
import random
from enum import Enum

def play_rps():
    # Constants are always in CAPS
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    # Now we start coding the Rock-Paper-Scissors game.
    print("")
    player_choice = input("Enter...\n1 for Rock 🪨, \n2 for Paper 📄, \nor \n3 for Scissors ✂️:\n\n")
    
    # Let's introduce some control-flow statements
    if player_choice not in ["1","2","3"]:
        print("You must enter 1, 2 or 3!")
        return play_rps()

    player = int(player_choice)

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
    
    print("\nPlay again? ")
    
    while True:
        playagain = input("\n Y for Yes \n Q to Quit\n\n")
        if playagain.lower() not in ["y","q"]:
            continue
        else:
            break
    
    
    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n🎉 Thank You For Playing!")
        # We can end the loop in two ways
        sys.exit("Buh-Bye!")
        # or
        # break

play_rps()