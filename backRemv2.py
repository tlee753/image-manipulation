# function to remove background from image
# saves file as png
# can be modified to remove black or white backgrounds
# created by tlee753
# last modified 2/8/16

import math
from numpy import array
from PIL import Image
# imports required components

def backRem (inputFile):
    
    try:
        im = Image.open(inputFile)
        print("Size:")
        print(im.size)
    except:
        print ("Unable to load image")
    # opens file, prints error message if file is corrupt
    
    stringLength = len(inputFile)
    # gets the length of the input file string
    outputString = inputFile[0:stringLength-5] + "_edited.png"
    # creates output file string to name file and keep original intact
    
    [red, green, blue] = im.split()
    # splits image into red, green, and blue images
    # keeps other layers, they are just empty
    
    imageArray = array(im)
    
    for rows in imageArray:
        for cols in imageArray:
            if imageArray[rows, cols].any >= 255:
                imageArray[rows, cols] = (0, 255, 0, 255)
    # iterates through each pixel, sets alpha value to 0 if the pixel is white
    
    im.save(outputString)
    # saves the edited file under the edited name
    
    print ("File editing complete")
    # prints completion message
    
backRem('Hole.jpeg')
# function call



"""
img = Image.fromarray(arr)
img.save("output.png")

http://docs.python-guide.org/en/latest/scenarios/imaging/
- Original pillow installation

https://automatetheboringstuff.com/chapter17
- pillow documentation

http://stackoverflow.com/questions/3752476/python-pil-replace-a-single-rgba-color
- modifying pixels
"""