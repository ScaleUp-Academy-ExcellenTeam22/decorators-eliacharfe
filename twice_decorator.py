import decorator


class CustomError(Exception):
    pass


def twice_decorator(func):
    def wrapped_function(function, argument):
        function(argument)
        return function(argument)
    return decorator.decorator(wrapped_function, func)


@twice_decorator
def times2(num):
    print("in times2")
    return num * 2


if __name__ == '__main__':

    try:
        times2(5)
    except Exception as e:
        print(e)