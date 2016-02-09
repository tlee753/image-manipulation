from numpy import array
from PIL import Image

def PIL2array(input):
    img = Image.open(input)
    arr = array(img)
    print (arr)
    
PIL2array('Hole.jpeg')