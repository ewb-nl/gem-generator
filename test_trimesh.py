import numpy as np
import trimesh

# attach to logger so trimesh messages will be printed to console
trimesh.util.attach_to_log()

# load a file by name or from a buffer
mesh = trimesh.load('gems/gem1.stl')
mesh.units = 'm'

print dir(mesh)

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
print mesh.moment_inertia # todo generate prinicple moments of inertia to get rotationally invariate values

quit()

# is the current mesh watertight?
mesh.is_watertight

# what's the euler number for the mesh?
mesh.euler_number

# the convex hull is another Trimesh object that is available as a property
# lets compare the volume of our mesh with the volume of its convex hull
np.divide(mesh.volume, mesh.convex_hull.volume)

# since the mesh is watertight, it means there is a
# volumetric center of mass which we can set as the origin for our mesh
mesh.vertices -= mesh.center_mass

# facets are groups of coplanar adjacent faces
# set each facet to a random color
# colors are 8 bit RGBA by default (n,4) np.uint8
for facet in mesh.facets:
    mesh.visual.face_colors[facet] = trimesh.visual.random_color()

# preview mesh in an opengl window if you installed pyglet with pip
mesh.show()

# transform method can be passed a (4,4) matrix and will cleanly apply the transform
mesh.apply_transform(trimesh.transformations.random_rotation_matrix())

# axis aligned bounding box is available
mesh.bounding_box.extents

# a minimum volume oriented bounding box also available
# primitives are subclasses of Trimesh objects which automatically generate
# faces and vertices from data stored in the 'primitive' attribute
mesh.bounding_box_oriented.primitive.extents
mesh.bounding_box_oriented.primitive.transform

# show the mesh appended with its oriented bounding box
# the bounding box is a trimesh.primitives.Box object, which subclasses
# Trimesh and lazily evaluates to fill in vertices and faces when requested
# (press w in viewer to see triangles)
(mesh + mesh.bounding_box_oriented).show()

# bounding spheres and bounding cylinders of meshes are also
# available, and will be the minimum volume version of each
# except in certain degenerate cases, where they will be no worse
# than a least squares fit version of the primitive.
print(mesh.bounding_box_oriented.volume, 
      mesh.bounding_cylinder.volume,
      mesh.bounding_sphere.volume)
