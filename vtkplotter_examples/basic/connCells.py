"""
Parse mesh with connectedCells()
"""
from vtkplotter import *

N = 12
sub = 0
tol = 0.02

mesh = load(datadir+'250.vtk')
show(
     mesh.wireframe().c('blue'),
     mesh.boundaries(),
     Point(mesh.points()[30]),
     mesh.connectedCells(30), # cells polygons at vertex nr.30
     )

s = mesh.subdivide(sub).clean(tol)

coords = s.points()
pmesh = Points(s)

tomerge = []
for p in coords:
    ipts = s.closestPoint(p, N=N, returnIds=True)
    pts = coords[ipts]

    d = delaunay2D(pts, mode='fit').c('blue').wireframe()

    piece = d.connectedCells(0, returnIds=False)

    show(pmesh, d, piece, Point(p, c='r'), interactive=0)

    tomerge.append(piece)

show(merge(tomerge).clean(), interactive=1)
