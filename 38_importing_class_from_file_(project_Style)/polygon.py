class Polygon:
    __width = None
    __height= None
    def set_dimensions(self,wdth,hght):
        self.__height = hght
        self.__width = wdth
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height