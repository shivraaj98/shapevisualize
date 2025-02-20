# visualizer.py
import pyvista as pv
import numpy as np
from shapes import Sphere, Cone, Cylinder, Pyramid, Triangle

class ShapeVisualizer:
    @staticmethod
    def visualize(shape):
        # Implementation for visualizing the shape
        print(f"Visualizing shape: {shape}")
        if isinstance(shape, Sphere):
            mesh = pv.Sphere(radius=shape.radius)
        elif isinstance(shape, Cone):
            mesh = pv.Cone(radius=shape.radius, height=shape.height)
        elif isinstance(shape, Cylinder):
            mesh = pv.Cylinder(radius=shape.radius, height=shape.height)
        elif isinstance(shape, Pyramid):
            mesh = pv.Pyramid(
                base=[[-shape.base_length/2, -shape.base_length/2, 0],
                      [shape.base_length/2, -shape.base_length/2, 0],
                      [shape.base_length/2, shape.base_length/2, 0],
                      [-shape.base_length/2, shape.base_length/2, 0]],
                height=shape.height
            )
        elif isinstance(shape, Triangle):
            points = np.array([
                [0, 0, 0],
                [shape.base, 0, 0],
                [0, shape.height, 0]
            ])
            mesh = pv.PolyData(points, faces=[3, 0, 1, 2])
        else:
            raise ValueError("Unsupported shape type.")
        
        plotter = pv.Plotter()
        plotter.add_mesh(mesh, color='lightblue')
        plotter.show()