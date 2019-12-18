"""
Show a cube for each available texture name
any jpg file can be used as texture.
"""
from vtkplotter import Plotter, Cube, Text
from vtkplotter.settings import textures, textures_path

print(__doc__)
print(textures_path)
print(textures)

vp = Plotter(N=len(textures), axes=0)

for i, txt in enumerate(textures):
    if i>30: continue
    cb = Cube().texture(txt)
    tname = Text(txt, pos=3)
    vp.show(cb, tname, at=i)

vp.show(interactive=1)
