from typing import Callable
from decorator import decorator


@decorator
def twice_decorator(function: Callable, argument: any) -> Callable:
    """
    A decorator that executes the function it wraps twice.
    :param function: The function that have the property @twice_decorator that been called.
    :param argument: The argument to the function.
    :return: Decorator of the inner function.
    """
    function(argument)
    return function(argument)


@twice_decorator
def times2(num: int) -> int:
    """
    Get an integer and multiply it by 2.
    :param num: An integer.
    :return: The integer sent multiply by 2.
    """
    print(num)


if __name__ == '__main__':
    times2(5)


