import math

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

    def __sub__(self, other):
        return Vec3f(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def normalize(self):
        length = self.length()
        return Vec3f(self.x / length, self.y / length, self.z / length)

    def __mul__(self, scalar):
        return Vec3f(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __add__(self, other):
        return Vec3f(self.x + other.x, self.y + other.y, self.z + other.z)


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