"""Fit a plane to regions of a surface defined by
N points that are closest to a given point of the surface.
For some of these point we show the fitting plane.
Black points are the N points used for fitting.
Green histogram is the distribution of residuals from the fitting.
"""
from vtkplotter import *

vp = Plotter(verbose=0, axes=0, bg='w')

s = vp.load(datadir+"cow.vtk").alpha(0.3).subdivide()  # remesh

variances = []
for i, p in enumerate(s.points()):
    if i % 100:
        continue  # skip most points
    pts = s.closestPoint(p, N=12)  # find the N closest points to p
    plane = fitPlane(pts)  # find the fitting plane
    vp += plane
    vp += Points(pts)  # blue points
    vp += Point(p, r=5, c="red")  # mark in red the current point
    cn, v = plane.info["center"], plane.info["normal"]
    vp += Arrow(cn, cn + v / 15.0, c="g")
    variances.append(plane.info["variance"])

vp += histogram(variances, c="g").scale([30,.03,30]).pos(-0.5, -1.2, -.6)

vp += Text(__doc__, pos=1)
vp.show(viewup="z")
