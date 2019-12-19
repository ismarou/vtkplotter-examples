"""Represent a volume as lego blocks (voxels).
Colors correspond to the volume's scalar.
Try also:
> vtkplotter --lego data/embryo.tif"""
# https://matplotlib.org/users/colormaps.html
from vtkplotter import *

vol = load(datadir+'embryo.tif') # load Volume
printHistogram(vol, logscale=True)

vol.crop(back=0.5) # crop 50% from neg. y

# show lego blocks whose value is between vmin and vmax
lego = vol.legosurface(vmin=60, cmap='seismic')

# make colormap start at 40
lego.addScalarBar(vmin=40, horizontal=1, c='k')

comment = Text(__doc__, c='k')

show(lego, comment, bg='w', axes=1, viewup='z')
