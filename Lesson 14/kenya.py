# This is a module that contains fun facts on my lovely country.

from random import choice

capital = "Nairobi"
bird = "Lilac-breasted Roller"
language = "Swahili"
flower = "Orchid"
song = "Ee Mungu Nguvu Yetu"

def randomfunfact():
    random_fun_fact = ["62 languages are spoken across Kenya", "Kenya is home to Africa’s second-highest mountain",
    "The first African woman to win the Nobel Peace Prize is from Kenya.", "Kenya is home to world record breakers."]
    
    index = choice("0123")
    
    print(random_fun_fact[int(index)])

# Using this control statement prevents this function from being run unless it is explicitly called.
if __name__ == "__main__":
    randomfunfact()