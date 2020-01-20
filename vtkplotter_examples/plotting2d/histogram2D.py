"""Histogram 2D"""
from vtkplotter import *
import numpy as np

n = 10000
x = np.random.normal(2, 1, n)*1.2
y = np.random.normal(1, 1, n)

h = histogram2D(x, y, bins=(25,25), cmap='cividis')

show(h, axes=8, bg='w', viewup='2d')
