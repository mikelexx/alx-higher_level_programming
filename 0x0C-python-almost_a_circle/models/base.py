#!/usr/bin/python3

"""
This module contains class that is  “base” of all other\
        classes in this project.
"""
import json
import turtle


class Base():
    """
    This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your\
    future classes and to avoid duplicating the same code (by \
    extension, same bugs).
    Args:
        id (int): assumed to be always integer.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This function returns JSON string representation
        of a list_dictionaries.
        Args:
            list_dictionaries: a list of dictionaries.
        Returns: JSON string representation of list_dictionaries
        or "[]" if the argument is None or empty.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file:
        if list_objs in None, it saves an empty list.
        The filename must be: <Class name>.json - example: Rectangle.json.
        Args:
            list_objs:  is a list of instances who inherits
            of Base - example: list of Rectangle or list of
            Square instances.
        """
        json_list_objs = Base.to_json_string(
                [obj.to_dictionary() for obj in list_objs])
        filename = str(cls.__name__) + ".json"
        print(filename)
        with open(filename, "w", encoding="UTF8") as f:
            f.write(json_list_objs)

    def from_json_string(json_string):
        """
         this function returns the list of the JSON string
         representation json_string.
         Args:
            json_string: string representation of a list of dictionaries.
        Returns: empty list if json_string is None else the list represented
        by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        that returns an instance with all attributes already set:
        Args:
            dictionary: attributes to the new instance to be created.
        """
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 2)
            new_instance.update(**dictionary)
            return new_instance
        if cls.__name__ == "Square":
            new_instance = cls(4)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """
        returns: a list of instances otherwise empty list if
        file supposed to have the list doesn't exist.
        """
        instances_list = []
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r", encoding="UTF8") as f:
                list_dictionaries = cls.from_json_string(f.read())
            for dict_obj in list_dictionaries:
                instances_list.append(cls.create(**dict_obj))
            return instances_list
        except FileNotFoundError:
            return instances_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serializes list of objects in CSV
        Args:
            list_objs: list of objects
        """
        filename = str(cls.__name__) + ".csv"
        with open(filename, "a", encoding="UTF8") as f:
            if cls.__name__ == "Rectangle":
                count = 0
                for obj in list_objs:
                    if count != 0 and count != len(list_objs):
                        f.write(",")
                    elif count != 0:
                        f.write(",")
                    f.write(str(obj.id))
                    f.write(str(obj.width))
                    f.write(str(obj.height))
                    f.write(str(obj.x))
                    f.write(str(obj.y))
                    count += 1
            if cls.__name__ == "Square":
                count = 0
                for obj in list_objs:
                    if count != 0 and count != len(list_objs):
                        f.write(",")
                    f.write(str(obj.id))
                    f.write(str(obj.size))
                    f.write(str(obj.x))
                    f.write(str(obj.y))
                    count += 1
    
    @classmethod
    def load_from_file_csv(cls):
        """
        deserializes csv values  into list of objects
        """
        filename = str(cls.__name__) + ".csv"
        with open(filename, "r", encoding="UTF8") as f:
            instances_list = []
            list_vals = f.read()
            print(list_vals)
            if cls.__name__ == "Rectangle":
                for i in range(0, len(list_vals), 5):
                        obj = {}
                        obj["id"] = int(list_vals[i])
                        obj["width"] = int(list_vals[i+1])
                        obj["height"] = int(list_vals[i + 2])
                        obj["x"] = int(list_vals[i + 3])
                        obj["y"] = int(list_vals[i + 4])
                        print(obj)
                        instances_list.append(cls.create(**obj))
            elif cls.__name__ == "Square":
                for i in range(0, len(list_vals), 4):
                    obj = {}
                    obj["id"] = int(list_val[i])
                    obj["size"] = int(list_val[i + 1])
                    obj["x"] = int(list_val[i + 2])
                    obj["y"] = int(list_val[i + 3])
                    print(obj)
                    instances_list.append(cls.create(**obj))
            return instances_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        this function opens a window and draws all the Rectangles
        and Squares:
        Args:
            list_rectangles: list of Rectangle object
            list_squares: list of Square objects
        """

        my_turtle = turtle.Turtle()
        screen = my_turtle.Screen()
        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.right(90)
                turtle.forward(rect.height)
                turtle.right(90)
        for sq in list_squares:
            turtle.penup()
            turtle.goto(sq.x, sq.y)
            turtle.pendown()
            for _ in range(2):
                turtle.forward(sq.size)
                turtle.right(90)
                turtle.forward(sq.size)
                turtle.right(90)
        screen.exitonclick()

