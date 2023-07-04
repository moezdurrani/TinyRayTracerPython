import math
import sys
from typing import List
from math import sqrt
from vectors import *

class Model:
    # def __init__(self, filename: str, material) -> None:
    #     self.verts: List[Vec3f] = []
    #     self.faces: List[Vec3i] = []
    #     self.load_model(filename)
    #     self.material = material

    def __init__(self, filename, material):
        self.verts = []
        self.faces = []
        self.material = material
        self.load_model(filename)

    def load_model(self, filename: str) -> None:
        try:
            with open(filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line.startswith('v '):
                        coordinates = line[2:].split()
                        vertex = Vec3f(float(coordinates[0])-5, float(coordinates[1]), float(coordinates[2])-18)
                        self.verts.append(vertex)
                    elif line.startswith('f '):
                        indices = line[2:].split()
                        face = Vec3i(int(indices[0]) - 1, int(indices[1]) - 1, int(indices[2]) - 1)
                        self.faces.append(face)
        except FileNotFoundError:
            print(f"Failed to open {filename}")
            sys.exit(1)

        print(f"# v# {len(self.verts)} f# {len(self.faces)}")

        min_vertex, max_vertex = self.get_bbox()
        print(f"bbox: [{min_vertex} : {max_vertex}]")

    def ray_triangle_intersect(self, fi: int, orig: Vec3f, dir: Vec3f, tnear: float, tfar=float('inf')) -> bool:
        def cross(v1: Vec3f, v2: Vec3f) -> Vec3f:
            return Vec3f(
                v1.y * v2.z - v1.z * v2.y,
                v1.z * v2.x - v1.x * v2.z,
                v1.x * v2.y - v1.y * v2.x
            )

        def dot(v1: Vec3f, v2: Vec3f) -> float:
            return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

        edge1 = self.point(self.vert(fi, 1)) - self.point(self.vert(fi, 0))
        edge2 = self.point(self.vert(fi, 2)) - self.point(self.vert(fi, 0))
        pvec = cross(dir, edge2)
        det = dot(edge1, pvec)
        if det < 1e-5:
            return False

        tvec = orig - self.point(self.vert(fi, 0))
        u = dot(tvec, pvec)
        if u < 0 or u > det:
            return False

        qvec = cross(tvec, edge1)
        v = dot(dir, qvec)
        if v < 0 or u + v > det:
            return False

        inv_det = 1.0 / det
        tnear = dot(edge2, qvec) * inv_det
        return tnear > 1e-5

    def nverts(self) -> int:
        return len(self.verts)

    def nfaces(self) -> int:
        return len(self.faces)

    def get_face(self, index: int) -> Vec3i:
        assert 0 <= index < self.nfaces()
        return self.faces[index]

    def get_bbox(self) -> (Vec3f, Vec3f):
        min_vertex = max_vertex = self.verts[0]
        for vertex in self.verts[1:]:
            for i in range(3):
                min_vertex = Vec3f(min(min_vertex.x, vertex.x), min(min_vertex.y, vertex.y),
                                   min(min_vertex.z, vertex.z))
                max_vertex = Vec3f(max(max_vertex.x, vertex.x), max(max_vertex.y, vertex.y),
                                   max(max_vertex.z, vertex.z))
        return min_vertex, max_vertex

    def point(self, i: int) -> Vec3f:
        assert 0 <= i < self.nverts()
        return self.verts[i]

    def vert(self, fi: int, li: int) -> int:
        assert 0 <= fi < self.nfaces() and 0 <= li < 3
        face = self.faces[fi]
        if li == 0:
            return face.x
        elif li == 1:
            return face.y
        elif li == 2:
            return face.z

    def __str__(self) -> str:
        output = ""
        for i in range(self.nverts()):
            output += f"v {self.point(i)}\n"
        for i in range(self.nfaces()):
            output += "f "
            for k in range(3):
                output += f"{self.vert(i, k) + 1} "
            output += "\n"
        return output

    # def cross(self, other):
    #     if isinstance(other, Vec3f):
    #         return Vec3f(
    #             self.y * other.z - self.z * other.y,
    #             self.z * other.x - self.x * other.z,
    #             self.x * other.y - self.y * other.x
    #         )

    def compute_normal(self, face):
        v0 = self.point(face.x)
        v1 = self.point(face.y)
        v2 = self.point(face.z)
        edge1 = v1 - v0
        edge2 = v2 - v0
        N = edge1.cross(edge2).normalize()
        return N


