# Import necessary libraries and data
import random

from replit import clear

from art import logo, vs
from game_data import data

# Function to get data from a random account
def get_random_account():
  """Get data from random account"""
  return random.choice(data)

# Function to format account data into a printable format
def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

# Function to check if the user's guess is correct
def check_answer(guess, a_followers, b_followers):
  """
  Checks followers against user's guess and returns True if they got it right.
  Or False if they got it wrong.
  """
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

# Function to start and run the game
def game():
  print(logo)
  score = 0
  game_should_continue = True

  # Select two random accounts
  account_a = get_random_account()
  account_b = get_random_account()

  # Ensure account_a and account_b are not the same
  while account_a == account_b:
    account_b = get_random_account()

  # Main game loop
  while game_should_continue:

    # Display the formatted account data
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Get the user's guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get the follower counts for both accounts
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # Check if the user's guess is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen and display the logo again
    clear()
    print(logo)

    # Update the score and provide feedback
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

    # Update account_a and account_b for the next round
    account_a = account_b
    account_b = get_random_account()

    # Ensure account_a and account_b are not the same
    while account_a == account_b:
      account_b = get_random_account()

# Start the game
game()
``` read me for this code
