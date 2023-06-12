from vectors import *
import numpy as np
from PIL import Image
import struct
import math

class light:
    def __init__(self, position, intensity):
        self.position = position
        self.intensity = intensity

class Material:
    def __init__(self, a=None, color=None, spec=None):
        if a is None:
            self.albedo = Vec3f(1, 0, 0)
        else:
            self.albedo = a

        if color is None:
            self.diffuse_color = Vec3f()
        else:
            self.diffuse_color = color

        if spec is None:
            self.specular_exponent = 0
        else:
            self.specular_exponent = spec

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

def reflect(I, N):
    return I - N * 2.0 * (I.dot(N))


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

def cast_ray(orig, dir, spheres, lights, depth=0):

    point, N, material = scene_intersect(orig, dir, spheres)

    if depth > 4 or point is None:
        return Vec3f(0.2, 0.7, 0.8)  # background color

    reflect_dir = reflect(dir, N).normalize()
    reflect_orig = point - N * 1e-3 if reflect_dir.dot(N) < 0 else point + N * 1e-3
    reflect_color = cast_ray(reflect_orig, reflect_dir, spheres, lights, depth + 1)

    diffuse_light_intensity = 0
    specular_light_intensity = 0

    for light in lights:
        light_dir = (light.position - point).normalize()
        light_distance = (light.position - point).length()

        shadow_orig = point - N * 1e-3 if light_dir.dot(N) < 0 else point + N * 1e-3  # checking if the point lies in the shadow of lights[i]

        shadow_pt, shadow_N, tmpmaterial = scene_intersect(shadow_orig, light_dir, spheres)

        if shadow_pt is not None and (shadow_pt - shadow_orig).length() < light_distance:
            continue

        diffuse_light_intensity += light.intensity * max(0.0, light_dir.dot(N))
        specular_light_intensity += pow(max(0.0, -reflect(-light_dir, N).dot(dir)), material.specular_exponent) * light.intensity

    diffuse_color = Vec3f(*material.diffuse_color)  # Convert tuple to Vec3f
    albedo_0, albedo_1, albedo_2 = material.albedo  # Unpack albedo components

    return diffuse_color * diffuse_light_intensity * albedo_0 + Vec3f(1.0, 1.0, 1.0) * specular_light_intensity * albedo_1 + reflect_color * albedo_2


def render(spheres, lights):
    width = 1024
    height = 768
    fov = math.pi / 3.0 # Field of View of the camera
    framebuffer = [Vec3f(0, 0, 0)] * (width * height)

    for j in range(height):
        for i in range(width):
            x = (2 * (i + 0.5) / float(width) - 1) * math.tan(fov / 2.0) * width / float(height)
            y = -(2 * (j + 0.5) / float(height) - 1) * math.tan(fov / 2.0)
            dir = Vec3f(x, y, -1).normalize()
            framebuffer[i + j * width] = cast_ray(Vec3f(0, 0, 0), dir, spheres, lights)

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
    ivory = Material((0.6, 0.3, 0.1), (0.4, 0.4, 0.3), 50.0)
    red_rubber = Material((0.9, 0.1, 0.0), (0.3, 0.1, 0.1), 10.0)
    mirror = Material((0.0, 10.0, 0.8), (1.0, 1.0, 1.0), 1425.0)

    spheres = []
    spheres.append(Sphere(Vec3f(-3, 0, -16), 2, ivory))
    spheres.append(Sphere(Vec3f(-1.0, -1.5, -12), 2, mirror))
    spheres.append(Sphere(Vec3f(1.5, -0.5, -18), 3, red_rubber))
    spheres.append(Sphere(Vec3f(7, 5, -18), 4, mirror))

    lights = []
    lights.append(light(Vec3f(-20,20,20),1.5))
    lights.append(light(Vec3f(30, 50, -25), 1.8))
    lights.append(light(Vec3f(30, 20, 30), 1.7))

    render(spheres,lights)

if __name__ == "__main__":
    main()