"""Plot function:
    y(x) = 2 + 2*sin(2*x)/(x+1)

with error band defined as:
    ye = y**2 /5
"""
from vtkplotter import Text, plotxy, show
import numpy as np

x = np.arange(0, 6, 0.1)
y = 2+2*np.sin(2*x)/(x+1)
ye = y**2 / 5

plt1 = plotxy(
    [x, y],         # accepts various input formats
    yerrors=ye,
    yscale=1,       # set the y-scaling factor
    xlimits=(0,6),
    ylimits=(0,5),
    line=True,
    marker='',      # dont show marker
    errorBand=True, # errors on y as an error band
    ec="r",         # error band color
    la=0.6,         # error and line alphas
    lc="k",         # line color
)

show(plt1, Text(__doc__),
     bg="w", axes=1, viewup='2d')
