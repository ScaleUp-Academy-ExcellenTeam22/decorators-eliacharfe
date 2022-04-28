from abc import ABC, abstractmethod
from functools import singledispatch


class Movable(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Player(Movable):
    def __init__(self):
        super().__init__()

    def move(self):
        print("can move to all direction")


class Enemy(Movable):
    def __init__(self):
        super().__init__()

    def move(self):
        print("can move only right or left")


###################################

@singledispatch
def is_greater_than(x, y):
    raise TypeError()


@is_greater_than.register(int)
def _(first_integer: int, second_integer: int):
    print(first_integer > second_integer)


@is_greater_than.register(float)
def _(first_float: float, second_float: float):
    print(first_float > second_float)


@is_greater_than.register(str)
def _(first_string: str, second_string: str):
    print(first_string > second_string)


@is_greater_than.register(list)
def _(first_list, second_list):
    print(first_list > second_list)


#################################

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if not isinstance(x, int) and not isinstance(x, float):
            raise TypeError(f"type of '{x}' is not an integer nor a float")
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if not isinstance(y, int) and not isinstance(y, float):
            raise TypeError(f"type of '{y}' is not an integer nor a float")
        self._y = y

    def __str__(self):
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
