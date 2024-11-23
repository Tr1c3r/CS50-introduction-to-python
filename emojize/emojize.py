import emoji  # Import the emoji library

while True:  # Create an infinite loop
    try:  # Try to do the following block of code
        inp = input("Input: ")  # Prompt the user for input and store it in 'inp'
        emoji_text = emoji.emojize(inp, language='alias')  # Convert 'inp' into emojis using the 'emoji' library
        print(f"Output: {emoji_text}")  # Print the result, including the converted emojis
        break  # Exit the loop after successful input and conversion
    except ValueError:  # If a ValueError occurs (e.g., invalid input), continue to the next iteration
        pass
