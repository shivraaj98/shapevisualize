# tests/test_shapes.py
import unittest
from shapes import Sphere, Cone, Cylinder, Pyramid, Triangle
import math

class TestSphere(unittest.TestCase):
    def test_sphere_from_radius(self):
        s = Sphere(radius=2)
        self.assertAlmostEqual(s.volume, (4/3)*math.pi*8, places=2)
        self.assertAlmostEqual(s.surface_area, 16*math.pi, places=2)

class TestCone(unittest.TestCase):
    def test_cone_from_radius_height(self):
        c = Cone(radius=3, height=4)
        self.assertAlmostEqual(c.slant_height, 5, places=2)
        self.assertAlmostEqual(c.volume, (1/3)*math.pi*9*4, places=2)

class TestTriangle(unittest.TestCase):
    def test_triangle_base_height(self):
        t = Triangle(base=4, height=3)
        self.assertEqual(t.area, 6)

if __name__ == '__main__':
    unittest.main()