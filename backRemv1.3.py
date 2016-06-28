"""
Background Remover
==================
Function to remove backgrounds which fit user input criteria from pictures

- Saves files as .png
- Can be modified to remove black or white backgrounds
- Can also be modified to remove picture and leave white background
- Created by tlee753
- Last Modified 6/28/16
- Version 1.3
"""

from PIL import Image
from numpy import array
# import required methods from libraries

def backRem ():
    inputFile = raw_input("Please type file name string without quotations. \n")
    # asks user to input file name

    try:
        image = Image.open(inputFile)
        image = image.convert('RGBA')
        print "Image successfully loaded.\n"
        # opens image and converts to Red, Green, Blue, Alpha interpretation

    except:
        print ("Unable to load file. Please check to make sure file exists and is spelled correctly.\n")
        # errors if the input is not an image file

    data = array(image)
    # converts the image into four interconnected arrays of RGBA values ranging from 0 to 255

    [red, green, blue, alpha] = data.T
    # splits the four layers of the array into separate single layered arrays


    # test section to alter which whether above or below input value pixels are masked

    maskInput = raw_input("Would you like to remove RGB pixels with values above mask? Default is yes/above to remove white background.\n")
    maskInput = maskInput.lower()
    maskInput = maskInput.replace(" ", "")

    if (maskInput == "above" or maskInput == "yes" or maskInput == "" or maskInput == "y" or maskInput == "a" or maskInput == "up"):
        maskBool = True
        print "Removing pixels above user values.\n"
    elif (maskInput == "below" or maskInput == "no" or maskInput == "n" or maskInput == "b" or maskInput == "down"):
        maskBool = False
        print "Removing pixels below user values.\n"
    else:
        print "this is an error to be added later\n"


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
        # checks to see whether user input for mask values are type int

    except:
        print ("\nPlease input integer values between 0 and 255 for mask.\n")
        # errors if the values are not integers between 0 and 255


    if maskBool:
        mask = (red >= redValue) & (green >= greenValue) & (blue >= blueValue) & (alpha >= alphaValue)
    else:
        mask = (red <= redValue) & (green <= greenValue) & (blue <= blueValue) & (alpha >= alphaValue)
    # creates a mask for pixels that fit user defined parameters

    data[mask.T] = (0, 0, 0, 0)
    # alters pixels included in the mask to be transparent

    image = Image.fromarray(data)
    # converts four interconnected arrays back into image interpretation

    outputFile = inputFile[0:len(inputFile)-4] + "_edited.png"
    image.save(outputFile)
    # creates a new file name based on the input and saves the edited image under that name

    print ("\nConversion Complete")
    # prints confirmation of successful conversion for user


backRem()
# function call


# shortcuts to remove white/black backgrounds
# add better default support with mask values in particular

# alpha support (above and below) -> four cases