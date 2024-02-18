from polygon import Polygon
from shape import Shape
class Triangle(Polygon,Shape):
    def area(self):
        print(f"area of triangle is {(self.get_width()*self.get_height())/2}")




