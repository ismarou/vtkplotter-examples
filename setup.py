from setuptools import setup

try:
    VERSIONFILE = "examples/version.py"
    verstrline = open(VERSIONFILE, "rt").read()
    verstr = verstrline.split('=')[1].replace('\n','').replace("'","")
except:
    verstr='unknown'

##############################################################
setup(
    name='vtkplotter-examples',
    version=verstr,
    packages=['vtkplotter-examples'],
    scripts=[],
    install_requires=['vtkplotter'],
    description="""Repository for vtkplotter examples""",
    author='Marco Musy',
    author_email='marco.musy@embl.es',
    license='MIT',
    url='https://github.com/marcomusy/vtkplotter-examples',
    keywords='vtk vtkplotter 3D visualization mesh numpy',
    classifiers=['Intended Audience :: Science/Research',
                'Intended Audience :: Education',
                'Intended Audience :: Information Technology',
                'Programming Language :: Python',
                'License :: OSI Approved :: MIT License',
                'Topic :: Scientific/Engineering :: Visualization',
                'Topic :: Scientific/Engineering :: Physics',
                'Topic :: Scientific/Engineering :: Medical Science Apps.',
                'Topic :: Scientific/Engineering :: Information Analysis',
                'Programming Language :: Python :: 2.7',
                'Programming Language :: Python :: 3.5',
                'Programming Language :: Python :: 3.6',
                'Programming Language :: Python :: 3.7'
                ],
    include_package_data=True
)


##############################################################
# # check examples
# change version in vtkplotter/version.py

# cd ~/Projects/vtkplotter-examples/
# pip install .

# cd examples && ./run_all.sh
# cd ~/Projects/vtkplotter-examples/
# python prove/test_filetypes.py

# check vtkconvert:
# vtkconvert vtkplotter-examples/data/290.vtk -to ply; vtkplotter vtkplotter-examples/data/290.ply

# check on python2 the same stuff is ok
# cd ~/Projects/vtkplotter/
# sudo -H pip install . -U
# cd ~/Projects/vtkplotter-examples/
# python examples/tutorial.py

# check notebooks:
# cd ~/Projects/vtkplotter/
# jupyter notebook > /dev/null 2>&1
# remove trailing spaces

# cd ~/Projects/vtkplotter/
# rm -rf examples/*/.ipynb_checkpoints examples/*/*/.ipynb_checkpoints .ipynb_checkpoints/
# rm -rf examples/other/dolfin/navier_stokes_cylinder/ examples/other/dolfin/shuttle.xml
# rm examples/other/trimesh/featuretype.STL examples/other/trimesh/machinist.XAML
# rm examples/other/scene.npy examples/other/timecourse1d.npy vtkplotter/data/290.ply
# rm examples/other/voronoi3d.txt examples/other/voronoi3d.txt.vol
# rm examples/other/embryo.html examples/other/embryo.x3d

# git status
# git add [files]
# git commit -a -m 'comment'
# git push

# git status
# (sudo apt install twine)
# (python -m pip install --user --upgrade twine)
# python setup.py sdist bdist_wheel
# twine upload dist/vtkplotter-examples-?.?.?.tar.gz -r pypi
# make release

## to generate gif: ezgif.com

## fenics 2019.2 docker:
# docker pull quay.io/fenicsproject/dolfinx:dev-env-real
# docker run -ti -v $(pwd):/home/musy/my-project/shared --name fenics-container quay.io/fenicsproject/dolfinx:dev-env-real
#
#    cd
#    pip3 install vtkplotter # OR
#    git clone https://github.com/marcomusy/vtkplotter.git
#    cd vtkplotter
#    pip3 -v install . --user
#    
#    cd
#    pip3 install git+https://github.com/FEniCS/fiat.git --upgrade
#    pip3 install git+https://github.com/FEniCS/ufl.git  --upgrade
#    pip3 install git+https://github.com/FEniCS/ffcx.git --upgrade
#    git clone https://github.com/FEniCS/dolfinx.git
#    cd dolfinx
#    mkdir -p build && cd build && cmake -G Ninja -DCMAKE_BUILD_TYPE=Developer ../cpp/
#    ninja -j3 install
#    cd ../python
#    pip3 -v install . --user


























