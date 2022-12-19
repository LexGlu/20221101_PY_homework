"""
Lesson 18. Homework
"""

import re
import secrets
from functools import wraps

"""
Task 1.
Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
passed to the constructor. The logic inside the `validate` method could be to check if the passed email parameter
is a valid email string.
"""


class Email:

    def __init__(self, email: str):
        Email.validate(email)

    @classmethod
    def validate(cls, email):
        pattern = r'([a-z|A-Z|0-9]+[.-_])*[a-zA-Z0-9]+@{1}[a-zA-Z0-9]+(\.[a-zA-Z]{2,})+'
        if re.fullmatch(pattern, email) and 3 <= len(email.split('@')[0]) <= 64:
            print('Email is valid!')
        else:
            print('Email is invalid!')


# tests
# Email('boris.johnson@gov.co.uk')
# Email('boris..johnson@gov.co.uk')
# Email('boris.johnson_@gov.co.uk')
# Email('boris.johnson@gov_co.uk')
# Email('boris.johnson@gov.c')
# Email('b@gov.co.uk')
# Email('b12@gov.co.uk')
# Email('BoRiS_jOhNsOn@gov.co.uk')


"""
Task 2.
Implement 2 classes, the first one is the Boss and the second one is the Worker.
Worker has a property 'boss', and its value must be an instance of Boss.
You can reassign this value, but you should check whether the new value is Boss.
Each Boss has a list of his own workers.
You should implement a method that allows you to add workers to a Boss.
You're not allowed to add instances of Boss class to workers list directly via access to attribute,
use getters and setters instead!
You can refactor the existing code.
"""


class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []
        # dict probably could be better (worker.id as key and instance of Worker as value)
        # added alternative with dicts
        self.workers_dict = {}

    def __str__(self):
        workers_repr = "\n".join(f"{i+1}) {self.workers_dict[worker]}" for i, worker in enumerate(self.workers_dict))

        return f'Boss name: {self.name}, company: {self.company}\n'\
               f'Workers:\n' \
               f'{workers_repr}'


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss
        boss.workers.append(self)
        boss.workers_dict[self.id] = self

    def upd_ex_boss_workers(self):
        self._boss.workers = [i for i in self._boss.workers if i != self]
        del self._boss.workers_dict[self.id]  # for dict

    def __repr__(self):
        return self.name

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, boss_inst: Boss):
        if boss_inst.__class__.__name__ == Boss.__name__:
            self.upd_ex_boss_workers()
            self._boss = boss_inst
            self._boss.workers.append(self)
            self._boss.workers_dict[self.id] = self  # for dict
        else:
            print('Argument should be instance of a Boss class!')

    @boss.deleter
    def boss(self):
        self.upd_ex_boss_workers()
        del self._boss


def id_generator(length: int):
    nums = list(range(10))
    res_lst = [str(secrets.choice(nums)) for i in range(length)]
    while res_lst[0] == '0':  # added to assure that number won't start from 0
        res_lst[0] = str(secrets.choice(nums))
    return int("".join(i for i in res_lst))


# boss1 = Boss(id_generator(6), 'Frank Cowperwood', 'Titan')
# boss2 = Boss(id_generator(6), 'Bill Gates', 'Microsoft')
#
# worker1 = Worker(id_generator(6), 'Algernon', boss1.company, boss1)
# worker2 = Worker(id_generator(6), 'Charles Yerkes', boss1.company, boss1)
#
# print(f'Initial info about {boss1.name}\n{boss1}')
#
# worker1.boss = boss2
# print(f'\nInfo about {boss1.name} after {worker1} quit his job in {boss1.company}\n{boss1}')
# print(f'\nInfo about {boss2.name} after {worker1} joined {boss2.company}\n{boss2}')


"""
Task 3.
Write a class TypeDecorators which has several methods for converting results of functions to a specified type
(if it's possible):
methods:
to_int
to_str
to_bool
to_float
Don't forget to use @wraps
"""


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args):
            try:
                res = int(func(*args))
            except TypeError or ValueError:
                res = func(*args)
                print(f'{type(func(*args)).__name__} cannot be converted to int!')
            return res
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args):
            res = str(func(*args))
            return res
        return wrapper

    @staticmethod
    def to_float(func):

        @wraps(func)
        def wrapper(*args):
            try:
                res = float(func(*args))
            except TypeError or ValueError:
                res = func(*args)
                print(f'{type(func(*args)).__name__} cannot be converted to float!')
            return res

        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args):
            res = bool(func(*args))
            return res
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


@TypeDecorators.to_float
def do_anything(integer: int):
    return integer


assert do_nothing('25') == 25
assert do_something('True') is True
