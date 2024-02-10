#!/user/bin/python3
"""
Write the class Square that inherits from Rectangle:
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Implements the square shape.
    Args:
        size: length of square
        x: x coordinate position of square
        y: y coordinate position of square
        id: identification number of square
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.height)

    def update(self, *args, **kwargs):
        """
        this function assigns an argument to each attribute of object.
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        Args: list of attributes to be added.
        """
        if args and len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
            return
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def to_dictionary(self):
        """
        returns the dictionary representation of square.
        """
        rep = {}
        for key, val in self.__dict__.items():
            if key == "_Rectangle__width":
                rep["size"] = val
            if key == "_Rectangle__x":
                rep["x"] = val
            if key == "_Rectangle__y":
                rep["y"] = val
            if key == "id":
                rep["id"] = val
        return rep
