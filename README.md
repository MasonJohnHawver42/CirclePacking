# CirclePacking

# What I do
Fill 2d planes with circles.

# How I do it
Adding randomly generated circles, then grow them untill they intersect another circle.

# What you need
numpy and opencv

# How to use me
normal circle Packing

    from CirclePacking import *

    size = (800, 600)  #(w, h)
    max_iter = 1000
    min_radius = 4
    max_radius = -1  # negative radius implies no max radius
    growthPerIter = 5
    newCirclePerIter = 1

    showCirclePacking(size[1], size[0], max_iter, min_radius, max_radius, growthPerIter, newCirclePerIter)
    
circle packing from an img

    from CirclePacking import *

    img = "img_directory/img_name.img_format"
    max_iter = 1000
    min_radius = 4
    max_radius = -1  # negative radius implies no max radius
    growthPerIter = 5
    newCirclePerIter = 1

    circlePackingFromImg(img, max_iter, min_radius, max_radius, growthPerIter, newCirclePerIter)
