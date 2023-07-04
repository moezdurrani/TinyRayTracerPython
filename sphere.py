import math
from vectors import *

class Sphere:
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersect(self, orig, dir, t0):
        OtC = self.center - orig
        dt = OtC.dot(dir)
        d2 = OtC.dot(OtC) - dt * dt
        if d2 > self.radius * self.radius:
            return False
        thc = math.sqrt(self.radius * self.radius - d2)
        t0[0] = dt - thc
        t1 = dt + thc
        if t0[0] < 0:
            t0[0] = t1
        if t0[0] < 0:
            return False
        return True
# orig, origin of the ray
# dir, direction of the ray
# OtC, vector from origin of the ray to the center of the sphere
# dtt, dot product of OtC and dir (the direction of the ray)
# d2, the squared length of OtC minus the squared length of the projection of OtC onto dir.
# d2 is the perpendicular distance between the ray and the center of the radius