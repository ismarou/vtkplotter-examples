"""Example usage of align() method:
generate two random sets of points and
align them using the Iterative Closest Point algorithm.
"""
from __future__ import division
from random import uniform as u
from vtkplotter import *

vp = Plotter(shape=[1, 2], verbose=0, axes=2, bg="w")

N1 = 15  # number of points of first set
N2 = 15  # number of points of second set
x = 1.0  # add some randomness

pts1 = [(u(0, x), u(0, x), u(0, x) + i) for i in range(N1)]
pts2 = [(u(0, x) + 3, u(0, x) + i / 2 + 2, u(0, x) + i + 1) for i in range(N2)]

vpts1 = Points(pts1, r=8, c="b").legend("source")
vpts2 = Points(pts2, r=8, c="r").legend("target")

vp.show(vpts1, vpts2, at=0)

# find best alignment between the 2 sets of Points, e.i. find
# how to move vpts1 to best match vpts2
alpts1 = alignICP(vpts1, vpts2).points()
vp += [Points(alpts1, r=8, c="b"), Text(__doc__, c="k")]

for i in range(N1):  # draw arrows to see where points end up
    vp += Arrow(pts1[i], alpts1[i], c="k", s=0.007, alpha=0.1)

vp.show(at=1, interactive=1)
