"""
Probe a voxel dataset at specified points
"""
from vtkplotter import *
import numpy as np

vol = load(datadir+"embryo.slc")

pts = np.random.rand(1000, 3)*256

apts = probePoints(vol, pts).pointSize(3)

#print(apts.getPointArray()) # check the list of point/cell scalars
scals = apts.getPointArray(0)

printHistogram(scals, minbin=1, horizontal=1, c='g')

show(vol, apts, Text(__doc__), axes=8)
