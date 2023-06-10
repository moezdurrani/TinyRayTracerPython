from vectors import *
import numpy as np
from PIL import Image
import struct

class Material:
    def __init__(self, diffuse_color=Vec3f(0, 0, 0)):
        self.diffuse_color = diffuse_color

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


def scene_intersect(orig, dir, spheres):
    spheres_dist = math.inf
    hit = None
    N = None
    material = None
    for i in range(len(spheres)):
        dist_i = [0.0]
        if spheres[i].ray_intersect(orig, dir, dist_i) and dist_i[0] < spheres_dist:
            spheres_dist = dist_i[0]
            hit = orig + dir * dist_i[0]
            N = (hit - spheres[i].center).normalize()
            material = spheres[i].material
    return hit, N, material

def cast_ray(orig, dir, spheres):
    point, N, material = scene_intersect(orig, dir, spheres)

    if point is None:
        return Vec3f(0.2, 0.7, 0.8)  # background color

    light_dir = (Vec3f(1, 4, -1) - point).normalize()  # Example light direction

    # Lambertian reflection model
    diffuse_color = material.diffuse_color
    intensity = max(0, light_dir.dot(N))
    final_color = diffuse_color * intensity

    return diffuse_color



def render(spheres):
    width = 1024
    height = 768
    fov = math.pi / 2.0 # Field of View of the camera
    framebuffer = [Vec3f(0, 0, 0)] * (width * height)

    for j in range(height):
        for i in range(width):
            x = (2 * (i + 0.5) / float(width) - 1) * math.tan(fov / 2.0) * width / float(height)
            y = -(2 * (j + 0.5) / float(height) - 1) * math.tan(fov / 2.0)
            dir = Vec3f(x, y, -1).normalize()
            framebuffer[i + j * width] = cast_ray(Vec3f(0, 0, 0), dir, spheres)

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
    ivory = Material(Vec3f(0.4, 0.4, 0.3))
    red_rubber = Material(Vec3f(0.3, 0.1, 0.1))

    spheres = []
    spheres.append(Sphere(Vec3f(-3, 0, -16), 2, ivory))
    spheres.append(Sphere(Vec3f(-1.0, -1.5, -12), 2, red_rubber))
    spheres.append(Sphere(Vec3f(1.5, -0.5, -18), 3, red_rubber))
    spheres.append(Sphere(Vec3f(7, 5, -18), 4, ivory))

    render(spheres)

if __name__ == "__main__":
    main()