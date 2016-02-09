# function to remove background from image
# saves file as png
# can be modified to remove black or white backgrounds
# created by tlee753
# last modified 2/8/16

import math
import numpy
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
    
    array = np.asarray(red, dtype=np.uint8)
    print (array.shape)
    
    for rows in array:
        for cols in array:
            if layer[rows, cols] >= 255:
                im[rows, cols] = (0, 255, 0, 255)
    # iterates through each pixel, sets alpha value to 0 if the pixel is white
    
    im.save(outputString)
    # saves the edited file under the edited name
    
    print ("File editing complete")
    # prints completion message
    
backRem('Hole.jpeg')
# function call

