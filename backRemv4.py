"""
#!/usr/bin/python
from PIL import Image
from numpy import array
# import sys

def backRem (inputFile):
    img = Image.open(inputFile)
    img = img.convert("RGBA")

    pixdata = img.load()

    # Clean the background noise, if color != white, then set to black.

    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y] == (255, 255, 255, 255):
                pixdata[x, y] = (0, 0, 0, 0)
                
    newImage = Image.fromarray(pixdata)
    newImage.show()
    
backRem('Hole.jpeg')
"""
#!/usr/bin/python
from PIL import Image
import sys

img = Image.open('Hole.jpeg')
img = img.convert("RGBA")

pixdata = img.load()

# Clean the background noise, if color != white, then set to black.

for y in xrange(img.size[1]):
    for x in xrange(img.size[0]):
        if pixdata[x, y] == (255, 255, 255, 255):
            pixdata[x, y] = (0, 0, 0, 255)