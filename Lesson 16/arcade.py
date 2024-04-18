import sys
import rps
from guess_number import guess_number

def play_game(name = "playerOne"):
    welcome_back = False
    
    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu! 🤖")
    
        gameChoice = input("\nPlease choose a game: \n1 = Rock Paper Scissors \n2 = Guess My Number \nOr press 'X' to exit the Arcade.\n\n")
        
        if gameChoice.lower() not in ["1", "2", "x"]:
            print(f"\n{name}, Please enter either 1, 2 or x.\n")
            return play_game(name)
        
        welcome_back = True
        
        if gameChoice == "1":
            rock_paper_scissors = rps.rps(name)
            rock_paper_scissors()
        elif gameChoice == "2":
            guess_my_number = guess_number(name)
            guess_my_number()
        else:
            print(f"\nSee you next time!\n")
            sys.exit(f"Bye {name}! 👋\n")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description= "Provides a greeting for the player in the arcade."
    )

    parser.add_argument(
        "-n", "--name", metavar= "Name", required= True,
        help= "Please, Enter your name to play in the Arcade!"
    )

    args = parser.parse_args()
    
    print(f"\n{args.name}, welcome to the Arcade! 🤖")
    
    play_game(args.name)