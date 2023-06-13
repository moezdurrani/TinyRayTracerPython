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

    # def __sub__(self, other):
    #     if isinstance(other, (int, float)):
    #         return Vec3f(self.x - other, self.y - other, self.z - other)
    #     elif isinstance(other, Vec3f):
    #         return Vec3f(self.x - other.x, self.y - other.y, self.z - other.z)
    #     else:
    #         raise TypeError("Unsupported operand type for -: 'Vec3f' and '{}'".format(type(other)))

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    # def normalize(self):
    #     length = self.length()
    #     return Vec3f(self.x / length, self.y / length, self.z / length)

    def normalize(self):
        length = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        if length != 0:
            return Vec3f(self.x / length, self.y / length, self.z / length)
        else:
            return Vec3f()

    def norm(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    # def __mul__(self, scalar):
    #     return Vec3f(self.x * scalar, self.y * scalar, self.z * scalar)

    def __mul__(self, other):
        if isinstance(other, Vec3f):
            return Vec3f(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, (int, float)):
            return Vec3f(self.x * other, self.y * other, self.z * other)

    # def __mul__(self, other):
    #     if isinstance(other, Vec3f):
    #         return Vec3f(self.x * other.x, self.y * other.y, self.z * other.z)
    #     elif isinstance(other, (int, float)):
    #         return Vec3f(self.x * other, self.y * other, self.z * other)
    #     else:
    #         raise TypeError("Unsupported operand type for *: 'Vec3f' and '{}'".format(type(other)))

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __add__(self, other):
        return Vec3f(self.x + other.x, self.y + other.y, self.z + other.z)

    def __neg__(self):
        return Vec3f(-self.x, -self.y, -self.z)


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

    # Method that allows to access the components of the vectors with vector[i] notation
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        elif index == 3:
            return self.w
        else:
            raise IndexError("Vec3f index out of range")