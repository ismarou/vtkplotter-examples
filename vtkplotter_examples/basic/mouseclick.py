"""
Mouse click event example
click of the mouse causes a call to a custom function.
"""
from vtkplotter import Plotter, printc, Text, datadir


def onLeftClick(mesh):
    printc("Left   button pressed on", [mesh], c="g")


def onMiddleClick(mesh):
    printc("Middle button pressed on", [mesh], c="y")


def onRightClick(mesh):
    printc("Right  button pressed on", [mesh], c="r")


vp = Plotter(verbose=0)

vp.load(datadir+"skyscraper.obj", c='gold')

vp.mouseLeftClickFunction = onLeftClick
vp.mouseMiddleClickFunction = onMiddleClick
vp.mouseRightClickFunction = onRightClick

printc("Click object to trigger function call", invert=1, box="-")

vp += Text(__doc__)
vp.show()
