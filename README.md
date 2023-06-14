# TinyRayTracerPython

As part of my research, I have developed a ray tracer in Python called TinyRayTracerPython. This project is inspired by my previous implementation in C++ (https://github.com/moezdurrani/tinyRayTracer) and has been rewritten using numpy.

## Image Rendering
The first step in this project was to implement image rendering and saving. The code for this functionality can be found [here](https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Codes/ImageToDisk.py).

<img src="https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Images/001.png">

## Creating a 3D Sphere
Next, I implemented a 3D sphere using an algorithm provided [here](https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Codes/3DSphere.py).

<img src="https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Images/002.png">

## Multiple Spheres
Building on the 3D sphere, I extended the ray tracer to support rendering multiple spheres. The code for this can be found [here](https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Codes/MultipleSpheres.py).

<img src="https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Images/003.png">

## Adding Lights
To enhance the scene, I introduced lighting effects. The code for adding lights to the scene can be found [here](https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Codes/Lights.py).

<img src="https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Images/004.png">

## Reflections
Using the Phong Reflection Model, I implemented reflections for the lights in the scene. The code for this feature can be found [here](https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Codes/Reflections.py).

<img src="https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Images/005.png">

## Shadows
To create realistic lighting, I added shadows to the scene. The code for implementing shadows can be found [here](https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Codes/Shadows.py).

<img src="https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Images/006.png">

## Refractions
To simulate the refraction of light, I implemented refractions in the ray tracer. The algorithm used for this feature can be found [here](https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Codes/Refractions.py)

<img src="https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Images/007.png">

## Chessboard
A Chessboard was added in the background temporarily to properly observe how the laws of optics are working. The code was added [here](https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Codes/ChessBoard.py)

<img src="https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Images/008.png">

## Background Image
Instead of a constant color background, I created a circular image to serve as the background. The code for generating the background image can be found [here](https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Codes/Environment.py)

<img src="https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Images/009.png">

## Chessboard Removal
For the purposes of this project, the chessboard was removed from the scene. The modified code without the chessboard can be found [here](https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Codes/NoChessBoard.py)

<img src="https://github.com/moezdurrani/TinyRayTracerPython/blob/main/Images/010.png">



