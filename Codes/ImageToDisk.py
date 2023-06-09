from vectors import *
import numpy as np
from PIL import Image

def render():
    width = 1024
    height = 768
    framebuffer = [Vec3f() for _ in range(width * height)]

    for j in range(height):
        for i in range(width):
            framebuffer[i + j * width] = Vec3f(j / float(height), i / float(width), 0)

    image = np.empty((height, width, 3), dtype=np.uint8)
# Creating a numpy array called image with a height and width and 3 channels for rgb colors

    for i in range(height * width):
        for j in range(3):
            image[i // width, i % width, j] = int(255 * max(0, min(1, framebuffer[i][j])))

    image = Image.fromarray(image)
    image.save("out.png")

def main():
    render()

if __name__ == "__main__":
    main()
