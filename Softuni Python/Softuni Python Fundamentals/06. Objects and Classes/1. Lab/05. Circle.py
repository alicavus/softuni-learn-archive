class Circle:
    __pi = 3.14

    def __init__(self, diameter: float):
        self.diameter = diameter
        self.radius = diameter / 2
    
    def calculate_circumference(self):
        return self.__pi * self.diameter
    
    def calculate_area(self):
        return self.__pi * self.radius ** 2
    
    def calculate_area_of_sector(self, angle: float):
        return angle / 360 * self.calculate_area()

'''
circle = Circle(10)
print(f'{circle.calculate_area()}')
print(f'{circle.calculate_circumference()}')
print(f'{circle.calculate_area_of_sector(5)}')
'''
    

    