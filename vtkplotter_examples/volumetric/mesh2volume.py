"""Convert a mesh it into volume (left in grey) where the
foreground voxels are 1 and the background voxels are 0.

Right: the Volume is isosurfaced.
"""
from vtkplotter import *

doc = Text2D(__doc__, c="k")

s = load(datadir+"bunny.obj").normalize().wireframe()

v = mesh2Volume(s, spacing=(0.02, 0.02, 0.02)).alpha([0,0.5]).c('blue')

iso = v.isosurface().color("b")

show(v, s.scale(1.05), doc, at=0, N=2)

show(iso, at=1, interactive=1)
