# Image-Manipulation
Matlab and Python Scripts for image manipulation

### Functionality
- Background Remover (PYTHON)
  - remove backgrounds from images (either black or white) with some tolerance
  - works by creating a mask for the background and removing those pixels
  - takes in either .jpg or .png, returns a .png for transparency
- Border Maker (MATLAB)
  - adds a border of any size to an image
  - automatically determines .jpg or .png, adds a white background to .jpg and transparent background to .png
  - saves file in the same type it was given

### Future Steps
- update masking for python file
- Rewrite border adder in python
- Convert to separate program
  - potentially in java fx, most likely in python with pythonQT
