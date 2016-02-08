from PIL import Image

def imageTestv1 (inputFile):
    image = Image.open(inputFile)
    image.show()
    
imageTestv1('Hole.jpeg')