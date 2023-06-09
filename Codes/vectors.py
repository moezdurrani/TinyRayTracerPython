# Creating a 2D Vector with x and y components
# __init__ method to initialize them, if not default is 0
class Vec2f:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


# Creating a 3D Vector with x, y, and z components
class Vec3f:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


# Method that allows to access the components of the vectors with vector[i] notation
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("Vec3f index out of range")


# Creating a 3D Vector with x, y, and z components.
# It has int components, instead of float
class Vec3i:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


# Creating a 4D Vector with x, y, z, and w components.
class Vec4f:
    def __init__(self, x=0, y=0, z=0, w=0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
