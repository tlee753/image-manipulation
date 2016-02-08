# function to remove background from image
# saves file as png
# can be modified to remove black or white backgrounds
# created by tlee753
# last modified 2/8/16


import sys
import math
import numpy
from PIL import *
# import cv2
# imports system, numerical, and math methods

def backRem (inputFile):
    image = cv2.imread(inputFile)
    # reads in image file into array
    
    stringLength = len(inputFile)
    # gets the length of the input file string
    
    outputString = inputFile[0:stringLength-5] + "_clear.png"
    # creates output file string to name file and keep original intact
    
    # layer = image(:, :, 1)
    # seperates single layer from image
    
    # [m, n] = size(layer)
    # gets the size of the layer
    
    # alphaArray = [[0 for col in range(n)] for row in range(m)]
    # creates an array of zeros equal in size to the image
    
    for rows in layer:
        for cols in layer:
            if layer[rows, cols] >= 255:
                image[rows, cols] = (0, 0, 0, 0)
    # for loop to go through each pixel and enter '1' in array if white
    
    cv2.imwrite(outputString, image)
    
    print('File Conversion Completed')


backRem('hole.jpeg')
# function call
