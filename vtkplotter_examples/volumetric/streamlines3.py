"""Draw streamlines for the cavity case from OpenFOAM tutorial"""

from vtkplotter import *

# load file as type vtkUnStructuredGrid
ugrid = loadUnStructuredGrid(datadir+'cavity.vtk')

# make a grid of points to probe as type vtkActor
probe = Grid(pos=(0.05,0.08,0.005), normal=(0,1,0),
             sx=0.01, sy=0.1, resx=4, resy=20, c='k')

# compute stream lines with Runge-Kutta4, return a vtkActor
stream = streamLines(ugrid, probe,
                     activeVectors='U', # name of the active array
                     #tubes={"radius":1e-04, "varyRadius":2},
                     lw=2, # line width
                     )

# make a cloud of points form the ugrid, in order to draw arrows
domain = pointCloudFrom(ugrid)
coords = domain.getPoints()
vects  = domain.getPointArray('U')/200
arrows = Arrows(coords-vects, coords+vects, c='jet_r') # use colormap
box    = domain.box().c('k') # build a box frame of the domain
comment= Text(__doc__)

show(stream, arrows, box, probe, comment, axes=5, bg='white')
