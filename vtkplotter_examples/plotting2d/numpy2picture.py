"""Load a picture with matplotlib imread()
and make it a 3D object.
"""
from matplotlib.image import imread
from vtkplotter import Picture, Text, datadir, show

fname = datadir+'images/tropical.jpg'
arr = imread(fname)

pic = Picture(arr) # create Picture object from numpy array

# (press r to reset):
show(pic, Text(__doc__), axes=8, viewup='2d')
