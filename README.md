# TinyRayTracerPython

As most part of my research is going to be coded in python, I recreated a ray tracer similar to the one I created in C++ (https://github.com/moezdurrani/tinyRayTracer) in python using numpy.

The first part was writing an image to the disk, here is the [code](https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Codes/ImageToDisk.py).

<img src="https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Images/001.png">

I programmed a 3D sphere using the alogirthm given [here](https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Codes/3DSphere.py)

<img src="https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Images/002.png">

Once the 3D Sphere was created, it wasn't hard to add multiple spheres [here](https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Codes/MultipleSpheres.py)

<img src="https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Images/003.png">

Now Lights were added to the scene [here](https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Codes/Lights.py)

<img src="https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Images/004.png">

Reflection added to the lights Using Phong Reflection Model (Ambient Reflection, Diffuse Reflection, Specular Reflection).
The code can be found [here](https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Codes/Reflections.py)

<img src="https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Images/005.png">

Shadows were added [here](https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Codes/Shadows.py)

<img src="https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Images/006.png">

After adding shadows, Refractions were added using this [algorithm](https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Codes/Refractions.py)

<img src="https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Images/007.png">

Then the ChessBoad was added [here](https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Codes/ChessBoard.py)

<img src="https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Images/008.png">

Instead of a constant color as a background, I made a circular image as a background [here](https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Codes/Environment.py)

<img src="https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Images/009.png">



