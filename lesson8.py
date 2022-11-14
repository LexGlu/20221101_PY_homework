"""
LESSON 8
"""

"""
Task 1. A simple function.
Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
The function should then print “My favorite movie is named {name}”. 
"""


def favorite_movie():
    movie = input('Enter name of your favorite movie: ')
    print(f'My favorite movie is named {movie}')


"""
Task 2. Creating a dictionary.
Create a function called make_country, which takes in a country’s name and capital as parameters.
Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
Make the function print out the values of the dictionary to make sure that it works as intended.
"""


def make_country(name, capital, **kwargs):  # kwargs added for alternative version
    print({name: capital})  # not sure about expected output from the task description, so added alternative below

    # alternative
    # country = {'name': name, 'capital': capital}
    # for key, value in kwargs.items():
    #     country[key] = value
    # print(country)


"""
Task 3. A simple calculator.
Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter 
(to keep things simple let it only be ‘+’, ‘-’ or ‘*’)
and an arbitrary number of arguments (only numbers) as the second parameter.
Then return the sum or product of all the numbers in the arbitrary parameter. For example:

the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42  
"""


def make_operation(operator, *args):

    res = args[0]  # 0 (as value) was not assigned, 'cause make_operation(‘-’, 5, 5, -10, -20) will NOT return 30
    if operator == '-':
        for i in args[1:]:
            res -= i
    elif operator == '+':
        for i in args[1:]:
            res += i
    else:
        for i in args[1:]:
            res *= i

    # alternative using eval() function
    # for i in args[1:]:
    #     res = eval(f'{res} {operator} {i}')

    return res


favorite_movie()
make_country('Peru', 'Lima')
# make_country('Peru', 'Lima', population=33600000, currency='Sol')
print(make_operation('+', 7, 7, 2))  # 16
print(make_operation('-', 5, 5, -10, -20))  # 30
print(make_operation('*', 7, 6))  # 42
