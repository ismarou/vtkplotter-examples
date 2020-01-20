"""A simple scatter plot with plotxy()"""
from vtkplotter import plotxy, show, Text
from numpy.random import randn

x = randn(100)
y = randn(100)*20

plt = plotxy(
    [x, y],       # accepts different formats
    xtitle="variable x",
    ytitle="variable y",
    line=False,
    yscale=None,  # automatic y scale
    marker=".",   # marker style
    mc="dr",      # marker color
)

# show Assembly object and lock interaction to 2d:
# (can zoom in a region w/ mouse, press r to reset)
show(plt, Text(__doc__), bg="w", axes=1, viewup='2d')
