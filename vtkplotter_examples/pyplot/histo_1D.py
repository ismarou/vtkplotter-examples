from vtkplotter import histogram, show
import numpy as np

h1 = histogram(np.random.randn(500)*3+10,
               xtitle='random variable x',
               ytitle='dN/dx',
               yscale=0.2,
               xlim=(-2,20),
               ylim=(0,25),
               fill=True,
               outline=False,
               errors=True,
               axes=True,
               )

h2 = histogram(np.random.randn(500)*2+ 7,
               yscale=0.2, # same yscale!
               xlim=(-2,20),
               ylim=(0,25),
               fill=False,
               lc='firebrick',
               lw=4,
               axes=False,
               )
h2.z(0.1) # put h2 in front of h1 by setting its z-coord

# pick the 16th bin and color it tomato
h1.unpack(15).color('tomato').alpha(0.7)

# show locking scene to the 2d xy plane
show(h1, h2, viewup='2d')
