# public attribute are used freely.
# private attribute can be used inside of class only.
# protected attribute are used inside of class and it's subclass.

class JustAttribute:
    def __init__(self):
        self.attribute_public = 'public'
        self._attribute_protected = 'protected'
        self.__attribute_private = 'private'
    
attribute = JustAttribute()
print(attribute.attribute_public)
print(attribute._attribute_protected)
print(attribute.__attribute_private)

# To access private attribute we have to use _ underscore with classname.
print(attribute._JustAttribute__attribute_private)


#****************************************************************************************
# private and public methods in python

class JustPass:
    def myclassmethod(self):
        print('This is public method....')
    def __myclassIsPrivate(self):
        print('This is private class ......')
just = JustPass()
just.myclassmethod()
just.__myclassIsPrivate()

# To access private method we have to use _ underscore with classname.
just._JustPass__myclassIsPrivate()

#*********************************************************************************************

class SetDimensions:
    _height = None
    _weight = None
    def using_dime(self,ht,wt):
        self._height = ht
        self._weight = wt
class Rectangle(SetDimensions):
    def area(self):
        print(f"area of rectangle is {self._weight * self._height}")
class Triangle(SetDimensions):
    def area(self):
        print(f"area of triangle is {(self._weight*self._height)/2}")
rect = Rectangle()
tri = Triangle()
rect.using_dime(50,30)
tri.using_dime(40,20)
rect.area()
tri.area()