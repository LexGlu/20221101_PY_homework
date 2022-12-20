"""
Lesson 19. Homework
"""

import itertools


"""
Task 1
Create your own implementation of a built-in function enumerate, named `with_index`, which takes two parameters:
`iterable` and `start`, default is 0. Tips: see the documentation for the enumerate function
"""


def with_index(iterable, start=0):
    iter_length = len(iterable)
    return zip(range(start, iter_length + start), iterable)


# alternative with itertools.count
# def with_index(iterable, start=0):
#     return zip(itertools.count(start), iterable)


test = 'abcdefgh'

for index, element in with_index(test):
    print(index, element)

# added for comparison (works the same)
# for index, element in enumerate(test, 10):
#     print(index, element)


"""
Task 2
Create your own implementation of a built-in function range, named in_range(), which takes three parameters: `start`,
`end`, and optional step. Tips: See the documentation for `range` function
"""


def in_range(start, end, step=1):
    lst = []
    ind = start
    while ind < end:
        lst.append(ind)
        ind += step
    return tuple(lst)


print(in_range(0, 10, 2))


"""
Task 3
Create your own implementation of an iterable, which could be used inside for-in loop. Also, add logic for retrieving
elements using square brackets syntax.
(тобто iterator[i], де iterator власне ітератор, i - індекс елемента колекції, на яку "натравлений" ітератор).
"""


class QubeMe:

    def __init__(self, data):
        self.data = data
        self.index = 0
        self.length = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration
        else:
            self.index += 1
            return self.data[self.index - 1] ** 3


lst1 = [1, 2, 3, 4, 5, 6]
iter_something = QubeMe(lst1)


for i in iter_something:
    print(i)
