from abc import ABC, abstractmethod
from functools import singledispatch


class Movable(ABC):
    """
    Class that extends "ABS" built-in class.
    """
    def __init__(self):
        """
        Constructor
        """
        pass

    @abstractmethod
    def move(self):
        """
        Abstract method that need to be implement in the successors of this class.
        """
        pass


class Player(Movable):
    """
    Class that extends "Movable" class.
    """
    def __init__(self):
        """
        Constructor
        """
        super().__init__()

    def move(self):
        """
        Implementation of the abstract method of its "parent".
        """
        print("can move to all direction")


class Enemy(Movable):
    """
    Class that extends "Movable" class.
    """
    def __init__(self):
        """
        Constructor
        """
        super().__init__()

    def move(self):
        """
        Implementation of the abstract method of its "parent".
        """
        print("can move only right or left")


###################################

@singledispatch
def is_greater_than(_, __):
    """
    A decorator that wrap a function with 2 arguments that its type is registered.

    :param _: First argument.
    :param __: Second argument.
    :raise: TypeError()
    """
    raise TypeError()


@is_greater_than.register(int)
def _(first_integer: int, second_integer: int) -> None:
    """
    Get 2 integers and print True if the first is greater than second, else False.

    :param first_integer: An integer.
    :param second_integer: An integer.
    """
    print(first_integer > second_integer)


@is_greater_than.register(float)
def _(first_float: float, second_float: float) -> None:
    """
    Get 2 floats and print True if the first is greater than second, else False.

    :param first_float: A float.
    :param second_float: A float.
     """
    print(first_float > second_float)


@is_greater_than.register(str)
def _(first_string: str, second_string: str) -> None:
    """
    Get 2 strings and print True if the first is greater alphabetically than second, else False.

    :param first_string: A string.
    :param second_string: A string.
    """
    print(first_string > second_string)


@is_greater_than.register(list)
def _(first_list: list, second_list: list) -> None:
    """
    Get 2 lists and print True if the first is greater than second, else False.
    Means that it pass simultaneously on both list and compare between the values of the "cells"
    at the same index. Note that all values at the same indexes need to be comparable (int - int,
    str - str, float - float etc...)
    Possible usage:  is_greater_than( [3, "abc", 2.5], [3, "xyz", 5.7] )

    :param first_list: A list.
    :param second_list: A list.
    """
    print(first_list > second_list)


#################################

class Location:
    """
    A class representing a location with 2 coordinates.
    """
    def __init__(self, x, y):
        """
        Constructor

        :param x: x coordinate of the location.
        :param y: y coordinate of the location.
        """
        self.x = x
        self.y = y

    @property
    def x(self):
        """
        Getter

        :return: An instance of x.
        """
        return self._x

    @x.setter
    def x(self, x):
        """
        Set the x instance to the parameter sent if it is an integer or a float else throw exception.

        :param x: The new x coordinate to set.
        """
        if not isinstance(x, int) and not isinstance(x, float):
            raise TypeError(f"type of '{x}' is not an integer nor a float")
        self._x = x

    @property
    def y(self):
        """
        Getter

        :return: An instance of y.
        """
        return self._y

    @y.setter
    def y(self, y):
        """
        Set the y instance to the parameter sent if it is an integer or a float else throw exception.

        :param y: The new y coordinate to set.
        """
        if not isinstance(y, int) and not isinstance(y, float):
            raise TypeError(f"type of '{y}' is not an integer nor a float")
        self._y = y

    def __str__(self):
        """
        Return string of the location.
        
        :return: String
        """
        return ''.join('(' + str(self.x) + ", " + str(self.y) + ')')


if __name__ == '__main__':
    player = Player()
    enemy = Enemy()

    player.move()
    enemy.move()

    try:
        is_greater_than(29, 7)
        is_greater_than(3.768, 99.8765)
        is_greater_than("akkaks", "oooooo")
        is_greater_than([1, 2, 44], [1, 2, 43])
        is_greater_than([3, "abc", 2.5], [3, "xyz", 5.7])
        is_greater_than(8, "string")  # raise exception
        is_greater_than([1, 2, 44], ["dffggs", 2, 43])  # raise exception
    except TypeError as e:
        print(e)

    try:
        location = Location(4.5, 5)
        print(location)

        location.x = 17
        print(location)

        location.y = 533.3333
        print(location)

        location = Location("some string", 6)  # raise exception
        print(location)

        location = Location(7.5, [1, 2, 3])  # raise exception
        print(location)

    except TypeError as e:
        print(e)
