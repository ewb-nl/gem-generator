# gem-generator
Artificial gem database generator for Engineers without Borders Nederland

## Source code
The code here uses different submodules
### Rock generator source code
https://git.blender.org/gitweb/gitweb.cgi/blender-addons-contrib.git/tree/HEAD:/add_mesh_rocks -> snapshot

Description is here:
https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Add_Mesh/Rock_Generator

### blender source code
http://git.blender.org/blender.git

### trimesh, source code
This is the code used to analize the generated meshes
https://github.com/mikedh/trimesh


## Getting Started

To get the repository follow the following instructions:

### Pull submodule elements
The first time you pull the submodules you first have to initialise them
	git submodule init

To pull the latest code
	git submodule update

### Setup virtual python environment
Install virtualenv
	pip install virtualenv

To setup a new virtual python environment
	virtualenv -p /usr/bin/python2.7 venv

Activate the virtual environment
	source venv/bin/activate

Install required packages
	pip install -r requirements.txt

Once you are done with the project, you can exit the virtual environment by typing
	deactivate

## Visualizing the gems in Blender
In blender, you can load the gem meshes and visualize the shape. Additionally, you can directly get the statistis of volume and surface area using the 3D Printing toolbox which can be activated from 'User Preferences -> Add-ons -> Mesh: 3D Print Toolbox'

Note that the dimentions of the mesh are saved in dm.


