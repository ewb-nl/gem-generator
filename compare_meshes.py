
import math
import numpy as np
import trimesh
import scipy.spatial as sp

# attach to logger so trimesh messages will be printed to console
#trimesh.util.attach_to_log()

meshes = []

# load a file by name or from a buffer
meshes.append(trimesh.load('gems/gem1.stl'))
#meshes.append(trimesh.load('gems/gem2_1.stl'))
meshes.append(trimesh.load('gems/gem2.stl'))

volumes = []
inertias = []
for mesh in meshes:
  mesh.units = 'm'
  mesh.density = 3.150 # kg/dm3
  volumes.append(mesh.volume)
  
  # move origin to centre of mass
  mesh.vertices -= mesh.center_mass
  
  # rotate mesh to align principle moment of inertia
  mesh.apply_transform(mesh.principal_inertia_transform)
  
  inertias.append(mesh.moment_inertia)
  mesh.show()

# get mesh overlap
intersection = trimesh.boolean.intersection(meshes)
intersection.units = 'm'
intersection.density = 3.150 # g/cm3

print 'Gem volumes (cm3): %.3f %.3f' % (volumes[0], volumes[1])

print 'Volume overlap: %.2f%%' % (100 * intersection.volume / max(volumes[0], volumes[1]))

print 'Shape distribution similarity: %.2f%%' % (100 * (1-np.linalg.norm(np.diagonal(inertias[0]-inertias[1])) / max(np.linalg.norm(inertias[0]), np.linalg.norm(inertias[1]))))

#print len(meshes[0].vertices)
#print len(meshes[1].vertices)

meshes_plot = None
meshes_max = len(meshes) - 1
for i, mesh in enumerate(meshes):
  color = [255*i/meshes_max, 255-255*i/meshes_max, 255-255*i/meshes_max, 100]
  #for facet in mesh.facets:
  #  mesh.visual.face_colors[facet] = color
  for i in range(0,len(mesh.visual.vertex_colors)):
    mesh.visual.vertex_colors[i] = color

  if meshes_plot is None:
    meshes_plot = mesh
  else:
    meshes_plot += mesh

meshes_plot.show()

