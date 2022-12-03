"""
Lesson 13. Homework
"""

from functools import wraps

"""
Task 1
Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!
For example:
 "add called with 4, 5"
"""


def logger(func):
    def wrapper(*args):
        print(f'{func.__name__} called with {", ".join(str(arg) for arg in args)}')
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


# add(10, 20, 30)

"""
Task 2
Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
"""


def stop_words(words: list):
    def wrapper(func):
        @wraps(func)
        def replacer(*args):
            res = func(*args)
            for word in words:
                res = res.replace(word, "*")
            return res
        return replacer
    return wrapper


@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"


# print(create_slogan('Steve'))
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

"""
Task 3
Write a decorator `arg_rules` that validates arguments passed to the function.
A decorator should take 3 arguments:
max_length: 15
type_: str
contains: [] - list of symbols that an argument should contain
If some of the rules' checks returns False, the function should return False and print the reason it failed;
otherwise, return the result.
"""


def arg_rules(type_: type, max_length: int, contains: list):
    def check_func(func):
        @wraps(func)
        def check_args(arg):
            if type(arg) != type_:
                print(f'Type of arg "{arg}" is not "{type_}"!')
                return False
            if len(arg) > max_length:
                print(f'Length of "{arg}" is longer than {max_length} symbols!')
                return False
            for symbol in contains:
                if symbol not in arg:
                    print(f'"{arg}" does not contain {contains} symbols!')
                    return False
            return func(arg)
        return check_args
    return check_func


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'