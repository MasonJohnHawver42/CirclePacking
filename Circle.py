import numpy as np


def getDistance(pos1, pos2):
    return np.sqrt(np.sum(np.power(pos2 - pos1, 2)))


class Circle:
    def __init__(self, pos, r):
        self.pos = pos
        self.radius = r
        self.grow = True

    def growCircle(self, scale=1):
        if self.grow:
            self.radius += scale

    def intersectingOther(self, other):
        """computes wether intersecting another circle"""

        dis = getDistance(self.pos, other.pos)
        if (dis < self.radius + other.radius):
            return True

        else:
            return False
