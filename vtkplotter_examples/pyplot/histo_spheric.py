"""Uniform distribution on a plane
is not uniform on a sphere"""
import numpy as np
from vtkplotter import *

phi = np.random.rand(1000)*6.28
the = np.random.rand(1000)*3.14

h0 = histogram(the, phi, cmap='rainbow')
h1 = histogram(the, phi, mode='spheric')

show(h0, h1, N=2, sharecam=False)
