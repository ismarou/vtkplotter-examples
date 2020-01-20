"""Draw the PCA (Principal Component Analysis) ellipsoid that contains
50% of a cloud of Points, then check if points are inside the surface.
Extra info is stored in mesh.info['sphericity'], 'va', 'vb', 'vc'.
"""
from vtkplotter import Plotter, pcaEllipsoid, Points, Text
import numpy as np


vp = Plotter(axes=1, bg='w')

pts = np.random.randn(500, 3)*[3,2,1]  # random gaussian point cloud

elli = pcaEllipsoid(pts, pvalue=0.5, pcaAxes=1)

ipts = elli.getMesh(0).insidePoints(pts)  # elli is a vtkAssembly
opts = elli.getMesh(0).insidePoints(pts, invert=True)

vp += Points(ipts, c="g")
vp += Points(opts, c="r")
vp += [elli, Text(__doc__)]

print("inside  points #", len(ipts))
print("outside points #", len(opts))
print("sphericity :", elli.info["sphericity"])
print("axis 1 size:", elli.info["va"])
print("axis 2 size:", elli.info["vb"])
print("axis 3 size:", elli.info["vc"])
vp.show()
