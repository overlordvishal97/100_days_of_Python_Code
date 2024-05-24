# Import the clear function from the replit module, which is used to clear the console
from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

# Print the logo and a welcome message
print(logo)
print("Welcome to the secret auction program.")

# Initialize an empty dictionary to store the bids
bids = {}

# Define a function to find the highest bidder
def find_highest_bidder(bidding_record):
  # Initialize variables to store the highest bid and the winner
  highest_bid = 0
  winner = ""
  
  # Iterate through the bidding record dictionary
  for bidder in bidding_record:
    # Get the bid amount for the current bidder
    bid_amount = bidding_record[bidder]
    
    # Check if the current bid is higher than the highest bid so far
    if bid_amount > highest_bid:
      # Update the highest bid and the winner
      highest_bid = bid_amount
      winner = bidder
      
  # Print the winner and their bid
  print(f"The winner is {winner} with a bid of ${highest_bid}")

# Initialize a flag to indicate whether the bidding is finished
bidding_finished = False

# Start a loop to continue bidding until the user decides to stop
while not bidding_finished:
  # Ask the user for their name and bid
  Name = input("What is your name? ")
  bib = int(input("What is your bid? $"))
  
  # Add the bid to the bids dictionary
  bids[Name] = bib
  
  # Ask the user if there are any other bidders
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
  
  # If the user decides to stop bidding, set the flag to True and find the highest bidder
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
    
  # If the user decides to continue bidding, clear the console and start again
  elif should_continue == "yes":
    clear()
