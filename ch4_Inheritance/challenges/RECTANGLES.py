class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_area(self):
        return self.__width * self.__length

    def get_perimeter(self):
        return 2*self.__width + 2*self.__length


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length,length)