"""
Warp the tip of a mesh using Thin Plate Splines.
Red points stay fixed while a single point in space
moves as the arrow shows.
"""
from vtkplotter import *


mesh = load(datadir+"man.vtk").normalize()

meshdec = mesh.clone().decimate(N=100)  # a heavily decimated copy

sources = [[0.0, 1.0, 0.2]]  # this point moves
targets = [[0.3, 1.3, 0.4]]  # to this.
for pt in meshdec.points():
    if pt[1] < 0.3:  # these pts don't move
        sources.append(pt)  # source = target
        targets.append(pt)

# calculate the warping T on the reduced mesh
T = meshdec.thinPlateSpline(sources, targets).getTransform()
warp = mesh.clone().applyTransform(T).c("blue").alpha(0.4)

apts = Points(sources).c("red")

arro = Arrow(sources[0], targets[0])

show(mesh, arro, warp, apts, Text2D(__doc__), viewup="z", axes=1)
