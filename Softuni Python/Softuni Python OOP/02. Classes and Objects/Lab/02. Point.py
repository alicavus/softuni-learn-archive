class Point:
    def __init__(p, x: int = 0, y: int = 0):
        p.x = x
        p.y = y

    def set_x(p, new_x: int = 0):
        p.x = new_x
    
    def set_y(p, new_y: int = 0):
        p.y = new_y
    
    def __str__(p):
        return f"The point has coordinates ({p.x},{p.y})"

p = Point(2, 4)
print(p)
p.set_x(3)
p.set_y(5)
print(p)