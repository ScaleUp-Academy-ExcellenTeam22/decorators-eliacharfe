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
def func(first_integer: int, second_integer: int):
    print(first_integer > second_integer)


@is_greater_than.register(float)
def func(first_float: float, second_float: float):
    print(first_float > second_float)


@is_greater_than.register(str)
def func(first_string: str, second_string: str):
    print(first_string > second_string)


@is_greater_than.register(list)
def func(first_list, second_list):
    print(first_list > second_list)


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
