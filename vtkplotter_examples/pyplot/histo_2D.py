"""Histogram of 2 variables"""
from vtkplotter import *
import numpy as np

n = 10000
x = np.random.normal(2, 1, n)*1.2
y = np.random.normal(1, 1, n)

h = histogram(x, y, bins=(25,25), cmap='cividis')

show(h, axes=1, viewup='2d')
