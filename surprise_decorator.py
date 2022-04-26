

class CustomError(Exception):
    pass


def surprise_decorator(function):
    def inner(argument):
        print("Surprise!")
    return inner


@surprise_decorator
def times2int(num):
    return num * 2


@surprise_decorator
def times2float(num):
    return num * 2


@surprise_decorator
def join_hello(name):
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

