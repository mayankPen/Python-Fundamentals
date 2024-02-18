from polygon import Polygon
from shape import Shape
class Rectangle(Polygon,Shape):
    def area(self):
        print(f'area of recatangle is {self.get_width()*self.get_height()}')