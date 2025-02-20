# shapes.py
import math

class Shape:
    """Base class for all 3D shapes."""
    pass

class Sphere(Shape):
    def __init__(self, radius=None, volume=None, surface_area=None):
        params = [radius, volume, surface_area]
        if sum(p is not None for p in params) < 1:
            raise ValueError("At least one parameter must be provided.")
        
        self.radius = radius
        self.volume = volume
        self.surface_area = surface_area
        self._calculate_missing()
        self._validate()

    def _calculate_missing(self):
        if self.radius is not None:
            self.volume = (4/3) * math.pi * (self.radius ** 3)
            self.surface_area = 4 * math.pi * (self.radius ** 2)
        elif self.volume is not None:
            self.radius = ((3 * self.volume) / (4 * math.pi)) ** (1/3)
            self.surface_area = 4 * math.pi * (self.radius ** 2)
        elif self.surface_area is not None:
            self.radius = math.sqrt(self.surface_area / (4 * math.pi))
            self.volume = (4/3) * math.pi * (self.radius ** 3)

    def _validate(self):
        if self.radius <= 0 or (self.volume is not None and self.volume <= 0) or (self.surface_area is not None and self.surface_area <= 0):
            raise ValueError("Parameters must be positive.")

class Cone(Shape):
    def __init__(self, radius=None, height=None, slant_height=None, volume=None, surface_area=None):
        params = [radius, height, slant_height, volume, surface_area]
        if sum(p is not None for p in params) < 2:
            raise ValueError("At least two parameters must be provided.")
        
        self.radius = radius
        self.height = height
        self.slant_height = slant_height
        self.volume = volume
        self.surface_area = surface_area
        self._calculate_missing()
        self._validate()

    def _calculate_missing(self):
        if self.radius is not None and self.height is not None:
            self.slant_height = math.sqrt(self.radius**2 + self.height**2)
            self.volume = (1/3) * math.pi * self.radius**2 * self.height
            self.surface_area = math.pi * self.radius * (self.radius + self.slant_height)
        elif self.radius is not None and self.slant_height is not None:
            self.height = math.sqrt(self.slant_height**2 - self.radius**2)
            self.volume = (1/3) * math.pi * self.radius**2 * self.height
            self.surface_area = math.pi * self.radius * (self.radius + self.slant_height)
        elif self.radius is not None and self.volume is not None:
            self.height = (3 * self.volume) / (math.pi * self.radius**2)
            self.slant_height = math.sqrt(self.radius**2 + self.height**2)
            self.surface_area = math.pi * self.radius * (self.radius + self.slant_height)
        # Additional cases can be added for other parameter combinations

    def _validate(self):
        if any(val <= 0 for val in [self.radius, self.height, self.slant_height, self.volume, self.surface_area] if val is not None):
            raise ValueError("Parameters must be positive.")

class Cylinder(Shape):
    def __init__(self, radius=None, height=None, volume=None, surface_area=None):
        params = [radius, height, volume, surface_area]
        if sum(p is not None for p in params) < 2:
            raise ValueError("At least two parameters must be provided.")
        
        self.radius = radius
        self.height = height
        self.volume = volume
        self.surface_area = surface_area
        self._calculate_missing()
        self._validate()

    def _calculate_missing(self):
        if self.radius is not None and self.height is not None:
            self.volume = math.pi * self.radius**2 * self.height
            self.surface_area = 2 * math.pi * self.radius * (self.radius + self.height)
        elif self.radius is not None and self.volume is not None:
            self.height = self.volume / (math.pi * self.radius**2)
            self.surface_area = 2 * math.pi * self.radius * (self.radius + self.height)
        elif self.height is not None and self.volume is not None:
            self.radius = math.sqrt(self.volume / (math.pi * self.height))
            self.surface_area = 2 * math.pi * self.radius * (self.radius + self.height)
        # Additional cases can be added

    def _validate(self):
        if any(val <= 0 for val in [self.radius, self.height, self.volume, self.surface_area] if val is not None):
            raise ValueError("Parameters must be positive.")

class Pyramid(Shape):
    def __init__(self, base_length=None, height=None, volume=None, surface_area=None):
        params = [base_length, height, volume, surface_area]
        if sum(p is not None for p in params) < 2:
            raise ValueError("At least two parameters must be provided.")
        
        self.base_length = base_length
        self.height = height
        self.volume = volume
        self.surface_area = surface_area
        self._calculate_missing()
        self._validate()

    def _calculate_missing(self):
        if self.base_length is not None and self.height is not None:
            self.volume = (1/3) * self.base_length**2 * self.height
            slant_height = math.sqrt((self.base_length / 2)**2 + self.height**2)
            self.surface_area = self.base_length**2 + 2 * self.base_length * slant_height
        elif self.base_length is not None and self.volume is not None:
            self.height = (3 * self.volume) / (self.base_length**2)
            slant_height = math.sqrt((self.base_length / 2)**2 + self.height**2)
            self.surface_area = self.base_length**2 + 2 * self.base_length * slant_height
        # Additional cases can be added

    def _validate(self):
        if any(val <= 0 for val in [self.base_length, self.height, self.volume, self.surface_area] if val is not None):
            raise ValueError("Parameters must be positive.")

class Triangle(Shape):
    def __init__(self, base=None, height=None, area=None):
        params = [base, height, area]
        if sum(p is not None for p in params) < 2:
            raise ValueError("At least two parameters must be provided.")
        
        self.base = base
        self.height = height
        self.area = area
        self._calculate_missing()
        self._validate()

    def _calculate_missing(self):
        if self.base is not None and self.height is not None:
            self.area = 0.5 * self.base * self.height
        elif self.base is not None and self.area is not None:
            self.height = (2 * self.area) / self.base
        elif self.height is not None and self.area is not None:
            self.base = (2 * self.area) / self.height

    def _validate(self):
        if any(val <= 0 for val in [self.base, self.height, self.area] if val is not None):
            raise ValueError("Parameters must be positive.")