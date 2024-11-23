# Importing the necessary function from the validator_collection library
from validator_collection import checkers

# The main function where the program execution begins
def main():
    # Prompting the user to input their email address
    input_email = input("What's your email address?: ")

    # Calling the check function to validate the email and storing the result
    valid_notvalid = check(input_email)

    # Printing the result of the email validation
    print(valid_notvalid)

# Function to check if the email is valid or not
def check(email):
    # Using the is_email function from the validator_collection library
    # The walrus operator (:=) is used for both assignment and condition check
    if (is_email_address := checkers.is_email(email)):
        # Returning 'Valid' if the email is valid
        return 'Valid'
    else:
        # Returning 'Invalid' if the email is not valid
        return 'Invalid'

# Ensuring that the main function is executed only if this script is run directly
if __name__ == "__main__":
    main()
