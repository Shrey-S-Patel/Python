import sys
import random
from enum import Enum

def rps(name = "PlayerOne"):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins
        
        # Constants are always in CAPS
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        # Now we start coding the Rock-Paper-Scissors game.
        print("")
        player_choice = input(f"{name}, please enter...\n1 for Rock 🪨, \n2 for Paper 📄, \nor \n3 for Scissors ✂️:\n\n")
        
        # Let's introduce some control-flow statements
        if player_choice not in ["1","2","3"]:
            print(f"{name}, please you must enter 1, 2 or 3!")
            return play_rps()

        player = int(player_choice)

        computer_choice = random.choice("123")
        computer = int(computer_choice)

        print(f'\n{name}, you chose {str(RPS(player)).replace("RPS.", "").title()}.')
        print(f'\nPython chose {str(RPS(computer)).replace("RPS.", "").title()}.\n')
        
        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer ==3:
                player_wins += 1
                return f"🎉 {name}, You Win!"
            elif player == 2 and computer ==1:
                player_wins += 1
                return f"🎉 {name}, You Win!"
            elif player == 3 and computer ==2:
                player_wins += 1
                return f"🎉 {name}, You Win!"
            elif player == computer:
                return "🪢 Tie Game!"
            else:
                python_wins += 1
                return f"🐍 Python Wins!\nSorry, {name}... 🥲"
        
        game_result = decide_winner(player, computer)
        print(game_result)
        
        nonlocal game_count
        game_count += 1

        print(f"\nGame Count = {game_count}")
        print(f"\n{name}'s Wins = {player_wins}")
        print(f"\nPython Wins = {python_wins}")
        
        print(f"\nPlay again, {name}? ")
        
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
            if __name__ == "__main__":
                sys.exit(f"\n🎉 Buh-Bye! {name}")
            else:
                return

    return play_rps


if __name__ == "__main__":
    
    import argparse

    parser = argparse.ArgumentParser(
        description= "Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="Name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()
    
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()