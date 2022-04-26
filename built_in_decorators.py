from abc import ABC, abstractmethod


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


if __name__ == '__main__':
    p = Player()
    p.move()

    e = Enemy()
    e.move()