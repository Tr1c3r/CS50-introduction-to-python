import random

def main():
    # Get the desired level from the user
    level = get_level()
    # Start the problem generation based on the chosen level
    generate_integer(level)

def get_level():
    # Keep prompting the user until a valid level (1, 2, or 3) is entered
    while True:
        try:
            l = input("Get level: ")
            if l not in ["1", "2", "3"]:
                raise ValueError
            return l
        except ValueError:
            pass

def get_random_numbers(ran):
    # Generate random numbers based on the given level
    if ran == "1":
        return random.randint(0, 9), random.randint(0, 9)
    elif ran == "2":
        return random.randint(10, 99), random.randint(10, 99)
    elif ran == "3":
        return random.randint(100, 999), random.randint(100, 999)

def generate_integer(level):
    # Initialize errors counter and score
    errors = 3
    score = 0

    # Generate and display 10 problems
    for i in range(10):
        # Get random numbers based on the chosen level
        a, b = get_random_numbers(level)

        # Keep prompting the user until a correct answer is provided or there are no attempts left
        while True:
            try:
                # Get the user's answer
                answer = int(input(f"{a} + {b} = "))

                # Check if the answer is correct
                if answer == (a + b):
                    score += 1
                    break
                # If the answer is incorrect, decrement the errors counter, display "EEE", and check if errors are exhausted
                elif answer != (a + b):
                    errors -= 1
                    print("EEE")
                if errors <= 0:
                    # If no errors left, display the correct answer
                    print(f"{a} + {b} = {a+b}")
                    break
            except ValueError:
                # Handle non-integer input
                pass

    # Display the final score
    print(f"Score: {score}")

if __name__ == "__main__":
    # Start the main function when the script is executed
    main()
