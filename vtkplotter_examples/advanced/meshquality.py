"""Metrics of quality for
the cells of a triangular mesh.
"""
from vtkplotter import *

mesh = load(datadir+"bunny.obj").scale(1000).computeNormals()

# generate an array for mesh quality
arr = mesh.quality(cmap='RdYlBu')
printHistogram(arr, title='bunny quality', c='g')

# add a scalar bar for the active scalars
mesh.lineWidth(0.1).addScalarBar()

# create numeric labels of active scalar on top of cells
labs = mesh.labels( cells=True, precision=3)

show(mesh, labs, Text(__doc__), bg='bb', zoom=4)
