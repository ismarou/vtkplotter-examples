from vtkplotter import plot, show
import numpy as np

x = np.arange(0, 10, 1)
y = 3 * np.sin(x)

# assign errors to both x and y
ye = np.random.rand(10)
xe = np.random.rand(10)

##############
plt1 = plot(x, y,
            xtitle="x variable (mm)",
            ytitle="y(x)",
            xlim=(-1, 11),
            ylim=(-3, 4),
            line=True,    # join points with a line
            lc="r",       # line color
            marker="*",   # marker style
            mc="r",       # marker color
            ms=.2,
)

##############
plt2 = plot(x+1, y+0.2,
            xerrors=xe,   # show error bars
            yerrors=ye,
            xlim=(-1, 11),
            ylim=(-3, 4),
            splined=True,
            lc="b",
            marker="s",   # o,p,*,h,D,d,v,^,s,x,a
            ms=.1,
            axes=0
)

##############
show(plt1, plt2, axes=0)
