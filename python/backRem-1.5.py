"""
Background Remover
==================
Function to remove backgrounds which fit user input criteria from pictures

- Saves files as .png for transparency
- Can be modified to remove black or white backgrounds with a user input tolerance
- Can also be modified to remove picture and leave white background

- Created by tlee753
- Last Modified 10/14/17
- Version 1.5
"""

# import required methods from libraries
from PIL import Image
from numpy import array

def backRem():
    # asks user to input file name    
    inputFile = raw_input("Please type file name string without quotations.\n> ")

    # continue to loop until proper file name is given
    proper = False
    while not proper:
        try:
            # opens image and converts to Red, Green, Blue, Alpha interpretation
            image = Image.open(inputFile)
            image = image.convert('RGBA')
            print("Image successfully loaded.\n")
            proper = True
            
        except IOError as error:
            # errors if the input is not an image file
            print ("Unable to load file. Please check to make sure file exists and is spelled correctly.\n")
            print ("=" * 50)
            print ("Error Arguments: " + str(error.args))
            print ("=" * 50)

    # converts the image into four interconnected arrays of RGBA values ranging from 0 to 255
    data = array(image)

    # splits the four layers of the array into separate single layered arrays
    [red, green, blue, alpha] = data.T

    proper = False
    while not proper:
        try:
            # creates an option for removing pixels above or below the user specified values
            maskInput = raw_input("Would you like to remove RGB pixels with values above mask? Default is yes/above to remove white background.\n> ")

            # adjusts the user input for easier response comparison
            maskInput = maskInput.lower().strip()

            # sets the mask boolean to above or below depending on the user input
            if (maskInput in ["above", "a", "yes", "y", "up", "u", ""]):
                maskBool = True
                print("Removing pixels above user values.\n")
                proper = True
            elif (maskInput in  ["below", "b", "no", "n", "down", "d"]):
                maskBool = False
                print("Removing pixels below user values.\n")
                proper = True
            else:
                raise ValueError("User input is not an available option.")

        except ValueError as error:
            # errors if the user input is not a valid option
            print("\nPlease input \"above\" or \"below\" for mask option.\n")
            print("=" * 50)
            print("Error Arguments: " + str(error.args))
            print("=" * 50 + "\n")

    # continue to loop and request user input until proper values are provided
    proper = False
    while not proper:
        try:
            # asks the user for values to mask the background with
            redValue = raw_input("Value of red for mask. (Default: 240) > ")
            greenValue = raw_input("Value of green for mask. (Default: 240) > ")
            blueValue = raw_input("Value of blue for mask. (Default: 240) > ")
            alphaValue = raw_input("Value of alpha for mask. Always removes values above user input. (Default: 255) > ")

            # default values if none specified
            if redValue == "":
                redValue = 240
            if greenValue == "":
                greenValue = 240
            if blueValue == "":
                blueValue = 240
            if alphaValue == "":
                alphaValue = 255

            # converts user input to type int
            redValue = int(redValue)
            greenValue = int(greenValue)
            blueValue = int(blueValue)
            alphaValue = int(alphaValue)

            # check to see if values are within range 0 - 255
            if (redValue < 0 or redValue > 255 or greenValue < 0 or greenValue > 255 or blueValue < 0 or blueValue > 255 or alphaValue < 0 or alphaValue > 255):
                raise ValueError("User input is not within specified integer value range between 0 and 255.")
            else:
                proper = True

        except ValueError as error:
            # errors if the values are not integers between 0 and 255
            print("\nPlease input integer values between 0 and 255 for mask.\n")
            print("=" * 50)
            print("Error Arguments: " + str(error.args))
            print("=" * 50 + "\n")

        except AttributeError as error:
            print("\nAttriute Error\n")
            print("=" * 50)
            print("Error Arguments: " + str(error.args))
            print("=" * 50 + "\n")

    # creates a mask for pixels that fit user defined parameters
    if maskBool:
        mask = (red >= redValue) & (green >= greenValue) & (blue >= blueValue) & (alpha >= alphaValue)
    else:
        mask = (red <= redValue) & (green <= greenValue) & (blue <= blueValue) & (alpha >= alphaValue)

    # alters pixels included in the mask to be transparent
    data[mask.T] = (0, 0, 0, 0)

    # converts four interconnected arrays back into image interpretation
    image = Image.fromarray(data)

    try:
        # creates a new file name based on the input and saves the edited image under that name
        outputFile = inputFile[0:len(inputFile)-4] + "_edited.png"
        image.save(outputFile)

        # prints confirmation of successful conversion for user
        print("\nConversion complete. File saved as \"" + outputFile + "\".\n")

    except Exception as error:
        # error message if image conversion fails
        print("Conversion failed. Please check inputs and then contact administrator.")
        print("=" * 50)
        print("Error Arguments: " + str(error.args))
        print("=" * 50 + "\n")

# function call
backRem()
