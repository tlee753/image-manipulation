"""
Background Remover
==================
Function to remove backgrounds which fit user input criteria from pictures

- Saves files as .png
- Can be modified to remove black or white backgrounds
- Can also be modified to remove picture and leave white background
- Created by tlee753
- Last Modified 2/10/16
- Version 1.2
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
        # opens image and converts to Red, Green, Blue, Alpha interpretation
        
    except:
        print ("\nUnable to load file. Please check to make sure file exists and is spelled correctly.\n")
        # errors if the input is not an image file    
           
    data = array(image)
    # converts the image into four interconnected arrays of RGBA values ranging from 0 to 255
    
    [red, green, blue, alpha] = data.T
    # splits the four layers of the array into separate single layered arrays

    redValue = raw_input("Minimum value of red for mask. Default: 240 \n")
    greenValue = raw_input("Minimum value of green for mask. Default: 240 \n")
    blueValue = raw_input("Minimum value of blue for mask. Default: 240 \n")
    alphaValue = raw_input("Minimum value of alpha for mask. Default: 240 \n")
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

    
    mask = (red >= redValue) & (green >= greenValue) & (blue >= blueValue) & (alpha >= alphaValue)
    # creates a mask for pixels that fit user defined parameters
    
    data[mask.T] = (0, 0, 0, 0)
    # alters pixels included in the mask to be transparent
    
    image = Image.fromarray(data)
    # converts four interconnected arrays back into image interpretation
    
    outputFile = inputFile[0:len(inputFile)-4] + "_edited.png"
    image.save(outputFile)
    # creates a new file name based on the input and saves the edited image under that name
    
    print ("Conversion Complete")
    # prints confirmation of successful conversion for user

    
backRem()
# function call