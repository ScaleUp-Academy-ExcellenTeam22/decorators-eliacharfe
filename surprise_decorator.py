class CustomError(Exception):
    pass


def surprise_decorator(function):
    """
    A decorator that decorate a function with/without arguments, and print "surprise"
    instead of the original functionality of the function.
    :param function: A function that have the property "surprise_decorator".
    :return: The inner function.
    """

    def inner(*args) -> None:
        """
        Ignore the arguments and print “surprise!”.
        :param args: The arguments of the function.
        """
        print("Surprise!")

    return inner


@surprise_decorator
def times2int(num):
    """
    Get an integer and return the integer multiply by 2.
    :param num: An integer.
    :return: The integer sent multiply by 2.
    """
    return num * 2


@surprise_decorator
def times2float(num):
    """
    Get a float and return the float multiply by 2.
    :param num: A float number.
    :return: The float sent multiply by 2.
    """
    return num * 2


@surprise_decorator
def join_hello(name):
    """
    Get a string and return a string which start by "Hello" then the string sent.
    :param name: The string sent.
    :return: A string which start by "Hello" then the string sent.
    """
    return ''.join(f"Hello {name}")


if __name__ == '__main__':
    times2int(5)
    times2int(3.5)
    times2int('dsjaka')

    times2float(4.7)
    times2float(4)
    times2float('dsjaka')

    join_hello('Boby')
    join_hello(7.8)
    join_hello(2)
