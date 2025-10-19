class Rectangle():
    def __init__(self, height, width):
        self._height = height
        self._width = width
    def show(self):
        print('Height is', self.height, 'and width is', self.width)

    @property
    def height(self):
        return (self._height * 2)

    @property
    def width(self):
        return (self._width * 2)
    
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print('Height must be greater than zero')

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print('Width must be greater than zero')

    @height.deleter
    def height(self):
        del self._height
        print('Private height deleted')

    @width.deleter
    def width(self):
        del self._width
        print('Private width deleted')

r = Rectangle(4, 5)
r.show()
print(r.height, r.width)
r.height = 4
r.width = 0

del r.height
del r.width

# r.show()

