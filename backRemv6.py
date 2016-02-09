from PIL import Image
from numpy import array

def backRem (inputFile):
    image = Image.open(inputFile)
    image = image.convert('RGBA')
    
    data = array(image)
    
    [red, green, blue, alpha] = data.T
    
    whiteMask = (red >= 240) & (green >= 240) & (blue >= 240) & (alpha >= 240)
    data[whiteMask.T] = (0, 0, 0, 0)
    
    image = Image.fromarray(data)
    
    outputFile = inputFile[0:len(inputFile)-5] + "_edited.png"
    image.save(outputFile)
    
    print ("Conversion Complete")
    
backRem('Hole.jpeg')