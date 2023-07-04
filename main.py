import sys
from vectors import *
import numpy as np
from PIL import Image
import struct
import math
from model import Model
from sphere import Sphere
import time

envmap_width = 0
envmap_height = 0
envmap = []

class light:
    def __init__(self, position, intensity):
        self.position = position
        self.intensity = intensity

class Material:
    def __init__(self, n=None, a=None, color=None, spec=None):
        if n is None:
            self.refractive_index = 1.0
        else:
            self.refractive_index = n

        if a is None:
            self.albedo = Vec4f(1, 0, 0, 0)
        else:
            self.albedo = a

        if color is None:
            self.diffuse_color = (0, 0, 0)
        else:
            self.diffuse_color = color

        if spec is None:
            self.specular_exponent = 0.0
        else:
            self.specular_exponent = spec


def reflect(I, N):
    return I - N * 2.0 * (I.dot(N))

def refract(I, N, refractive_index):
    cosi = -max(-1.0, min(1.0, I.dot(N)))
    etai = 1.0
    etat = refractive_index
    n = N

    if cosi < 0:
        cosi = -cosi
        etai, etat = etat, etai
        n = -N

    eta = etai / etat
    k = 1 - eta * eta * (1 - cosi * cosi)

    if k < 0:
        return Vec3f(0, 0, 0)
    else:
        return I * eta + n * (eta * cosi - math.sqrt(k))

def scene_intersect(orig, dir, spheres, duck):
    spheres_dist = math.inf
    checkerboard_dist = math.inf
    hit = None
    N = None
    material = Material()  # Assign a default Material object

    print('5, intersect')

    for i in range(len(spheres)):
        dist_i = [0.0]
        if spheres[i].ray_intersect(orig, dir, dist_i) and dist_i[0] < spheres_dist:
            spheres_dist = dist_i[0]
            hit = orig + dir * dist_i[0]
            N = (hit - spheres[i].center).normalize()
            material = spheres[i].material

    # Checking for intersections with the obj model


    obj_dist = float('inf')  # Initialize obj_dist with infinity
    faces = duck.faces  # Get the list of faces from the duck model
    for fi in range(duck.nfaces()):
        tnear = [0.0]  # Create a list to store the intersection distance
        if duck.ray_triangle_intersect(fi, orig, dir, tnear[0]):
            face = duck.get_face(fi)
            if tnear[0] < obj_dist:  # Check if the new intersection is closer
                obj_dist = tnear[0]  # Update the obj_dist variable
                hit = orig + dir * tnear[0]
                N = duck.compute_normal(face)  # Compute the surface normal for the triangle
                material = duck.material

    return hit, N, material

def cast_ray(orig, dir, spheres, lights, duck, depth=0):

    print('4, cast ray')

    point, N, material = scene_intersect(orig, dir, spheres, duck)

    if depth > 4 or point is None:
        u = 0.5 + math.atan2(dir.x, dir.z) / (2 * math.pi)
        v = 0.5 + math.asin(dir.y) / math.pi

        envmap_x = int(u * envmap_width)
        envmap_y = int(v * envmap_height)

        background_color = envmap[envmap_x + envmap_y * envmap_width]

        return background_color

    reflect_dir = reflect(dir, N).normalize()
    refract_dir = refract(dir, N, material.refractive_index).normalize()

    reflect_orig = point - N * 1e-3 if reflect_dir.dot(N) < 0 else point + N * 1e-3
    refract_orig = refract_orig = point - N * 1e-3 if refract_dir.dot(N) < 0 else point + N * 1e-3

    reflect_color = cast_ray(reflect_orig, reflect_dir, spheres, lights, duck, depth + 1)
    refract_color = cast_ray(refract_orig, refract_dir, spheres, lights, duck, depth + 1)

    diffuse_light_intensity = 0
    specular_light_intensity = 0

    for light in lights:
        light_dir = (light.position - point).normalize()
        light_distance = (light.position - point).length()

        shadow_orig = point - N * 1e-3 if light_dir.dot(N) < 0 else point + N * 1e-3  # checking if the point lies in the shadow of lights[i]

        shadow_pt, shadow_N, tmpmaterial = scene_intersect(shadow_orig, light_dir, spheres, duck)

        if shadow_pt is not None and (shadow_pt - shadow_orig).length() < light_distance:
            continue

        diffuse_light_intensity += light.intensity * max(0.0, light_dir.dot(N))
        specular_light_intensity += pow(max(0.0, -reflect(-light_dir, N).dot(dir)), material.specular_exponent) * light.intensity

    diffuse_color = Vec3f(*material.diffuse_color)  # Convert tuple to Vec3f
    albedo_0, albedo_1, albedo_2, albedo_3 = material.albedo  # Unpack albedo components

    return diffuse_color * diffuse_light_intensity * albedo_0 + Vec3f(1.0, 1.0, 1.0) * specular_light_intensity * albedo_1 + reflect_color * albedo_2 + refract_color * albedo_3

