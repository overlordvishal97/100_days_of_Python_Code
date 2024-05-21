# Import required modules
from replit import clear

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


# Define arithmetic operations as functions
def add(n1, n2):
  """Add two numbers"""
  return n1 + n2

def sub(n1, n2):
  """Subtract two numbers"""
  return n1 - n2

def multi(n1, n2):
  """Multiply two numbers"""
  return n1 * n2

def div(n1, n2):
  """Divide two numbers"""
  if n2 == 0:
    raise ValueError("Cannot divide by zero!")
  return n1 / n2

# Create a dictionary to map operation symbols to functions
operations = {"+": add, "-": sub, "*": multi, "/": div}

def calculator():
  """
  Main calculator function
  """
  print(logo)
  num1 = float(input("What's the first number?: "))

  # Display available operations
  print("Available operations:")
  for symbol in operations:
    print(symbol)

  should_continue = True

  while should_continue:
    # Get user input for operation and second number
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number?: "))

    # Perform calculation
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    # Ask user if they want to continue
    response = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
    if response == "y":
      num1 = answer
    else:
      should_continue = False
      clear()

# Call the calculator function
calculator()
