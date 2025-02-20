# main.py
import argparse
from shapes import Sphere, Cone, Cylinder, Pyramid, Triangle
from visualizer import ShapeVisualizer

def main():
    parser = argparse.ArgumentParser(description='3D Shape Parameter Calculator and Visualizer')
    subparsers = parser.add_subparsers(dest='shape', required=True)

    # Sphere parser
    sphere_parser = subparsers.add_parser('sphere')
    sphere_parser.add_argument('--radius', type=float, required=True, help='Radius of the sphere')
    sphere_parser.add_argument('--volume', type=float, help='Volume of the sphere')
    sphere_parser.add_argument('--surface-area', type=float, dest='surface_area', help='Surface area of the sphere')

    # Cone parser
    cone_parser = subparsers.add_parser('cone')
    cone_parser.add_argument('--radius', type=float, required=True, help='Base radius of the cone')
    cone_parser.add_argument('--height', type=float, required=True, help='Height of the cone')
    cone_parser.add_argument('--slant-height', type=float, dest='slant_height', help='Slant height of the cone')
    cone_parser.add_argument('--volume', type=float, help='Volume of the cone')
    cone_parser.add_argument('--surface-area', type=float, dest='surface_area', help='Surface area of the cone')

    # Cylinder parser
    cylinder_parser = subparsers.add_parser('cylinder')
    cylinder_parser.add_argument('--radius', type=float, required=True, help='Base radius of the cylinder')
    cylinder_parser.add_argument('--height', type=float, required=True, help='Height of the cylinder')
    cylinder_parser.add_argument('--volume', type=float, help='Volume of the cylinder')
    cylinder_parser.add_argument('--surface-area', type=float, dest='surface_area', help='Surface area of the cylinder')

    # Pyramid parser
    pyramid_parser = subparsers.add_parser('pyramid')
    pyramid_parser.add_argument('--base-length', type=float, required=True, help='Base length of the pyramid')
    pyramid_parser.add_argument('--height', type=float, required=True, help='Height of the pyramid')
    pyramid_parser.add_argument('--volume', type=float, help='Volume of the pyramid')
    pyramid_parser.add_argument('--surface-area', type=float, dest='surface_area', help='Surface area of the pyramid')

    # Triangle parser
    triangle_parser = subparsers.add_parser('triangle')
    triangle_parser.add_argument('--base', type=float, required=True, help='Base of the triangle')
    triangle_parser.add_argument('--height', type=float, required=True, help='Height of the triangle')
    triangle_parser.add_argument('--area', type=float, help='Area of the triangle')

    args = parser.parse_args()

    try:
        if args.shape == 'sphere':
            shape = Sphere(radius=args.radius, volume=args.volume, surface_area=args.surface_area)
        elif args.shape == 'cone':
            shape = Cone(radius=args.radius, height=args.height, slant_height=args.slant_height,
                         volume=args.volume, surface_area=args.surface_area)
        elif args.shape == 'cylinder':
            shape = Cylinder(radius=args.radius, height=args.height, volume=args.volume, surface_area=args.surface_area)
        elif args.shape == 'pyramid':
            shape = Pyramid(base_length=args.base_length, height=args.height, volume=args.volume, surface_area=args.surface_area)
        elif args.shape == 'triangle':
            shape = Triangle(base=args.base, height=args.height, area=args.area)
        else:
            raise ValueError("Unsupported shape type.")
        
        ShapeVisualizer.visualize(shape)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()