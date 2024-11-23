import sys
from pyfiglet import Figlet  # Import the Figlet class from the pyfiglet library

# Create a Figlet object
figlet = Figlet()

# Get the list of available fonts from the Figlet object
fonts = figlet.getFonts()

# Get the first command-line argument (required to be "-f" or "--font")
con = sys.argv[1]

# Check if the first argument is not equal to "-f" and not equal to "--font"
if con != "-f" and con != "--font":
    raise ValueError  # Raise a ValueError if the condition is not met

try:
    # Get the second command-line argument (the font name)
    f = sys.argv[2]

    # Check if the specified font is not in the list of available fonts
    if f not in fonts:
        raise ValueError  # Raise a ValueError if the font is not found in the list

    # Set the font of the Figlet object to the specified font
    figlet.setFont(font=f)
except (ValueError, IndexError):
    sys.exit(2)  # Exit the program with a status code of 2 if an error occurs

while True:
    try:
        # Prompt the user for input
        s = input("Input: ")

        # Render the input text using the configured font
        out = figlet.renderText(s)

        # Print the rendered text
        print("Output:\n", out)

        break  # Exit the loop
    except ValueError:
        pass  # Continue to the next iteration of the loop if an error occurs
