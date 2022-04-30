from pyclbr import Function
from typing import Callable

import decorator


def twice_decorator(func: Function) -> Callable:
    """
    A decorator that executes the function it wraps twice.

    :param func: The function that have the property @twice_decorator that been called.
    :return: Decorator of the inner function.
    """
    def wrapped_function(function, argument) -> int:
        """
        Get a function and its argument, call the function with the argument then return its return
        value.

        :param function: The function that been called (outside).
        :param argument: The argument of the function sent.
        :return:
        """
        function(argument)
        return function(argument)
    return decorator.decorator(wrapped_function, func)


@twice_decorator
def times2(num: int) -> int:
    """
    Get an integer and multiply it by 2.

    :param num: An integer.
    :return: The integer sent multiply by 2.
    """
    print("in times2 function")
    return num * 2


if __name__ == '__main__':

    times2(5)


