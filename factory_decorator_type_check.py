from functools import wraps
from typing import Callable


class CustomError(TypeError):
    def __init__(self, message):
        super().__init__(message)


def type_check(correct_type: type) -> Callable:
    """
    A decorator factory which returns a decorator that decorates functions with one argument.
    Get a type and return a decorator that checks if the parameter the function receives is of
    the correct type.

    :param correct_type: The correct type that the argument sent to the function should be.
    :return: A decorator that checks if the parameter the function receives is of the correct type.
    """
    def decorator_check_parameter_type(function):
        """
        A decorator that get a function and returns the return value of an inner function that
        check if the argument sent to the function is of the correct type.

        :param function: The function that need to check if got the correct type like defined.
        to the function.
        :return: The return value of the inner function.
        """
        @wraps(function)
        def inner_calculation_function(argument):
            """
            Get the argument sent to the function and raise exception if the type of the argument
            is not like the type defined to the function, if not raised, return the return value
            of the function.

            :param argument: The argument sent to the function.
            :return: The return value of the function that should be test its argument..
            """
            if not correct_type == type(argument):
                raise CustomError(f"{argument} is not of type {correct_type}")
            return function(argument)
        return inner_calculation_function
    return decorator_check_parameter_type


@type_check(int)
def times2int(num: int) -> int:
    """
    Get an integer and return the integer multiply by 2.

    :param num: An integer.
    :return: The integer sent multiply by 2.
    """
    return num * 2


@type_check(float)
def times2float(num: float) -> float:
    """
    Get a float and return the float multiply by 2.

    :param num: A float number.
    :return: The float sent multiply by 2.
    """
    return num * 2


@type_check(str)
def join_hello(name: str) -> str:
    """
    Get a string and return a string which start by "Hello" then the string sent.
    
    :param name: The string sent.
    :return: A string which start by "Hello" then the string sent.
    """
    return ''.join(f"Hello {name}")


def try_function(function, argument):
    try:
        function(argument)
    except CustomError as e:
        print(e)


if __name__ == '__main__':

    try_function(times2int, 20)
    try_function(times2int, 3.5)  # raise exception
    try_function(times2int, "Some string")  # raise exception

    try_function(times2float, 4.7)
    try_function(times2float, 4)  # raise exception
    try_function(times2float, "Some string")  # raise exception

    try_function(join_hello, "Jhon")  # raise exception
    try_function(join_hello, 3)  # raise exception
    try_function(join_hello, 7.8)  # raise exception

