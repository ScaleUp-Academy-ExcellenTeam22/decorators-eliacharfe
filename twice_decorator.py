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
def print_argument(num: int) -> None:
    """
    Get an integer and print it.
    :param num: An integer.
    """
    print(num)


if __name__ == '__main__':
    print_argument(5)


