import random

# Prompt the user to enter a level (natural number) until a valid input is provided
while True:
    try:
        # Read the user input as a float
        u = float(input("Level: "))

        # Check if the entered value is a positive integer
        if u.is_integer() and u >= 1:
            break  # Exit the loop if a valid natural number is entered
        else:
            raise ValueError  # Raise an error if the input is not valid
    except ValueError:
        pass  # Ignore ValueError and continue the loop if the input is invalid

# Generate a random number within the specified level range
i = int(random.randrange(1, int(u) + 1))

# Prompt the user to guess the number until they guess it correctly
while True:
    try:
        # Read the user's guess as an integer
        guess = int(input("Guess: "))

        # Compare the guess with the randomly generated number
        if guess < i:
            print("Too small!")
            pass
        elif guess > i:
            print("Too large!")
            pass
        elif guess == i:
            break  # Exit the loop if the guess is correct
    except (ValueError, IndexError):
        pass  # Ignore ValueError and IndexError, continue the loop if input is invalid

# Print a message indicating that the guess is correct
print("Just right!!")
