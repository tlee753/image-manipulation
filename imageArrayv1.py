import numpy
from PIL import Image



def PIL2array(input):
    img = Image.open(input)
    array = numpy.array(img.getdata(), numpy.uint8).reshape(img.size[1], img.size[0], 3)
    print (array)
    
PIL2array('Hole.jpeg')