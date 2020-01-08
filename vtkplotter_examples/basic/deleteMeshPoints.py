"""Remove points and cells from a mesh
which are closest to a specified point.
"""
from vtkplotter import *

pu = load(datadir+'pumpkin.vtk')
pu.c('lightgreen').bc('tomato').lw(0.1)

pt = [1, 0.5, 1]
ids = pu.closestPoint(pt, N=500, returnIds=True)

pu.deletePoints(ids, renamePoints=1)

show(Point(pt), pu, Text(__doc__), bg='white')
