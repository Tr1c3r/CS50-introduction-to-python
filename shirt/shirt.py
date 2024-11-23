# Import necessary modules
import sys
from PIL import Image, ImageOps, ImageFilter

# Define the main function
def main():
    # Check if the number of command-line arguments is less than 3
    if len(sys.argv) < 3:
        sys.exit("Too few arguments.")

    # Check if the number of command-line arguments is more than 3
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments.")

    # Check if both input and output files are valid image files (JPG or PNG)
    if not (is_image(sys.argv[1]) and is_image(sys.argv[2])):
        sys.exit("Not a JPG or PNG file declared.")

    # Check if the file formats of the input and output match
    elif get_extension(sys.argv[1]) != get_extension(sys.argv[2]):
        sys.exit("Formats in input and output must be equal")

    # Assign input and output file names from command-line arguments
    vopen = sys.argv[1]
    vsave = sys.argv[2]

    try:
        # Open the shirt image file
        shirt = Image.open("shirt.png")
        # Get the size of the shirt image
        size = shirt.size

        # Open the input image file
        input_img = Image.open(vopen)
        # Create a copy of the input image
        copy = input_img.copy()
        # Save the copy with the output file name
        copy.save(vsave)

        # Resize the copy to match the size of the shirt using BICUBIC resampling
        resized_input = ImageOps.fit(copy, size=size, method=Image.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
        # Paste the shirt onto the resized input image at the top-left corner
        resized_input.paste(shirt, (0, 0), shirt)

        # Save the final result with the output file name
        resized_input.save(vsave)
    except FileNotFoundError:
        sys.exit("File does not exist.")

# Function to check if a file has a valid image extension (JPG, JPEG, or PNG)
def is_image(example):
    example = example.lower()
    file_extension = example.split('.')[-1]

    # Allowed image file extensions
    switcher = {
        "jpg": True,
        "jpeg": True,
        "png": True,
    }

    return file_extension in switcher

# Function to get the file extension of a given file
def get_extension(file):
    return file.lower().split('.')[-1]

# Execute the main function if the script is run as the main program
if __name__ == "__main__":
    main()
