"""Create individual axes to 
each separate object in a scene"""
from vtkplotter import *

# Create a bunch of objects
s1 = Sphere(pos=(10,0,0), r=1, c='r')
s2 = Sphere(pos=(0,10,0), r=2, c='g')
s3 = Sphere(pos=(0,0,10), r=3, c='b')
pt = Point([-4,-4,-4], c='k')

# Build individual axes for each object. 
#  A new Assembly object is returned:
axes1 = s1.buildAxes(c='r')
axes2 = s2.buildAxes(c='g')
axes3 = s3.buildAxes(c='b', numberOfDivisions=10)

# By specifiyng axes in show() a new axes are 
#  created which span the whole bounding box.
#  Options are passed through a dictionary
show(pt, s1,axes1, s2,axes2, s3,axes3, Text(__doc__),
     bg='white',
     viewup='z',
     axes={'c':'black',
           'numberOfDivisions':10,
           'yzGrid':False,
           },
     )
