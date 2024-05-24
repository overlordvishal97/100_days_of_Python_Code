import random
from replit import clear
from art import logo

# Constants
# Define the maximum score in Blackjack (21) and the dealer's threshold (17)
BLACKJACK = 21
DEALER_THRESHOLD = 17

def deal_card():
    """Deal a random card from the deck"""
    # Define the deck of cards (11 is the Ace, which can be worth 1 or 11)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # Return a random card from the deck
    return random.choice(cards)

def calculate_score(cards):
    """Calculate the score of a hand of cards"""
    # If the hand has a total score of 21 and only 2 cards, it's a Blackjack (win)
    if sum(cards) == BLACKJACK and len(cards) == 2:
        return 0
    # If the hand has an Ace and the total score is over 21, convert the Ace to 1
    if 11 in cards and sum(cards) > BLACKJACK:
        cards.remove(11)
        cards.append(1)
    # Return the total score of the hand
    return sum(cards)

def compare(user_score, computer_score):
    """Compare the scores of the user and the computer"""
    # If the scores are equal, it's a draw
    if user_score == computer_score:
        return "Draw"
    # If the computer has a Blackjack, the user loses
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    # If the user has a Blackjack, they win
    elif user_score == 0:
        return "Win with a Blackjack"
    # If the user's score is over 21, they lose
    elif user_score > BLACKJACK:
        return "You went over 21. You lose"
    # If the computer's score is over 21, the user wins
    elif computer_score > BLACKJACK:
        return "Opponent went over 21. You win"
    # If the user's score is higher than the computer's, they win
    elif user_score > computer_score:
        return "You win"
    # Otherwise, the user loses
    else:
        return "You lose"

def play_game():
    # Print the game logo
    print(logo)
    # Initialize the user's and computer's hands
    user_cards = []
    computer_cards = []
    # Deal 2 cards to each player
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card)

    # User's turn
    while True:
        # Calculate the user's score
        user_score = calculate_score(user_cards)
        # Calculate the computer's score
        computer_score = calculate_score(computer_cards)
        # Print the user's hand and score
        print(f"Your cards: {user_cards}, current score: {user_score}")
        # Print the computer's upcard
        print(f"Computer's first card: {computer_cards[0]}")
        # If the user has a Blackjack, or the computer has a Blackjack, or the user's score is over 21, end the game
        if user_score == 0 or computer_score == 0 or user_score > BLACKJACK:
            break
        # Ask the user if they want to draw another card
        deal_again = input("Type 'y' to get another card, type 'n' to pass: ")
        # If the user wants to draw, add another card to their hand
        if deal_again == "y":
            user_cards.append(deal_card())
        # If the user wants to pass, end their turn
        else:
            break

    # Computer's turn
    while computer_score < DEALER_THRESHOLD:
        # Add another card to the computer's hand
        computer_cards.append(deal_card())
        # Calculate the computer's score
        computer_score = calculate_score(computer_cards)

    # Print the final hands and scores
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    # Compare the scores and print the result
    print(compare(user_score, computer_score))

# Main game loop
while True:
    # Ask the user if they want to play a game
    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    # If the user wants to play, clear the console and start a new game
    if play_again == "y":
        clear()
        play_game()
   
