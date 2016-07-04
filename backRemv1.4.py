"""
Background Remover
==================
Function to remove backgrounds which fit user input criteria from pictures

- Saves files as .png for transparency
- Can be modified to remove black or white backgrounds
- Can also be modified to remove picture and leave white background
- Created by tlee753
- Last Modified 6/29/16
- Version 1.4
"""

from PIL import Image
from numpy import array
# import required methods from libraries

def backRem():
    inputFile = raw_input("Please type file name string without quotations. \n")
    # asks user to input file name

    try:
        image = Image.open(inputFile)
        image = image.convert('RGBA')
        print "Image successfully loaded.\n"
        # opens image and converts to Red, Green, Blue, Alpha interpretation

    except IOError as error:
        print ("Unable to load file. Please check to make sure file exists and is spelled correctly.\n")
        print ("=" * 50)
        print ("Error Arguments: " + str(error.args))
        print ("=" * 50)
        # errors if the input is not an image file

    data = array(image)
    # converts the image into four interconnected arrays of RGBA values ranging from 0 to 255

    [red, green, blue, alpha] = data.T
    # splits the four layers of the array into separate single layered arrays

    maskInput = raw_input("Would you like to remove RGB pixels with values above mask? Default is yes/above to remove white background.\n")
    # creates an option for removing pixels above or below the user specified values

    maskInput = maskInput.lower()
    maskInput = maskInput.replace(" ", "")
    # adjusts the user input for easier response comparison

    if (maskInput == "above" or maskInput == "yes" or maskInput == "" or maskInput == "y" or maskInput == "a" or maskInput == "up"):
        maskBool = True
        print "Removing pixels above user values.\n"
    elif (maskInput == "below" or maskInput == "no" or maskInput == "n" or maskInput == "b" or maskInput == "down"):
        maskBool = False
        print "Removing pixels below user values.\n"
    else:
        raise ValueError('\nUser input is not an available option.\n')
    # sets the mask boolean to above or below depending on the user input

    redValue = raw_input("Value of red for mask. Default: 240 \n")
    greenValue = raw_input("Value of green for mask. Default: 240 \n")
    blueValue = raw_input("Value of blue for mask. Default: 240 \n")
    alphaValue = raw_input("Value of alpha for mask. Always removes values above user input. Default: 255 \n")
    # asks the user for values to mask the background with

    try:
        redValue = int(redValue)
        greenValue = int(greenValue)
        blueValue = int(blueValue)
        alphaValue = int(alphaValue)
        # converts user input to type int

        if (redValue < 0 or redValue > 255 or greenValue < 0 or greenValue > 255 or blueValue < 0 or blueValue > 255 or alphaValue < 0 or alphaValue > 255):
            raise ValueError('\nUser input is not within specified integer value range between 0 and 255.\n')
        # check to see if values are within range 0 - 255

    except ValueError as error:
        print ("\nPlease input integer values between 0 and 255 for mask.\n")
        print ("=" * 50)
        print ("Error Arguments: " + str(error.args))
        print ("=" * 50)
        # errors if the values are not integers between 0 and 255

    except AttributeError as error:
        print ("\nPlease input integer values between \n")
        print ("=" * 50)
        print ("Error Arguments: " + str(error.args))
        print ("=" * 50)

    if maskBool:
        mask = (red >= redValue) & (green >= greenValue) & (blue >= blueValue) & (alpha >= alphaValue)
    else:
        mask = (red <= redValue) & (green <= greenValue) & (blue <= blueValue) & (alpha >= alphaValue)
    # creates a mask for pixels that fit user defined parameters

    data[mask.T] = (0, 0, 0, 0)
    # alters pixels included in the mask to be transparent

    image = Image.fromarray(data)
    # converts four interconnected arrays back into image interpretation

    try:
        outputFile = inputFile[0:len(inputFile)-4] + "_edited.png"
        image.save(outputFile)
        # creates a new file name based on the input and saves the edited image under that name

        print ("\nConversion complete.\n")
        # prints confirmation of successful conversion for user

    except Exception as error:
        print ("Conversion failed. Please check inputs and then contact administrator.")
        print ("=" * 50)
        print ("Error Arguments: " + str(error.args))
        print ("=" * 50)
        # error message if image conversion fails


backRem()
# function call


# shortcuts to remove white/black backgrounds -> overload function
# - just file name string will remove white background
# - file name followed by "white" or "black" string serve as shortcuts for background removal

# add better default support with mask values in particular

# alpha support (above and below) -> four cases

# exception if values aren't int