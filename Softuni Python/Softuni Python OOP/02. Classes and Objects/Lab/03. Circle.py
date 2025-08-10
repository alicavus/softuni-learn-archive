from math import pi, pow

class Circle:
    pi = float(f"{pi:.2f}")

    def __init__(self, radius: float = 0):
        self.radius = radius
        pass

    def set_radius(self, new_radius: float = 0):
        self.radius = new_radius
    
    def get_area(self):
        return Circle.pi * pow(self.radius, 2)
    
    def get_circumference(self):
        return Circle.pi * self.radius * 2

circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
    
