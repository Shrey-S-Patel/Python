# Closure is a function having access to the scope of the parent function after the parent scope has returned.
# Having a closure is a good way of creating variables rather than polluting the global scope.

def parent_function(person):
    coins = 3
    
    def play_game():
        nonlocal coins
        coins -= 1
        
        if(coins > 1):
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif( coins == 1):
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.\n\nGame Over!")
        
    return play_game

tommy = parent_function("Tommy")
jenny = parent_function("Jenny")

tommy()
tommy()

jenny()