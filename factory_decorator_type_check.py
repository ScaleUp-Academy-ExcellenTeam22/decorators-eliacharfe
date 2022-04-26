from functools import wraps


class CustomError(Exception):
    pass


def type_check(correct_type):
    def decorator_check_parameter_type(function):
        @wraps(function)
        def inner_calculation_function(argument):
            if not correct_type == type(argument):
                raise CustomError(f"{argument} is not of type {correct_type}")
            return function(argument)
        return inner_calculation_function
    return decorator_check_parameter_type


@type_check(int)
def times2int(num):
    return num * 2


@type_check(float)
def times2float(num):
    return num * 2


@type_check(str)
def join_hello(name):
    return ''.join(f"Hello {name}")


if __name__ == '__main__':
    try:
        times2int(5)
        print(times2int(20))
        times2int(3.5)
    except CustomError as e:
        print(e)

    try:
        times2int('dsjaka')
    except CustomError as e:
        print(e)

    try:
        times2float(4.7)
        times2float(4)
    except CustomError as e:
        print(e)

    try:
        times2float('dsjaka')
    except CustomError as e:
        print(e)

    try:
        join_hello('Boby')
        join_hello(7.8)
    except CustomError as e:
        print(e)

    try:
        join_hello(2)
    except CustomError as e:
        print(e)
