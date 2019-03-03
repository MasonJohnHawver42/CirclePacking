from CirclePacking import *

size = (800, 600)  #(w, h)
max_iter = 1000
min_radius = 4
max_radius = -1  # negative radius implies no max radius
growthPerIter = 5
newCirclePerIter = 1

showCirclePacking(size[1], size[0], max_iter, min_radius, max_radius, growthPerIter, newCirclePerIter)
