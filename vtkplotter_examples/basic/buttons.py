"""
Add a square button with N possible internal states
 to a rendering window that calls an external function.
 Available fonts: arial, courier, times
"""
print(__doc__)

from vtkplotter import Plotter, printc, datadir


vp = Plotter(shape=(2, 1), axes=4)

mesh = vp.load(datadir+"magnolia.vtk", c="v")

vp.show(mesh, at=0)
vp.show(mesh, at=1)

# add a button to the current renderer (e.i. nr1)
def buttonfunc():
    mesh.alpha(1 - mesh.alpha())  # toggle mesh transparency
    bu.switch()                 # change to next status
    printc(bu.status(), box="_", dim=True)


bu = vp.addButton(
    buttonfunc,
    pos=(0.7, 0.05),  # x,y fraction from bottom left corner
    states=["press to hide", "press to show"],
    c=["w", "w"],
    bc=["dg", "dv"],  # colors of states
    font="courier",
    size=18,
    bold=True,
    italic=False,
)

vp.show(interactive=1)
