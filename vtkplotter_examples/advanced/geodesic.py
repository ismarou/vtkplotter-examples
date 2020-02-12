"""Dijkstra algorithm to compute the graph geodesic.

Takes as input a polygonal mesh and performs
a shortest path calculation 20 times.
"""
from vtkplotter import *

s = Sphere(r=1.07, res=200).clean(0.007).wireframe().alpha(0.02)

paths = []
for i in range(20):
    paths.append(geodesic(s, 2500, i * 700))
    # print(paths[-1].info['CumulativeWeights'])

doc = Text2D(__doc__, c="w")

show(s, Earth(style=4), doc, paths, 
	 bg='midnightblue', viewup="z")
