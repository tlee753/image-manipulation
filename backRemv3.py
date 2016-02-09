from numpy import array
from PIL import Image
# imports required components

def backRem (inputFile):
    try:
        image = Image.open(inputFile)
    except:
        print ("Unable to load image")
        
    outputString = inputFile[0:len(inputFile)-5] + "edited.png"
    # formats output file name
    
    imageConverted = image.convert('RGBA')
    imageArray = array(imageConverted)
    # creates a height x width x 4 numpy array
    
    # [red, green, blue, alpha] = imageArray.T
    # temporarily unpack the bands for readability
    
    for rows in imageArray:
        for cols in imageArray:
            if imageArray[rows, cols].any >= 240:
                imageArray[rows, cols] = (0, 0, 0, 0)
    print ('so far so good 3')          
    newImage = Image.fromarray(imageArray)
    newImage.show()
    
backRem('Hole.jpeg')
    
    
    
    
"""
import Image
import numpy as np

im = Image.open('test.png')
im = im.convert('RGBA')

data = np.array(im)   # "data" is a height x width x 4 numpy array
red, green, blue, alpha = data.T # Temporarily unpack the bands for readability

# Replace white with red... (leaves alpha values alone...)
white_areas = (red == 255) & (blue == 255) & (green == 255)
data[..., :-1][white_areas.T] = (255, 0, 0) # Transpose back needed

im2 = Image.fromarray(data)
im2.show()
"""