def render(spheres, lights, duck):
    width = 1024
    height = 768
    fov = math.pi / 3.0 # Field of View of the camera
    framebuffer = [Vec3f(0, 0, 0)] * (width * height)

    print('2, In render')

    for j in range(height):
        for i in range(width):
            x = (2 * (i + 0.5) / float(width) - 1) * math.tan(fov / 2.0) * width / float(height)
            y = -(2 * (j + 0.5) / float(height) - 1) * math.tan(fov / 2.0)
            dir = Vec3f(x, y, -1).normalize()
            framebuffer[i + j * width] = cast_ray(Vec3f(0, 0, 0), dir, spheres, lights, duck)

    image = Image.new("RGB", (width, height))

    for j in range(height):
        for i in range(width):
            pixel_color = framebuffer[i + j * width]
            r, g, b = int(255 * max(0, min(1, pixel_color.x))), int(255 * max(0, min(1, pixel_color.y))), int(
                255 * max(0, min(1, pixel_color.z))
            )
            image.putpixel((i, j), (r, g, b))

    print('3, In render')

    image.save("out.png", "PNG")

def load_environment_map(filename):
    global envmap, envmap_width, envmap_height
    try:
        image = Image.open(filename)
        envmap_width, envmap_height = image.size
        pixmap = image.tobytes()
        envmap = []
        for j in range(envmap_height-1, -1, -1):
            for i in range(envmap_width):
                r = pixmap[(i + j * envmap_width) * 3 + 0]
                g = pixmap[(i + j * envmap_width) * 3 + 1]
                b = pixmap[(i + j * envmap_width) * 3 + 2]
                envmap.append(Vec3f(r, g, b) * (1 / 255.0))
        return envmap, envmap_width, envmap_height
    except IOError:
        sys.stderr.write("Error: can not load the environment map\n")
        sys.exit(-1)

def main():

    start_time = time.time()

    print('0, main started')

    envmap, envmap_width, envmap_height = load_environment_map("envmap.jpg")

    print('0.2, environment loaded')

    ivory = Material(1.0, (0.6, 0.3, 0.1, 0.0), (0.4, 0.4, 0.3), 50.0)
    glass = Material(1.5, (0.0,  0.5, 0.1, 0.8), (0.6, 0.7, 0.8), 125.0)
    red_rubber = Material(1.0, (0.9, 0.1, 0.0, 0.0), (0.3, 0.1, 0.1), 10.0)
    mirror = Material(1.0, (0.0, 10.0, 0.8, 0.0), (1.0, 1.0, 1.0), 1425.0)

    spheres = []
    spheres.append(Sphere(Vec3f(-3, 0, -16), 2, ivory))
    spheres.append(Sphere(Vec3f(-1.0, -1.5, -12), 2, glass))
    spheres.append(Sphere(Vec3f(1.5, -0.5, -18), 3, red_rubber))
    spheres.append(Sphere(Vec3f(7, 5, -18), 4, mirror))

    spheres.append(Sphere(Vec3f(3, 0, -10), 3, red_rubber))

    lights = []
    lights.append(light(Vec3f(-20,20,20),1.5))
    lights.append(light(Vec3f(30, 50, -25), 1.8))
    lights.append(light(Vec3f(30, 20, 30), 1.7))

    print('0.4, lights, spheres and materials added')

    duck = Model('objFiles/polygon.obj', mirror)

    print("1, In main, model created")

    render(spheres,lights, duck)

    end_time = time.time()  # Stop measuring the execution time
    execution_time = (end_time - start_time) / 60.0
    print(f"Execution time: {execution_time} minutes")

if __name__ == "__main__":
    main()