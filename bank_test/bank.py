def main():
    # Prompt the user for input and store it in the variable 'greeting'
    greeting = input("Greeting: ")

    # Call the 'value' function with the user's input and print the result
    print(value(greeting))

def value(gr):
    # Convert the input to lowercase for case-insensitive comparisons
    modified_gr = gr.lower()

    # Check if the modified greeting starts with "h"
    if modified_gr.startswith("h"):
        # Check if the modified greeting starts with "hello"
        if modified_gr.startswith("hello"):
            # If yes, return 0
            return 0
        # If not "hello," return 20
        return 20
    else:
        # If the modified greeting doesn't start with "h," return 100
        return 100

# Check if this script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Call the 'main' function to start the program
    main()
