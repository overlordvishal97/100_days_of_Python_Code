# Print the game logo
logo = """

 .oOOOo.                                 oOoOOoOOo o                 o.     O                 o                 
.O     o                                     o     O                 Oo     o                 O                  
o                                            o     o                 O O    O                 O                  
O                                            O     O                 O  o   o                 o                  
O   .oOOo O   o  .oOo. .oOo  .oOo            o     OoOo. .oOo.       O   o  O O   o  `oOOoOO. OoOo. .oOo. `OoOo. 
o.      O o   O  OooO' `Ooo. `Ooo.           O     o   o OooO'       o    O O o   O   O  o  o O   o OooO'  o     
 O.    oO O   o  O         O     O           O     o   O O           o     Oo O   o   o  O  O o   O O      O     
  `OooO'  `OoO'o `OoO' `OoO' `OoO'           o'    O   o `OoO'       O     `o `OoO'o  O  o  o `OoO' `OoO'  o     


"""
print(logo)

# Import the random module for generating random numbers
import random

# Print the game introduction
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Ask the user to choose a difficulty level
user_input = input("Choose a difficulty. Type 'easy' or 'hard': ")

# Define the easy difficulty level function
def easy():
    # Initialize game variables
    game_over = False
    user_turn = 10
    num = random.randrange(1, 101)
    print(f"psst here is the {num}")  # Debugging statement to print the correct answer
    
    # Game loop
    while not game_over:
        # Ask the user to make a guess
        guess = int(input("Make a guess: "))
        user_turn -= 1
        print(f"you have {user_turn} attempts remaining to guess the number.")
        
        # Check if the user has run out of attempts
        if user_turn == 0:
            print("You have run out of guesses, you lose.")
            game_over = True  # Fix the bug: use a single = for assignment
        
        # Check if the user's guess is correct
        elif guess > num:
            print("Too high")
        elif guess < num:
            print("Too low")
        elif guess == num:
            print(f"You got it! The answer was {num}")
            game_over = True

# Define the hard difficulty level function
def hard():
    # Initialize game variables
    game_over = False
    user_turn = 5
    num = random.randrange(1, 101)
    print(f"psst here is the {num}")  # Debugging statement to print the correct answer
    
    # Game loop
    while not game_over:
        # Ask the user to make a guess
        guess = int(input("Make a guess: "))
        user_turn -= 1
        print(f"you have {user_turn} attempts remaining to guess the number.")
        
        # Check if the user has run out of attempts
        if user_turn == 0:
            print("You have run out of guesses, you lose.")
            game_over = True
        
        # Check if the user's guess is correct
        elif guess > num:
            print("Too high")
        elif guess < num:
            print("Too low")
        elif guess == num:
            print(f"You got it! The answer was {num}")
            game_over = True

# Call the appropriate difficulty level function based on user input
if user_input == "easy":
    print("You have 10 attempts remaining to guess the number.")
    easy()
elif user_input == "hard":
    print("You have 5 attempts remaining to guess the number.")
    hard()
