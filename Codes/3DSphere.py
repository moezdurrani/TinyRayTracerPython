from vectors import *
import numpy as np
from PIL import Image
import struct

class Sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def ray_intersect(self, orig, dir):
        OtC = self.center - orig
        dt = OtC.dot(dir)
        d2 = OtC.dot(OtC) - dt * dt
        if d2 > self.radius * self.radius:
            return False
        thc = math.sqrt(self.radius * self.radius - d2)
        t0 = dt - thc
        t1 = dt + thc
        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return False
        return True
# orig, origin of the ray
# dir, direction of the ray
# OtC, vector from origin of the ray to the center of the sphere
# dtt, dot product of OtC and dir (the direction of the ray)
# d2, the squared length of OtC minus the squared length of the projection of OtC onto dir.
# d2 is the perpendicular distance between the ray and the center of the radius

def cast_ray(orig, dir, sphere):
    sphere_dist = float("inf")
    if not sphere.ray_intersect(orig, dir):
        return Vec3f(0.2, 0.7, 0.8)  # background color

    return Vec3f(0.4, 0.4, 0.3)  # Sphere Intersection color

def render(sphere):
    width = 1024
    height = 768
    fov = math.pi / 2.0 # Field of View of the camera
    framebuffer = [Vec3f(0, 0, 0)] * (width * height)

    for j in range(height):
        for i in range(width):
            x = (2 * (i + 0.5) / float(width) - 1) * math.tan(fov / 2.0) * width / float(height)
            y = -(2 * (j + 0.5) / float(height) - 1) * math.tan(fov / 2.0)
            dir = Vec3f(x, y, -1).normalize()
            framebuffer[i + j * width] = cast_ray(Vec3f(0, 0, 0), dir, sphere)

    image = Image.new("RGB", (width, height))

    for j in range(height):
        for i in range(width):
            pixel_color = framebuffer[i + j * width]
            r, g, b = int(255 * max(0, min(1, pixel_color.x))), int(255 * max(0, min(1, pixel_color.y))), int(
                255 * max(0, min(1, pixel_color.z))
            )
            image.putpixel((i, j), (r, g, b))

    image.save("out.png", "PNG")

def main():
    sphere = Sphere(Vec3f(-3, 0, -16), 2)
    render(sphere)

if __name__ == "__main__":
    main()