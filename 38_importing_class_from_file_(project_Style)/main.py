from rectangle import Rectangle
from triangle import Triangle
rect = Rectangle()
tri = Triangle()
rect.set_color('blue')
tri.set_color('green')
rect.set_dimensions(30,30)
tri.set_dimensions(40,30)
rect.area()
tri.area()
print(rect.get_color())
print(tri.get_color())