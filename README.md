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

### Other TODO's
shortcuts to remove white/black backgrounds -> overload function
- just file name string will remove white background
- file name followed by "white" or "black" string serve as shortcuts for background removal
- add better default support with mask values in particular
- alpha support (above and below) -> four cases
- exception if values aren't int