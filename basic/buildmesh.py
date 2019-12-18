"""
Manually build a mesh.
"""
from vtkplotter import *

verts = [(50,50,50), (70,40,50), (50,40,80), (80,70,50)]
faces = [(0,1,2), (2,1,3), (1,0,3)]
# (the first triangle face is formed by vertex 0, 1 and 2)

a = Actor([verts, faces])
a.backColor('violet').lineColor('black').lineWidth(1)

# the way vertices are assembled into polygons can be retrieved
# in two different formats:
printc('getPolygons() format is    :', a.getPolygons(), c=3)
printc('getConnectivity() format is:', a.getConnectivity(), c=3)

show(a, Text(__doc__), viewup='z', axes=8)
