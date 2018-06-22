import numpy as np
import trimesh

# attach to logger so trimesh messages will be printed to console
#trimesh.util.attach_to_log()

# load a file by name or from a buffer
mesh = trimesh.load('gems/gem2.stl')
mesh.units = 'm'

#print dir(mesh)

# define density
mesh.density = 3.150 # kg/dm3

# what's the moment of inertia for the mesh?
print 'Volume'
print mesh.volume # volume is stored in dm3

print 'Mass'
print mesh.mass

print 'Centre of Mass'
print mesh.centroid

print 'moments of inertia'
print mesh.moment_inertia

print 'principle moments of inertia'
print trimesh.inertia.transform_inertia(mesh.principal_inertia_transform, mesh.moment_inertia)

print mesh.principal_inertia_components

properties = mesh.mass_properties

# since the mesh is watertight, it means there is a
# volumetric center of mass which we can set as the origin for our mesh
mesh.vertices -= mesh.center_mass

quit()

# preview mesh in an opengl window if you installed pyglet with pip
mesh.show()

